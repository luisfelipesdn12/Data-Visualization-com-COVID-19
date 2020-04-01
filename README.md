# Data-Visualization-com-COVID-19
> Análise e visualização de dados com Python a partir de dados sobre o COVID-19 - Data analysis and visualization with Python from data about COVID-19
---

## Introdução:
Estou estudando Data Science com a linguagem de programação Python. A fim de praticar, resolvi usar dados reais sobre a pandemia de _SARS-CoV-2_, tanto do Brasil, quanto do resto do mundo.
Os dados estão sendo obtidos em sua maioria por meio de um site chamado [Kaggle](https://www.kaggle.com/), ele é uma espécie de rede social de Data Scientists, onde são compartilhados inúmeros datasets, notebooks, e até mesmo competições, onde varias pessoas se reúnem a partir de dados e artigos para construir análises e construir conhecimento.
![img](https://i.imgur.com/NtbYcIs.png)
> _[Kaggle](https://www.kaggle.com/): Your Home for Data Science_

A partir [desses dados](./datasets), utilizei a linguagem Python juntamente com duas bibliotecas:

1. [**Pandas**](https://pandas.pydata.org/) - a utilizei para analisar os dados, sobretudo extrair colunas específicas dos `datasets.csv`;

2. [**Matplotlib**](https://matplotlib.org/) - fiz uso dessa biblioteca para a visualização dos dados, plotar gráficos de linha, diagramas de caixa, legendas etc.

-----
## Gráficos:
### Comparação da idade média entre casos totais e com óbito
O primeiro gráfico que eu plotei nesse projeto foi esse:
![BOXPLOT-Comparacao-de-idade-entre-casos-totais-e-casos-de-obito-em-pacientes-com-COVID-19](https://raw.githubusercontent.com/luisfelipesdn12/Data-Visualization-com-COVID-19/master/img/BOXPLOT-Comparacao-de-idade-entre-casos-totais-e-casos-de-obito-em-pacientes-com-COVID-19.png)
> Fonte:
> - Dado usado: [./datasets/COVID19_line_list_data.csv](./datasets/COVID19_line_list_data.csv)
> - Atualização mais recente: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset#COVID19_line_list_data.csv

Ele mostra a amplitude e a média da idade dos pacientes em casos reportados no total, e na parcela de óbitos.   
Escolhi utilizar o diagrama de caixa - *aka.: boxplot* - pois nele é possível visualizar, além da mediana, onde estão concentrados a maioria dos dados, a amplitude geral deles, os valores mínimos e máximos e valores discrepantes e isolados.

#### Elementos de um boxplot:
![Elementos de um boxplot](https://upload.wikimedia.org/wikipedia/commons/c/c9/Elements_of_a_boxplot_pt.svg)
