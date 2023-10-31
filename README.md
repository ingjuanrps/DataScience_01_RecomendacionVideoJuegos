# PI_01_Juan Ramón Perales Sosa.

# Machine Lerning Operations (MLOps).

![mlOper](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/09732ddc-dc41-42b6-9b51-be423dafca18)


## ¡Bienvenidos al primer proyecto individual de la etapa de labs! Se deberán hacer un trabajo situándose en el rol de un MLOps Engineer.
  * Se trabajo en Visual Studio Code, en estructuras de Paquetes, Modulos, Carpetas, Sub-carpetas y Archivos .py, .ipynb, .txt, .gitignore.
  * Framework FastAPI
  * Deployment

![Captura de pantalla (2)](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/3c41da8d-1a31-4659-87cd-a5751289f759)


# Funcion Desanidar.

![funcion](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/104226aa-fc75-43d4-a61d-f9a86a6d25c2)

# ETL.
  * Extracción, transformación y carga (ETL) es el proceso consistente en combinar datos de diferentes orígenes un gran repositorio central llamado almacenamiento de datos.

![ETL](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/6a66b300-f4e2-4ba5-ae66-e2b927b08363)

## Pasos que se realizarón.
### Importación de librerías.
### Guardando el DataFrame creado en un archivo .parquet para que pese menos.
### Creando un DataFrame con el arcchivo .parquet.
### En un archivo funciones.py se creo función para desanidar.
### Creando un DataFrame con el arcchivo .parquet.
### Guardando el DataFrame creado en un archivo .parquet para que pese menos.
### Creando un DataFrame con el arcchivo .parquet.
### Creando un nuevo DataFrame instanciando el DataFrame anterior (reviews)
  * Usando .explode()
    * El método **.explode()**, es una función de pandas en Python que se utiliza para descomponer una lista o una serie de listas en varias filas, repitiendo los valores en las otras columnas según corresponda. Esto es útil cuando se tiene datos anidados y deseas "desplegar" o "explorar" esos datos en un DataFrame más plano.
### Observamos como se comporta **.explode().**
### Concatenamos el DataFrame original 'reviews', con el nuevo DataFrame 'reviews_comenExpan'.
  * Despues eliminamos la columna 'reviews', del DataFrame Concatenado.
### Eliminamos la columna que esta vacia.
### Rellenamos valores faltantes o valores en NaN con **.fillna()**
### Revisando valores duplicados.
### Eliminando valores duplicados.
### Eliminando columnas inecesarias.
  * 'user_url','funny','last_edited','helpful'
### Guardando el dataframe en un archivo csv.
### Liberando memoria.

# Funciones.
### 00- Index.
  * 'Proyecto Invidual 01, Juan Ramón Perales Sosa.'

![f00](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/0173c036-f4ad-429f-8504-078edd52011a)


### 01- Función. def developer( desarrollador : str ):
  * Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. 
    Ejemplo de retorno:
    Año	Cantidad de Items	Contenido Free
    2023	50	27%
    2022	45	25%
    xxxx	xx	xx%

![f01](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/c7b0e8cb-48e4-4752-a36f-f40c92ba1590)


### 02- Función. def userdata( User_id : str ):
  * Debe devolver cantidad de dinero gastado por el usuario, 
    el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
    Ejemplo de retorno: 
    {"Usuario X" : us213ndjss09sdf, "Dinero gastado": 200 USD, "% de recomendación": 20%, "cantidad de items": 5}

![f02](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/333b012c-944e-4fd6-bba2-f5f674ad04a0)


### 03- Funcion. def UserForGenre( genero : str ): 
  * Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación
    de horas jugadas por año de lanzamiento.
    Ejemplo de retorno: 
    {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,"Horas jugadas":[{Año: 2013, Horas: 203}, 
    {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

![f03](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/bd48b187-cda8-4264-aba8-cbd34647939e)


### 04- Función. def best_developer_year( año : int ): 
  * Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. 
    (reviews.recommend = True y comentarios positivos)
    Ejemplo de retorno: 
    [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

![f04](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/96a4afb4-7f72-4ed1-8a65-07e7285bc88e)


### 05- función. def developer_reviews_analysis( desarrolladora : str ): 
  * Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave 
    y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento 
    como valor positivo o negativo.
    Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}

![f05](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/1bc751dc-cc85-4b7a-b62d-3e10759d403c)


# EDA.
## Pasos que se realizarón.
### Importación de Librerías.
### Extrayendo y creando mi DataFrame.
### Información del DataFrame, para ver si el archivo ya no contiene valores nulos.
### Grafíco missingno, para valores Nulos.
### Distribución de registros por recommend.
### Distribución de registros Sentiment_Analysis.
### Distribución de registros por Posteos.
### Análisis Sentimiento por año.

![sentimientos_porAño](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/bfe8a905-98a0-46f8-82f7-bdfca03a42af)

# Machine Lerning.
## Pasos que se realizaron.
### Importando Librerias.
### Cargando DataFrame.
### Filtrando DataFrame.
### Instanciando Modelo.
### Entrenando Modelo.

![modelo](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/0143a5cd-ddaa-4ef6-af7c-d0a559f0e0e6)

### Similitud Coseno.
### Función Recomendación_juego.

![funcionMachineLerning](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/c122c9b9-1b4c-44e6-9bd7-27bd57a61ba4)


![f06](https://github.com/ingjuanrps/PI_01_JRPS/assets/114045466/9542bfe6-620d-4be1-acf6-a6aa4666e319)


Contato: https://github.com/ingjuanrps 




