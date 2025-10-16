import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_samples = 100

data = np.random.randn(n_samples, 4)

feature_names = ['Длина лепестка', 'Ширина лепестка',
                 'Длина чашелистика', 'Ширина чашелистика']

correlation_matrix = np.corrcoef(data.T)

plt.figure(figsize=(10, 8))

im = plt.imshow(correlation_matrix, cmap='RdYlGn', aspect='equal', vmin=-1, vmax=1)

plt.colorbar(im)

plt.xticks(range(len(feature_names)), feature_names, rotation=45, ha='right')
plt.yticks(range(len(feature_names)), feature_names)

for i in range(len(feature_names)):
    for j in range(len(feature_names)):
        color = 'white' if abs(correlation_matrix[i, j]) > 0.5 else 'black'
        text = plt.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                       ha='center', va='center', color=color, fontweight='bold')

plt.title('Тепловая карта корреляций (случайные данные)', fontsize=14, pad=20)
plt.tight_layout()

plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')

plt.show()