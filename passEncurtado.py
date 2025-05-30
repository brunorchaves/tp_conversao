import numpy as np
import matplotlib.pyplot as plt

# Substitua 'dados.txt' pelo caminho do seu arquivo
# Ele deve conter duas colunas: 
#   coluna 1 = comprimento (mm)
#   coluna 2 = H
# separadas por espaço ou tab.
arquivo = 'h_encurtado.txt'

# Carrega o arquivo (pula linhas em branco e comentários iniciados em '#')
data = np.loadtxt(arquivo, comments='#')

# Se o arquivo tiver colunas invertidas, use: data = np.loadtxt(arquivo, usecols=(1,0))
length_mm = data[:, 0]
H = data[:, 1]

# Plota
plt.figure(figsize=(8, 5))
plt.plot(length_mm, H, marker='o', linestyle='-')
plt.xlabel('Comprimento (mm)')
plt.ylabel('H')
plt.title('H vs Comprimento')
plt.grid(True)
plt.tight_layout()
plt.show()
