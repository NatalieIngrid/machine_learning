import numpy as np
import matplotlib.pyplot as plt


mu = [0, 0]
sigma = [1, 1]
n_points = 100

rng = np.random.default_rng()
points_x = rng.normal(mu[0], sigma[0], n_points)
points_y = rng.normal(mu[1], sigma[1], n_points)

fig = plt.figure(figsize=(15, 5))

ax_main = fig.add_subplot(122)
ax_main.scatter(points_x, points_y, alpha=0.6, label='Точки')

theta = np.linspace(0, 2*np.pi, 100)
r_99 = 2.576 * max(sigma[0], sigma[1])
r_3sigma = 3 * max(sigma[0], sigma[1])

circle_99 = plt.Circle(mu, r_99, fill=False, color='red', linestyle='--',
                      label=f'Окружность 99% (r={r_99:.2f})')
circle_3sigma = plt.Circle(mu, r_3sigma, fill=False, color='green', linestyle=':',
                          label=f'Окружность 3сигма (r={r_3sigma:.2f})')

ax_main.add_patch(circle_99)
ax_main.add_patch(circle_3sigma)
ax_main.plot(mu[0], mu[1], 'ko', markersize=10, label='Центр μ')
ax_main.set_aspect('equal')
ax_main.grid(True)
ax_main.legend()
ax_main.set_title('Нормальное распределение точек')
ax_main.set_xlabel('X')
ax_main.set_ylabel('Y')

ax_x = fig.add_subplot(121)
ax_x.hist(points_x, bins=10, density=True, alpha=0.6, label='Гистограмма')
x_range = np.linspace(min(points_x), max(points_x), 100)

x_density = (1/(sigma[0] * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x_range - mu[0])/sigma[0])**2)
ax_x.plot(x_range, x_density, 'r-', label='Плотность распределения')
ax_x.set_title('Распределение X')
ax_x.set_xlabel('X')
ax_x.set_ylabel('Плотность')
ax_x.legend()

ax_y = ax_x.twinx()
ax_y.hist(points_y, bins=10, density=True, alpha=0.3, label='Гистограмма')
y_range = np.linspace(min(points_y), max(points_y), 100)

y_density = (1/(sigma[1] * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((y_range - mu[1])/sigma[1])**2)
ax_y.plot(y_range, y_density, 'g-', label='Плотность распределения')
ax_y.set_title('Распределение Y')
ax_y.set_xlabel('Y')
ax_y.set_ylabel('Плотность')
ax_y.legend()

plt.tight_layout()
plt.show()