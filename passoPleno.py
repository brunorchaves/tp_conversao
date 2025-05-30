import numpy as np
import matplotlib.pyplot as plt

# Caminho do seu arquivo de dados (já contendo B em Tesla)
arquivo = 'b_pleno.txt'

# 1) Carrega os dados: 
#    coluna 0 = comprimento (mm), coluna 1 = B (T)
data = np.loadtxt(arquivo, comments='#')
length_mm = data[:, 0]
B = data[:, 1]

# 2) Converte comprimento para ângulo (°): 0 mm → 0°, l_max → 360°
l_max = length_mm.max()
angles_deg = (length_mm / l_max) * 360.0

# 3) Converte B em intensidade de campo H usando H = B / μ₀
mu0 = 4 * np.pi * 1e-7  # H/m
H = B / mu0

# 4) Converte H em Força Magnetomotriz (FMM) usando FMM = H · g (g = 0,50 mm)
g = 0.50  # mm
FMM = H * g

# 5) Plota H vs ângulo
plt.figure(figsize=(8, 5))
plt.plot(angles_deg, H,  linestyle='-')
plt.xlabel('Ângulo (°)')
plt.ylabel('H (A/m)')
plt.title('Intensidade de Campo H vs Ângulo')
plt.grid(True)
plt.tight_layout()

# 6) Plota FMM vs ângulo
plt.figure(figsize=(8, 5))
plt.plot(angles_deg, FMM, linestyle='-')
plt.xlabel('Ângulo (°)')
plt.ylabel('FMM (A·mm)')
plt.title('Força Magnetomotriz (FMM) vs Ângulo')
plt.grid(True)
plt.tight_layout()

# 7) Plota B vs ângulo
plt.figure(figsize=(8, 5))
plt.plot(angles_deg, B, linestyle='-')
plt.xlabel('Ângulo (°)')
plt.ylabel('B (T)')
plt.title('Densidade de Fluxo B vs Ângulo')
plt.grid(True)
plt.tight_layout()

plt.show()
