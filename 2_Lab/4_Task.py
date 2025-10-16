import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_samples = 100

data = np.random.randn(n_samples, 4)

feature_names = ['Длина лепестка', 'Ширина лепестка',
                 'Длина чашелистика', 'Ширина чашелистика']

correlation_matrix = np.corrcoef(data.T)

plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix,
            annot=True,
            fmt='.2f',
            cmap='RdYlGn',
            center=0,
            vmin=-1, vmax=1,
            xticklabels=feature_names,
            yticklabels=feature_names,
            square=True,
            cbar_kws={'shrink': 0.8})

plt.title('Тепловая карта корреляций (Seaborn)', fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

plt.savefig('correlation_heatmap_seaborn.png', dpi=300, bbox_inches='tight')

plt.show()