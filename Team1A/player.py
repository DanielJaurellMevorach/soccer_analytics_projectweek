import cv2
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Path to frames directory
FRAME_DIR = r"C:\Users\Daniel\Desktop\UCLL\AdvancedAI\OHL\soccer_analytics_projectweek\Team1A\frames"
frames = sorted([os.path.join(FRAME_DIR, f) for f in os.listdir(FRAME_DIR) if f.endswith(('png', 'jpg', 'jpeg'))])

# GUI Setup
class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Frame Player")
        
        self.frame_index = 0
        self.playing = False
        self.slider_update = False  # Flag to prevent recursion
        
        # Create a label to display images
        self.label = ttk.Label(root)
        self.label.pack()
        
        # Slider for timeline
        self.slider = ttk.Scale(root, from_=0, to=len(frames)-1, orient="horizontal", command=self.slider_moved)
        self.slider.pack(fill="x")
        
        # Play/Pause Button
        self.play_button = ttk.Button(root, text="Play", command=self.toggle_playback)
        self.play_button.pack()
        
        self.update_frame()
    
    def update_frame(self):
        if self.frame_index >= len(frames):
            self.frame_index = 0  # Loop back to start
        
        # Load and display the frame
        img = Image.open(frames[self.frame_index])
        img = img.resize((640, 480), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.label.config(image=img_tk)
        self.label.image = img_tk
        
        # Update slider without triggering its callback
        self.slider_update = True
        self.slider.set(self.frame_index)
        self.slider_update = False
        
        if self.playing:
            self.frame_index += 1
            self.root.after(33, self.update_frame)  # ~30 FPS
    
    def toggle_playback(self):
        self.playing = not self.playing
        self.play_button.config(text="Pause" if self.playing else "Play")
        if self.playing:
            self.update_frame()
    
    def slider_moved(self, val):
        # If this is a programmatic update, ignore it
        if self.slider_update:
            return
        # Update frame index and display frame
        self.frame_index = int(float(val))
        self.update_frame()

# Run Application
root = tk.Tk()
app = VideoPlayer(root)
root.mainloop()
