import pandas as pd
import matplotlib.pyplot as plt
from js import document
from pyscript import display

# Carregar os dados do HTML
data_placeholder = document.querySelector("#data_placeholder").innerText
all_data = pd.read_json(data_placeholder)

# Processar os dados
# all_data = all_data[['BusinessType', 'OrderQuantity', 'UnitPrice']]
# all_data['TotalSaleValue'] = all_data['OrderQuantity'] * all_data['UnitPrice']
BusinessTypeSales = all_data.groupby(['BusinessType'])['TotalSaleValue'].sum().reset_index()

# Gerar o gráfico
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(BusinessTypeSales["BusinessType"], BusinessTypeSales["TotalSaleValue"], color="skyblue")
ax.set_title("Total Sale Value by Business Type")

# Exibir o gráfico no HTML
display(fig, target="graphic2")