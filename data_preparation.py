#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
# %%
#open data
dataku = pd.read_csv('videgames.csv')
# %%
#cek data kosong
dataku.isna().sum()

#%%
#rubah tipe data string to float

dataku['Precio'] = dataku['Precio'].apply(lambda x: float(x.split()[0].replace(',','')))
# %%
#modus pada kolom-kolom data kosong
mode_pabrik = dataku["Fabricante"].mode()[0]
mode_konsol = dataku["Consola"].mode()[0]
mode_genre = dataku["Género"].mode()[0]
mode_title = dataku["Título"].mode()[0]
# %%
#isi data kosong dengan modus
dataku["Género"] = dataku["Género"].fillna(mode_genre)
dataku["Fabricante"] = dataku["Fabricante"].fillna(mode_pabrik)
dataku["Consola"] = dataku["Consola"].fillna(mode_konsol)
dataku["Título"] = dataku["Título"].fillna(mode_title)


# %%
#cek data kosong
dataku.isna().sum()

# %%
data_genre_harga = dataku[["Género","Precio"]].groupby("Género").mean()
data_pabrik_harga = dataku[["Fabricante","Precio"]].groupby(["Fabricante"]).mean()
data_konsol_harga = dataku[["Consola","Precio"]].groupby(["Consola"]).mean()
data_title_harga = dataku[["Título","Precio"]].groupby(["Título"]).mean()
# %%
#Plot genre 
plt.bar(data_genre_harga.index,data_genre_harga["Precio"])
plt.xticks(rotation=90)
plt.title("Perbandingan rata-rata Harga dengan Genre")
plt.xlabel("Genre")
plt.ylabel("Harga")
plt.show()


# %%
#Plot Konsol
plt.bar(data_konsol_harga.index,data_konsol_harga["Precio"])
plt.xticks(rotation=90)
plt.title("Perbandingan rata-rata harga dengan konsol")
plt.xlabel("Konsol")
plt.ylabel("Harga")
plt.show()

# %%
