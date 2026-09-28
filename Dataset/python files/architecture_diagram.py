import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure
fig, ax = plt.subplots(figsize=(9, 15))
ax.set_xlim(0, 10)
ax.set_ylim(-2, 24)
ax.axis('off')

def draw_box(center_y, text):
    height = 1.8
    box = FancyBboxPatch(
        (1.5, center_y - height/2), 7, height,
        boxstyle="round,pad=0.4",
        edgecolor="#0B3C7D",
        facecolor="#EAF2FF",
        linewidth=2
    )
    ax.add_patch(box)

    ax.text(5, center_y, text,
            ha='center', va='center',
            fontsize=11,
            fontweight='bold',
            color="#0B3C7D")

# Steps
steps = [
    "Car Price Dataset (CSV - 152MB)",
    "HDFS Storage",
    "MapReduce Processing\n(Average Price by Brand)",
    "Hive Layer (SQL Queries)",
    "Pig Layer (Data Cleaning & Aggregation)",
    "HBase Layer (NoSQL Storage)",
    "Python Dashboard & Visualization",
    "Business Insights & Analysis"
]

# Proper spacing
y_positions = [21, 18, 15, 12, 9, 6, 3, 0]

for y, step in zip(y_positions, steps):
    draw_box(y, step)

# Draw clean arrows between box centers
for i in range(len(y_positions) - 1):
    ax.annotate(
        "",
        xy=(5, y_positions[i] - 1),
        xytext=(5, y_positions[i+1] + 1),
        arrowprops=dict(
            arrowstyle="simple",
            color="#0B3C7D",
            linewidth=1.5
        )
    )

# Title
ax.text(5, 23,
        "Hadoop Ecosystem Project Architecture",
        ha='center',
        fontsize=16,
        fontweight='bold',
        color="#0B3C7D")

# SAVE BEFORE SHOW
plt.savefig("project_architecture_professional.png",
            dpi=300,
            bbox_inches='tight')

plt.show()