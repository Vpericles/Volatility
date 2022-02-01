READ ME
__________________________
VOL
Vitor Péricles de Carvalho
vitor@laic.com.br
__________________________

Propósito:
- Código simples para cálculo de volatilidade realizada, de uma série história de preços.

Inputs:
- Arquivo .XLS com nome da série e série histórica de preços;

Outputs:
- calcula a volatilidade, apresentada resultado em texto e em gráfico (matplotlib.pyplot)
- salva arquivo .XLS com evolução da série histórica de volatilidade;

Bibliotecas utilizadas:
- xlrd (lê arquivo de Excel);
- matplotlib (pyplot, para plotar gráficos);
- xlsxwriter (grava arquivo de Excel);
- numpy;
- math;
- statistics (para cálculo de desvio padrão);

__________________________

O código está programado para cálculo de vol anualizada de janela móvel de 90 dias, que é
a forma usual para comparação e referência do Mercado Financeiro, muito comum para análise
de volatilidade de Fundos de Investimento, por exemplo.
A base de dados é o arquivo em .XLS que o código lê (especificado na linha 10).
A base de exemplo contém .XLS de IBOVESPA, em base diária. O cálculo pode ser feito para
qualquer base de tempo na série de dados, uma vez que a fonte dos dados é o arquivo de Excel.
Após o cálculo, arquivo .XLS com a evolução da série histórica de vol é gerado e salvo.
A periodicidade da janela móvel pode ser alterada nas linhas 33, 43 (acrescentando 1) e 44.
(no código, linha 33 = 90, linha 43 = 91 e linha 44 = 90).


