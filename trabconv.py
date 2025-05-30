import math
import pandas as pd

def calcular_fatores_e_corrente(q, passo_graus, gamma_eletrico, N_bobinas_por_fase, polos, B_max=1.7, g=0.0005):
    """
    Calcula Kd, Kp, Kw e corrente eficaz necessária para atingir B_max.

    Parâmetros:
    - q: número de ranhuras por polo por fase
    - passo_graus: ângulo do passo da bobina em graus elétricos
    - gamma_eletrico: ângulo entre ranhuras consecutivas em graus elétricos
    - N_bobinas_por_fase: número total de espiras por fase
    - polos: número total de polos
    - B_max: densidade de fluxo máxima no núcleo (T)
    - g: entreferro (m)

    Retorna:
    - dicionário com Kd, Kp, Kw, corrente de pico e eficaz
    """
    # Conversões para radianos
    gamma_rad = math.radians(gamma_eletrico)
    passo_rad = math.radians(passo_graus)

    # Fator de distribuição (Kd)
    Kd = math.sin(q * gamma_rad / 2) / (q * math.sin(gamma_rad / 2))

    # Fator de passo (Kp)
    Kp = math.sin(passo_rad / 2)

    # Fator de enrolamento
    Kw = Kd * Kp

    # Cálculo da FMM necessária
    mu0 = 4 * math.pi * 1e-7
    Fs = B_max * g / mu0

    # Corrente de pico usando fórmula do formulário (6a)
    p = polos / 2
    I_pico = Fs * p / ((3/2) * (4/math.pi) * Kw * N_bobinas_por_fase)

    # Corrente eficaz
    I_ef = I_pico / math.sqrt(2)

    return {
        'Kd': round(Kd, 4),
        'Kp': round(Kp, 4),
        'Kw': round(Kw, 4),
        'I_pico (A)': round(I_pico, 2),
        'I_ef (A)': round(I_ef, 2)
    }

# Casos para comparação
caso1 = calcular_fatores_e_corrente(
    q=3,
    passo_graus=160,
    gamma_eletrico=40,
    N_bobinas_por_fase=6*20,
    polos=4
)

caso2 = calcular_fatores_e_corrente(
    q=3,
    passo_graus=180,
    gamma_eletrico=30,
    N_bobinas_por_fase=6*20,
    polos=4
)

# Exibir resultados em uma tabela com pandas
df = pd.DataFrame([caso1, caso2], index=["Caso 1", "Caso 2"])
print(df)
