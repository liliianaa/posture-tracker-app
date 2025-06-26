import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
import os
import time
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
from collections import defaultdict
import pandas as pd

st.set_page_config(page_title="Posture Tracking", layout="wide")
st.title("📼 Upload Video - Human Posture Tracking (Sit/Stand) + Time Counter")

# === Posture Timer Class ===
class PostureTimer:
    def __init__(self):
        self.timers = defaultdict(lambda: {"Sit": 0.0, "Stand": 0.0})
        self.current_state = {}
        self.last_update = {}

    def update(self, track_id, label):
        now = time.time()
        if track_id not in self.last_update:
            self.last_update[track_id] = now
            self.current_state[track_id] = label
            return

        prev_label = self.current_state.get(track_id, None)
        elapsed = now - self.last_update[track_id]

        if label == prev_label:
            self.timers[track_id][label] += elapsed
        else:
            self.current_state[track_id] = label

        self.last_update[track_id] = now

    def get_time(self, track_id, label):
        return int(self.timers[track_id][label])

    def reset(self, track_id):
        self.timers[track_id] = {"Sit": 0.0, "Stand": 0.0}
        self.current_state.pop(track_id, None)
        self.last_update.pop(track_id, None)


# === Fungsi untuk Menampilkan Teks dengan Background ===
def draw_label_with_bg(frame, text, pos, font=cv2.FONT_HERSHEY_SIMPLEX,
                       font_scale=0.55, text_color=(255, 255, 255),
                       bg_color=(0, 255, 0), thickness=1, padding=4):
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_w, text_h = text_size
    x, y = pos
    cv2.rectangle(frame, (x - padding, y - text_h - padding),
                         (x + text_w + padding, y + padding),
                         bg_color, cv2.FILLED)
    cv2.putText(frame, text, (x, y), font, font_scale, text_color, thickness)


# === Fungsi untuk Menghasilkan Warna Berdasarkan ID ===
def get_color_from_id(track_id):
    if not isinstance(track_id, int):
        track_id = abs(hash(track_id)) % (2**32)
    np.random.seed(track_id)
    color = np.random.randint(0, 255, size=3)
    return tuple(int(c) for c in color)


# === Load Model & Tracker ===
@st.cache_resource
def load_model():
    return YOLO("best.pt")

@st.cache_resource
def load_tracker():
    return DeepSort(
        max_age=30,
        n_init=3,
        nn_budget=100,
        embedder="mobilenet",
        half=True,
        bgr=True
    )

model = load_model()
tracker = load_tracker()
timer = PostureTimer()

# === Upload File ===
uploaded_file = st.file_uploader("🔼 Upload video MP4", type=["mp4"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error("❌ Gagal membuka video.")
    else:
        st.success("✅ Video berhasil dimuat.")
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 20.0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        st.write(f"**Resolusi:** {width}x{height}, **FPS:** {fps:.2f}, **Frames:** {total_frames}")

        output_path = os.path.join(tempfile.gettempdir(), "output_posture.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        stframe = st.empty()
        progress = st.progress(0)
        frame_count = 0

        label_names = {0: "Sit", 1: "Stand"}

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)[0]

            detections = []
            for r in results.boxes:
                xyxy = r.xyxy[0]
                x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
                conf = float(r.conf[0])
                cls = int(r.cls[0])
                w, h = x2 - x1, y2 - y1
                detections.append(([x1, y1, w, h], conf, cls))

            tracks = tracker.update_tracks(detections, frame=frame)

            for track in tracks:
                if not track.is_confirmed():
                    continue

                track_id = track.track_id
                x1, y1, x2, y2 = map(int, track.to_ltrb())
                label_id = track.get_det_class()
                label = label_names.get(label_id, "Unknown")

                # Warna berdasarkan ID
                color = get_color_from_id(track_id)

                # Update timer
                timer.update(track_id, label)
                sit_time = timer.get_time(track_id, "Sit")
                stand_time = timer.get_time(track_id, "Stand")

                text = f'ID: {track_id} {sit_time}s SIT' if label == "Sit" else f'ID: {track_id} {stand_time}s STAND'

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                draw_label_with_bg(frame, text, (x1, y1 - 10), bg_color=color)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(rgb, channels="RGB")

            out.write(frame)
            frame_count += 1
            progress.progress(min(frame_count / total_frames, 1.0))

        cap.release()
        out.release()
        st.success("✅ Video selesai diproses!")

        # === Simpan CSV Data Durasi ===
        data = []
        for track_id in timer.timers.keys():
            data.append({
                "ID": track_id,
                "Sit Duration (s)": timer.get_time(track_id, "Sit"),
                "Stand Duration (s)": timer.get_time(track_id, "Stand"),
            })

        df = pd.DataFrame(data)
        csv_path = os.path.join(tempfile.gettempdir(), "output_posture.csv")
        df.to_csv(csv_path, index=False)

        # === Tampilkan Tombol Download ===
        col1, col2 = st.columns(2)
        with col1:
            with open(output_path, "rb") as f:
                st.download_button("📥 Download Video Hasil", f, file_name="output_posture.mp4", mime="video/mp4")
        with col2:
            with open(csv_path, "rb") as f:
                st.download_button("📄 Download Data CSV", f, file_name="output_posture.csv", mime="text/csv")
