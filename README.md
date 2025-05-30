# Plot de H vs Comprimento

Este repositório contém um script em Python para ler dados de um arquivo `.txt` e gerar gráficos de:

- **Intensidade de Campo H** vs **Comprimento (mm)**
- **Força Magnetomotriz (FMM)** vs **Ângulo (°)**
- **Densidade de Fluxo (B)** vs **Ângulo (°)**

---

## Arquivos

- `plot_h_from_file.py`: script principal que carrega os dados e plota os gráficos.
- `h_encurtado.txt`: arquivo de exemplo com duas colunas separadas por espaço ou tabulação:
  - **Coluna 0**: comprimento em mm  
  - **Coluna 1**: valores de H (A/m)  

  > **Atenção**: antes de salvar seu arquivo `.txt`, remova as duas primeiras linhas de cabeçalho (por exemplo:
  > ```
  > % Column 0: Length, mm
  > % Column 1: |B|, Tesla
  > ```
  > ), e verifique se o nome do arquivo coincide com o definido na variável `arquivo` dentro do script.

- `requirements.txt`: lista de dependências Python.
- `README.md`: este arquivo.

---

## Pré-requisitos

- Python 3.x  
- `pip`

---

## Instalação

1. Clone este repositório ou faça o download dos arquivos.  
2. Navegue até o diretório do projeto.  
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

1. Garanta que seu arquivo de dados (`h_encurtado.txt`) esteja no mesmo diretório do script.  
2. Execute o script:
   ```bash
   python plot_h_from_file.py
   ```  
3. As janelas com os gráficos de **H**, **FMM** e **B** serão exibidas automaticamente.

---

## Estrutura de Dados

O arquivo de dados deve conter apenas valores numéricos organizados em duas colunas:

```
<comprimento_mm> <valor_H>
```

Exemplo de `h_encurtado.txt` após remover cabeçalhos:

```
0.00000000 -141143.75
0.06021507 -70384.1281
...
3.73333464 -485842.019
```

---

## Personalização

- Para ajustar estilos ou salvar os gráficos em arquivos, edite funções do Matplotlib dentro de `plot_h_from_file.py` (por exemplo, usando `plt.savefig('grafico.png', dpi=300)`).

---

## Licença

Este projeto está licenciado sob a **MIT License**.

---

## Autor

Bruno Ribeiro Chaves
