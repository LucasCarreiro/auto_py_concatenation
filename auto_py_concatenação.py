#Seguinte, vc primeiro tem que importar essas bibliotecas. qualquer coisa pesquisa no google "Como importar uma biblioteca python"(pandas,numpy,matplotlib)#

import pandas as pd

#👇Aqui vc Coloca os arquivos que serão lidos👇#

arquivo_excel_1 = 'Aqui coloca o nome do arquivo junto com a extensão dele. Ex:Fulano1.xlsx'
arquivo_excel_2 = 'Aqui coloca o segundo arquivo .xlsx'

#Daqui em diante será a codificação para estruturar os arquivos#

# ❌ PRESTE BASTANTE ATENÇÃO E LEIA TODAS AS LINHAS ❌ #

df_dia_1 = pd.read_excel(arquivo_excel_1,sheet_name='Aqui vai o nome da planilha1 dentro do arquivo')
df_dia_2 = pd.read_excel(arquivo_excel_2,sheat_name='Aqui vai o nome da planilha2 dentro do segundo arquivo')

#Se por acaso o arquivo 1 ou o arquivo 2 tiver mais de uma planilha, duplica a linha e adiciona o nome da planilha, lembre-se de mudar o nome do termo antes do = seguindo o padrão - df_dia_X - #

#Aqui será adicionado um termo para inicar a junção das planilhas, mas especificamente uma concatenação dos arquivos#

#Dentro do parentese abaixo vc adiciona todos os df_dia da linha anterior#

df_todas_as_planilhas = pd.concat(df_dia_1,df_dia_2)

#Agora que temos todas as informações concatenadas, criaremos um arquivo excel com essas informações#

df_todas_as_planilhas.to_excel('O Nome do Aquivo Final.xlsx')

#Fim
