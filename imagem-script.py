from js import document
import pandas as pd

# Dados
data = {
    "Ano": ["2023", "2023", "2024", "2024"],
    "Fruta": ["Pera", "Maca", "Pera", "Maca"],
    "Quantidade": [10, 20, 30, 20]
}

# Criar DataFrame
df = pd.DataFrame(data)
ano_selecionado = document.getElementById("ano-dropdown").value
df_filtrado = df[df["Ano"] == ano_selecionado]



# Escolher a imagem
# try:
fruta_favorita = df_filtrado.loc[df_filtrado["Quantidade"].idxmax(), "Fruta"]
imagem_fruta = f'<img src="{fruta_favorita.lower()}.png" style="width:100px;">'
# except:
    # Exibe o ano selecionado e o resultado do máximo
print(f"Ano selecionado: {ano_selecionado}")
print(f"Fruta favorita: {df_filtrado}")

