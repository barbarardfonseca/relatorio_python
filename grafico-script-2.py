import pandas as pd
import io
import requests
# from js import document
from pyscript import display
import matplotlib.pyplot as plt


# def load_file(event):
# URL do arquivo Excel na nuvem
url = "https://raw.githubusercontent.com/barbarardfonseca/barbarardfonseca.github.io/master/testesPy/MissaoZero_BaseDados.xlsx"
# Criar um DataFrame vazio para armazenar todos os dados
all_data = pd.DataFrame()
try:
    # Fazer o download do arquivo
    response = requests.get(url)
    response.raise_for_status()
    
    # Abrir o arquivo Excel como um objeto de leitura
    excel_data = pd.ExcelFile(io.BytesIO(response.content), engine="openpyxl")
    sheet_data_test = pd.read_excel(excel_data, sheet_name='Jan')
    # print(0,sheet_data_test.head())
    # Iterar sobre todas as planilhas no arquivo
    for sheet in excel_data.sheet_names:
        # Ler cada planilha em um DataFrame
        sheet_data = pd.read_excel(excel_data, sheet_name=sheet)
        
        # Adicionar uma coluna para o nome da planilha
        sheet_data['Month'] = sheet
        
        # Concatenar os dados de cada planilha
        all_data = pd.concat([all_data, sheet_data], ignore_index=True)
        # return all_data
        
except Exception as e:
    'aaaa'
########## Parte 2 ##########
# all_data = all_data.iloc[:, [1, 9,10]]
all_data = all_data[['BusinessType', 'OrderQuantity','UnitPrice']]
all_data['TotalSaleValue'] = all_data['OrderQuantity'] * all_data['UnitPrice']
BusinessTypeSales = all_data.groupby(['BusinessType'])['TotalSaleValue'].sum().reset_index()
# print(1,BusinessTypeSales.head())
# BusinessTypeSales.columns = ['BusinessType', 'TotalSaleValue']
# # Configurar o gráfico de barras

fig1, ax1 = plt.subplots(figsize=(6, 4))  # Criar a figura e os eixos
ax1.bar(BusinessTypeSales["BusinessType"], BusinessTypeSales["TotalSaleValue"], color="skyblue")  # Adicionar o gráfico de barras
ax1.set_title("Total Sale Value by Business Type")  # Definir o título

display(fig1, target="graphic1")
##############################################################333
# fig2, ax2 = plt.subplots(figsize=(6, 4))  # Criar a figura e os eixos
# ax2.bar(df_filtrado["Fruta"], df_filtrado["Quantidade"], color="red")  # Adicionar o gráfico de barras
# ax2.set_title("Quantidade de Frutas por Ano")  # Definir o título
# ax2.set_xlabel("Fruta")  # Definir o rótulo do eixo X
# ax2.set_ylabel("Quantidade")  # Definir o rótulo do eixo Y

# display(fig2, target="mpl2")

