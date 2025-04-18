import pandas as pd #Usamos Pandas ya que son bases de datos no relacionadas y extraer datos 
import matplotlib.pyplot as plt # Graficos 
import seaborn as sns # Graficas con mayor apoyo visual y estadisticas

#Leemos el DataFrame Para esto se usa la ruta donde esta el archivo en tu caso cambia la ruta por donde este el archivo.csv
df = pd.read_csv("Crop_Recommendation.csv")


#Anlizamos como viene el DataFrame 
print("Primeras filas Data Frame")
print(df.head())

print("\n Resumen del dataset:")
#Miramos si hay datos Nulos y los tipos de datos de cada uno 
print(df.info())
# Estadísticas como promedio, desviación estándar, mínimos y máximos para cada columna numérica
print(df.describe())



print(df.groupby('Crop').describe())
#Ya es cuestion de los parametros que necesites (media, desviacion...etc) cambiar ".describe" por lo que se necesite
#Ejemplo : 
# print(df.groupby('Crop').std())

#Ahora queremos tener correlacion podriamos hacerlo con la correlacion de Pearson 
# 1 Relacion perfectamente positiva, 0 No hay correlacion lineal, -1 Relacion perfectamente negativa 
#Hay que tener en cuenta que la columna crop no es numerica asi que hay que tener un DataFrame que sea solo numerico
df_numerical = df.drop(columns=['Crop'])
print("\n Correlacion Entre Las Variables ")
print(df_numerical.corr())

#Ya teniendo los Datos vamos a obtener los graficos usando seaborn 

plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.regplot(x='Humidity', y='Temperature', data=df, scatter_kws={'s': 20, 'color': 'blue'}, line_kws={'color': 'red', 'lw': 2})


plt.title('Humedad vs Temperatura Y su linea de Tendencia', fontsize=16)
plt.xlabel('Humedad', fontsize=14)
plt.ylabel('Temperatura', fontsize=14)


plt.show()

#Repetimos el proceso pero para otro proposito en este caso humedad vs precipitación

plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.regplot(x='Humidity', y='Rainfall', data=df, scatter_kws={'s': 20, 'color': 'blue'}, line_kws={'color': 'red', 'lw': 2})


plt.title('Humedad vs Precipitación Y su linea de Tendencia', fontsize=16)
plt.xlabel('Humedad', fontsize=14)
plt.ylabel('Precipitación', fontsize=14)


plt.show()
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.regplot(x='Nitrogen', y='Rainfall', data=df, scatter_kws={'s': 20, 'color': 'blue'}, line_kws={'color': 'red', 'lw': 2})


plt.title('Nitrogeno Vs Precipitacion Y su linea de Tendencia', fontsize=16)
plt.xlabel('Nitrogeno', fontsize=14)
plt.ylabel('Precipitación', fontsize=14)


plt.show()



desviacion=df_numerical.std()

plt.figure(figsize=(10, 6))
desviacion.plot(kind='bar', color='cyan', edgecolor='pink')


plt.title('Desviacion de cada parámetro', fontsize=16)
plt.xlabel('Parámetros', fontsize=14)
plt.ylabel('Desviacion', fontsize=14)


plt.show()

#Un grafico de Torta para saber de todos los suelos cuales son Acidos, Neutro y Alcaninos 

def clasificar_ph(pH):
    if pH < 6.5:
        return 'Ácido'
    elif 6.5 <= pH <= 7.5:
        return 'Neutro'
    else:
        return 'Alcalino'

# Creamos una nueva columna
df['Tipo_pH'] = df['pH_Value'].apply(clasificar_ph)

# Contamos la frecuencia de cada tipo
ph_counts = df['Tipo_pH'].value_counts()

# Graficamos
plt.figure(figsize=(8, 8))
plt.pie(ph_counts, labels=ph_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución del tipo de pH en los suelos evaluados')
plt.axis('equal')
plt.show()

