import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import editor as ed

# Abrir el archivo con los datos originales
df = pd.read_csv("Raw_data.csv")

# Instanciar el programa para editar espectros
esp_ed = ed.Editar_espectro(df)

# Obtener un corte entre 2 longitudes de onda
esp_ed.get_cut((2517, 3000))

# Imprimir el estado del DF
print(esp_ed.data_frame)

# Guardar el DF como CSV
esp_ed.save_csv("Espectro_recortado.csv")


