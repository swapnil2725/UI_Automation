import mss
import imageio
import numpy as np

class ScreenRecorder:
    def __init__(self, output_filename="results/recording.mp4", fps=5):
        self.output_filename = output_filename
        self.fps = fps
        self.frames = []
        self.sct = mss.mss()

    def start_recording(self):
        print("Recording started...")

    def capture_frame(self):
        screenshot = self.sct.grab(self.sct.monitors[0])
        img = np.array(screenshot)
        self.frames.append(img)

    def stop_recording(self):
        imageio.mimsave(self.output_filename, self.frames, fps=self.fps)
        print(f"Recording saved as {self.output_filename}")
