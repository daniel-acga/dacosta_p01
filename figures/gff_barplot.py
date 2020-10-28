#!/home/dacosta/anaconda3/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Crea el dataset con << tus datos obtenidos en barplot_data.txt >>
frecuencias = [11, 13, 1, 1, 1, 5, 17]
categorias = ['gene', 'CDS', 'region', "three_prime_UTR", "five_prime_UTR", "stem_loop", "mature_protein_region_of_CDS"]
categorias = [ '\n'.join(wrap(l, 11)) for l in categorias]

y_pos = np.arange(len(categorias))

# Gráfico de barras
plt.bar(y_pos, frecuencias)

# Nombres en el eje-x
plt.xticks(y_pos, categorias)

# Mostrar la gráfica
plt.show()
