import os

def generate_kp_chart(planets):

    fig, ax = plt.subplots(figsize=(6,6))

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    circle = plt.Circle((0,0), 1, fill=False)
    ax.add_artist(circle)

    for i in range(12):
        angle = np.deg2rad(i * 30)
        x = np.cos(angle)
        y = np.sin(angle)
        ax.plot([0, x], [0, y], 'gray')

    for planet, data in planets.items():
        angle = np.deg2rad(data["degree"])
        x = 0.8 * np.cos(angle)
        y = 0.8 * np.sin(angle)

        ax.text(x, y, planet, fontsize=10, ha='center')

    ax.axis("off")

    # 🔥 SAFE PATH (auto create)
    os.makedirs("static", exist_ok=True)

    file_path = os.path.join("static", "kp_chart.png")
    plt.savefig(file_path)

    return "kp_chart.png"