import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================================
# КОНСТАНТЫ
# ==========================================================
G = 6.67430e-11
AU = 1.496e11
DAY = 86400

# ==========================================================
# ВСПОМОГАТЕЛЬНОЕ
# ==========================================================
def rotate(vec, angle):
    """Поворот вектора на угол (рад)"""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        c * vec[0] - s * vec[1],
        s * vec[0] + c * vec[1]
    ])

# ==========================================================
# КЛАСС НЕБЕСНОГО ТЕЛА
# ==========================================================
class Body:
    def __init__(self, name, mass, position, velocity, color):
        self.name = name
        self.mass = mass
        self.pos = np.array(position, dtype=float)
        self.vel = np.array(velocity, dtype=float)
        self.color = color
        self.traj = [self.pos.copy()]

# ==========================================================
# ГРАВИТАЦИЯ
# ==========================================================
def compute_accelerations(bodies):
    accs = []
    for i, bi in enumerate(bodies):
        acc = np.zeros(2)
        for j, bj in enumerate(bodies):
            if i == j:
                continue
            r = bj.pos - bi.pos
            d = np.linalg.norm(r)
            acc += G * bj.mass * r / d**3
        accs.append(acc)
    return accs

# ==========================================================
# LEAPFROG
# ==========================================================
def leapfrog_step(bodies, dt):
    acc = compute_accelerations(bodies)

    for b, a in zip(bodies, acc):
        b.vel += 0.5 * dt * a

    for b in bodies:
        b.pos += dt * b.vel

    acc_new = compute_accelerations(bodies)

    for b, a in zip(bodies, acc_new):
        b.vel += 0.5 * dt * a
        b.traj.append(b.pos.copy())

# ==========================================================
# ИНИЦИАЛИЗАЦИЯ СИСТЕМЫ
# ==========================================================
sun = Body(
    "Sun",
    1.989e30,
    [0, 0],
    [0, 0],
    "yellow"
)

# ---------- Земля ----------
earth_orbit_angle = np.radians(2)
earth_pos = rotate(np.array([AU, 0]), earth_orbit_angle)
earth_vel = rotate(np.array([0, 29_780]), earth_orbit_angle)

earth = Body(
    "Earth",
    5.972e24,
    earth_pos,
    earth_vel,
    "blue"
)

# ---------- Луна ----------
moon_distance = 384_400_000
moon_speed = 1_022

moon_pos = earth.pos + rotate(
    np.array([moon_distance, 0]),
    np.radians(5)
)
moon_vel = earth.vel + rotate(
    np.array([0, moon_speed]),
    np.radians(5)
)

moon = Body(
    "Moon",
    7.35e22,
    moon_pos,
    moon_vel,
    "gray"
)

# ---------- Марс ----------
mars_orbit_angle = np.radians(-3)
mars_pos = rotate(np.array([1.524 * AU, 0]), mars_orbit_angle)
mars_vel = rotate(np.array([0, 24_077]), mars_orbit_angle)

mars = Body(
    "Mars",
    6.39e23,
    mars_pos,
    mars_vel,
    "red"
)

# ---------- Фобос ----------
phobos_distance = 9_378_000
phobos_speed = 2_138

phobos_pos = mars.pos + np.array([phobos_distance, 0])
phobos_vel = mars.vel + np.array([0, phobos_speed])

phobos = Body(
    "Phobos",
    1.06e16,
    phobos_pos,
    phobos_vel,
    "black"
)

bodies = [sun, earth, moon, mars, phobos]

# ==========================================================
# ПАРАМЕТРЫ СИМУЛЯЦИИ
# ==========================================================
dt = DAY
steps = 2500

# ==========================================================
# ВИЗУАЛИЗАЦИЯ
# ==========================================================
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-2 * AU, 2 * AU)
ax.set_ylim(-2 * AU, 2 * AU)
ax.set_title("Solar System with Moons (N-body, Leapfrog)")

lines = {}
points = {}

for b in bodies:
    lines[b.name], = ax.plot([], [], lw=1, color=b.color, label=b.name)
    points[b.name], = ax.plot([], [], "o", color=b.color)

ax.legend(loc="upper right")

def update(frame):
    leapfrog_step(bodies, dt)

    for b in bodies:
        traj = np.array(b.traj)
        lines[b.name].set_data(traj[:, 0], traj[:, 1])
        points[b.name].set_data([b.pos[0]], [b.pos[1]])

    return list(lines.values()) + list(points.values())

ani = FuncAnimation(fig, update, frames=steps, interval=20)
plt.show()
