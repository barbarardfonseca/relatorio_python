import pandas as pd
import io
import requests
from pyscript import display

# Processar os dados
url = "https://raw.githubusercontent.com/barbarardfonseca/barbarardfonseca.github.io/master/testesPy/MissaoZero_BaseDados.xlsx"
response = requests.get(url)
response.raise_for_status()
excel_data = pd.ExcelFile(io.BytesIO(response.content), engine="openpyxl")

all_data = pd.DataFrame()
for sheet in excel_data.sheet_names:
    sheet_data = pd.read_excel(excel_data, sheet_name=sheet)
    sheet_data['Month'] = sheet
    all_data = pd.concat([all_data, sheet_data], ignore_index=True)

# Enviar os dados para o HTML (armazenar no placeholder como JSON)
all_data['TotalSaleValue'] = all_data['OrderQuantity'] * all_data['UnitPrice']
all_data_json = all_data.to_json(orient="records")

display(all_data_json, target="data_placeholder")
