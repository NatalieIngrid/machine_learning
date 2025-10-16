import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

mu = [0, 0]
sigma = [1, 1]
n_points = 100

rng = np.random.default_rng()
points_x = rng.normal(mu[0], sigma[0], n_points)
points_y = rng.normal(mu[1], sigma[1], n_points)

plt.figure(figsize=(10, 10))

plt.scatter(points_x, points_y, alpha=0.6, label='Точки')


theta = np.linspace(0, 2*np.pi, 100)
r_99 = 2.576 * max(sigma[0], sigma[1])
r_3sigma = 3 * max(sigma[0], sigma[1])

circle_99 = plt.Circle(mu, r_99, fill=False, color='red', linestyle='--',
                      label=f'Окружность 99% (r={r_99:.2f})')
circle_3sigma = plt.Circle(mu, r_3sigma, fill=False, color='green', linestyle=':',
                          label=f'Окружность 3сигма (r={r_3sigma:.2f})')

ax = plt.gca()
ax.add_patch(circle_99)
ax.add_patch(circle_3sigma)

plt.plot(mu[0], mu[1], 'ko', markersize=10, label='Центр μ')

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title('Нормальное распределение точек с правилом трёх сигм')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
plt.savefig('distribution.png')