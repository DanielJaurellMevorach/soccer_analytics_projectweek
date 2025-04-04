import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np

# Directory where PNG frames are saved
output_dir = "c:/Users/Daniel/Desktop/UCLL/AdvancedAI/OHL/soccer_analytics_projectweek/Team1A/frames"

# Load images into a list from folder "frames" in the same directory
# unique_frames = sorted([int(f.split('_')[-1].split('.')[0]) for f in os.listdir(output_dir) if f.startswith("frame_") and f.endswith(".png")])
# img_list = [plt.imread(os.path.join(output_dir, f"frame_{frame_id}.png")) for frame_id in unique_frames[:200]]

if not os.path.exists(output_dir):
    print(f"Directory '{output_dir}' does not exist. Creating it...")
    os.makedirs(output_dir)
    
print(f"Looking for frames in: {os.path.abspath(output_dir)}")

unique_frames = sorted([int(f.split('_')[-1].split('.')[0]) for f in os.listdir(output_dir) if f.startswith("frame_") and f.endswith(".png")])
img_list = [plt.imread(os.path.join(output_dir, f"frame_{frame_id}.png")) for frame_id in unique_frames[:200]]

# Check if images are loaded properly
if not img_list:
    print("No images loaded! Check your file paths.")
    exit()

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))
img_display = ax.imshow(img_list[0], animated=True)
ax.axis("off")  # Hide axes

# Update function for animation
def update(frame_idx):
    img_display.set_array(img_list[frame_idx])  # Update image data
    return [img_display]

# Create animation
ani = FuncAnimation(fig, update, frames=len(img_list), interval=100, blit=True)

# Show animation
plt.show()

# Optional: Save the animation as a GIF
ani.save("football_animation.gif", writer="pillow", fps=10)
print("Animation saved as football_animation.gif!")
