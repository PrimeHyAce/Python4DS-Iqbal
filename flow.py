import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(-6, 10)
ax.axis('off')

# Define shapes and colors
shapes = {
    "start_end": {"shape": "oval", "color": "lightgreen"},
    "process": {"shape": "rectangle", "color": "lightblue"},
    "decision": {"shape": "diamond", "color": "lightcoral"}
}

# Add shapes to the plot
def add_shape(ax, shape_type, xy, text):
    if shape_type == "oval":
        patch = mpatches.Ellipse(xy, width=2, height=1, color=shapes[shape_type]["color"], ec="black")
    elif shape_type == "rectangle":
        patch = mpatches.FancyBboxPatch((xy[0] - 1.5, xy[1] - 0.5), 3, 1, boxstyle="round,pad=0.1", color=shapes[shape_type]["color"], ec="black")
    elif shape_type == "diamond":
        patch = mpatches.RegularPolygon(xy, numVertices=4, radius=1, orientation=np.pi/4, color=shapes[shape_type]["color"], ec="black")
    ax.add_patch(patch)
    ax.text(xy[0], xy[1], text, ha='center', va='center', fontsize=10, color="black")

# Define positions for the shapes
positions = {
    "Power On": (5, 9),
    "Initialize Sensors and Connect to App": (5, 7),
    "Capture Environment with Camera and Sensors": (5, 5),
    "Process Data for Object and Obstacle Detection": (5, 3),
    "Object/Obstacle Detected?": (5, 1.5),
    "Generate Alerts": (7, 0),
    "Notify User of Detected Object/Obstacle": (5, -1.5),
    "User Receives Notification and Takes Action": (5, -3.5),
    "Power Off": (5, -5)
}

# Plot shapes
add_shape(ax, "start_end", positions["Power On"], "Power On")
add_shape(ax, "process", positions["Initialize Sensors and Connect to App"], "Initialize Sensors\nand Connect to App")
add_shape(ax, "process", positions["Capture Environment with Camera and Sensors"], "Capture Environment\nwith Camera and Sensors")
add_shape(ax, "process", positions["Process Data for Object and Obstacle Detection"], "Process Data for Object\nand Obstacle Detection")
add_shape(ax, "decision", positions["Object/Obstacle Detected?"], "Object/Obstacle\nDetected?")
add_shape(ax, "process", positions["Generate Alerts"], "Generate Alerts")
add_shape(ax, "process", positions["Notify User of Detected Object/Obstacle"], "Notify User of Detected\nObject/Obstacle")
add_shape(ax, "process", positions["User Receives Notification and Takes Action"], "User Receives Notification\nand Takes Action")
add_shape(ax, "start_end", positions["Power Off"], "Power Off")

# Draw arrows
def draw_arrow(ax, start, end, text=None):
    arrow = mpatches.FancyArrowPatch(start, end, mutation_scale=10, color="black")
    ax.add_patch(arrow)
    if text:
        ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.2, text, ha='center', va='center', fontsize=10, color="black")

# Define arrows
arrows = [
    ("Power On", "Initialize Sensors and Connect to App"),
    ("Initialize Sensors and Connect to App", "Capture Environment with Camera and Sensors"),
    ("Capture Environment with Camera and Sensors", "Process Data for Object and Obstacle Detection"),
    ("Process Data for Object and Obstacle Detection", "Object/Obstacle Detected?"),
    ("Object/Obstacle Detected?", "Generate Alerts", "Yes"),
    ("Generate Alerts", "Notify User of Detected Object/Obstacle"),
    ("Notify User of Detected Object/Obstacle", "User Receives Notification and Takes Action"),
    ("User Receives Notification and Takes Action", "Power Off"),
    ("Object/Obstacle Detected?", "Capture Environment with Camera and Sensors", "No"),
]

# Plot arrows
for start, end, *text in arrows:
    start_pos = (positions[start][0], positions[start][1] - 0.5)
    end_pos = (positions[end][0], positions[end][1] + 0.5)
    draw_arrow(ax, start_pos, end_pos, text[0] if text else None)

plt.show()