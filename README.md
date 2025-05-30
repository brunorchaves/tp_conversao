# Plot de H vs Comprimento

Este repositório contém um script em Python para ler dados de um arquivo `.txt` e gerar um gráfico de **H** versus **comprimento (mm)**.

## Arquivos

- `plot_h_from_file.py`: script principal que carrega os dados e plota o gráfico.
- `dados.txt`: arquivo de exemplo com duas colunas (comprimento em mm e H).
- `requirements.txt`: lista de dependências do projeto.
- `README.md`: este arquivo.

## Pré-requisitos

- Python 3.x
- `pip`

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Navegue até o diretório do projeto.
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Coloque seu arquivo de dados (`dados.txt`) no mesmo diretório do script.
2. Execute o script:
   ```bash
   python plot_h_from_file.py
   ```
3. Um gráfico com **H vs Comprimento (mm)** será exibido em uma janela.

## Estrutura de Dados

O arquivo de dados deve ter duas colunas separadas por espaço ou tabulação:

```
<comprimento_mm> <valor_H>
```

Exemplo de `dados.txt`:
```
0.0 -141143.75
0.0602 -70384.1281
...
3.7333 -485842.019
```

## Personalização

- Para alterar o estilo do gráfico, edite o código em `plot_h_from_file.py` e ajuste parâmetros de Matplotlib.
- Você pode salvar o gráfico em arquivo adicionando por exemplo:
  ```python
  plt.savefig('grafico.png', dpi=300)
  ```

## Licença

Este projeto está sob a licença MIT. 

## Autor

Bruno Ribeiro Chaves
