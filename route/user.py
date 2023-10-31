import pandas as pd
import numpy as np
from fastapi import APIRouter


user = APIRouter()

# DataFrame para las 5 primeras funciones.
df_merge = pd.DataFrame(pd.read_parquet(
    r'C:\Users\ingju\Desktop\jrPI_1\data\04gamesMerge\02gamesmerge.parquet'))
# DataFrame para funciones de Machine Lerning.

similitudCoseno = np.loadtxt(
    r'C:\Users\ingju\Desktop\jrPI_1\data\05_ML\redu_osg_mr_sim_cos.txt')
indice = pd.DataFrame(pd.read_csv(
    r'C:\Users\ingju\Desktop\jrPI_1\data\05_ML\redu_osg_mr_indice.csv'))
df_BD = pd.DataFrame(pd.read_csv(
    r'C:\Users\ingju\Desktop\jrPI_1\data\05_ML\redu_osg_mr.csv'))


@user.get('/')
def index():
    return 'Proyecto Invidual 01, Juan Ramón Perales Sosa.'


''' def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. 
Ejemplo de retorno:
Año	Cantidad de Items	Contenido Free
2023	50	27%
2022	45	25%
xxxx	xx	xx%
'''


@user.get('/user1/{desarrolladora}')
def developer(desarrolladora):
    resultado = ''
    años = df_merge[df_merge['developer'] ==
                    desarrolladora]['anio_lanzamiento']
    years = []
    for año in años:
        if año not in years:
            years.append(año)
    if len(years) == 0:
        return print('No posee juegos')
    years.sort()
    for año in years:
        cantidad = df_merge[(df_merge['developer'] == desarrolladora) & (
            df_merge['anio_lanzamiento'] == año)].shape[0]
        free = df_merge[(df_merge['developer'] == desarrolladora) & (
            df_merge['price'] == 0) & (df_merge['anio_lanzamiento'] == año)].shape[0]
        porciento = round((free/cantidad)*100, 2)
        try:
            resultado = {
                f"En el año {año} la desarrolladora: {desarrolladora} posee {cantidad} de juegos y {porciento}% son free"}
        except:
            resultado = {f'No se encontro desarrolladora'}
    return resultado


azar = df_merge['developer'].sample().values[0]
developer(azar)


'''def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, 
   el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
Ejemplo de retorno: 
{"Usuario X" : us213ndjss09sdf, "Dinero gastado": 200 USD, "% de recomendación": 20%, "cantidad de items": 5}
'''


@user.get('/user2/{user_id}')
def userdata(user_id):
    ids = list(df_merge[df_merge['user_id'] == user_id]['item_id'])

    if len(ids) == 0:
        return print('No se encontro Id')
    gastado = 0
    for id in ids:
        try:
            gastado += df_merge[df_merge['item_id']
                                == int(id)]['price'].values[0]
        except:
            continue
        gastado = round(gastado, 2)
        porcentaje = (df_merge[df_merge['user_id'] == user_id]['recommend'].sum(
        )/len(df_merge[df_merge['user_id'] == user_id]))*100
        cantidadItems = (df_merge[df_merge['user_id']
                                  == user_id]['items_count'].values[0])
        resultado = {
            f"Usuario: {user_id} tiene Dinero gastado: ${gastado} USD, el % de recomendación: {porcentaje}% y la Cantidad items es: {cantidadItems}"}
    return resultado


azar1 = df_merge['user_id'].sample().values[0]
userdata(azar1)

'''def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación
    de horas jugadas por año de lanzamiento.
Ejemplo de retorno: 
{"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,"Horas jugadas":[{Año: 2013, Horas: 203}, 
 {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
'''


@user.get('/user3/{genero}')
def UserForGenre(genero):
    filtro = df_merge['genres'].apply(
        lambda x: True if genero.strip().lower() in list(str(x).split(",")) else False)
    resultado = df_merge[filtro]
    if resultado.empty:
        retorno = {"Error": f"No se encontro género {genero.title()} "}
    else:
        usuario = df_merge.groupby(['user_id']).sum()[['playtime_forever']].reset_index(
        ).sort_values(by='playtime_forever', ascending=False).iloc[0]['user_id']
        filtro = (df_merge['genres'].apply(lambda x: True if genero.strip().lower() in list(
            str(x).split(",")) else False)) & (df_merge['user_id'].str == str(usuario))
        resultado2 = df_merge[filtro].groupby(['anio_lanzamiento']).sum()[['playtime_forever']].reset_index(
        ).sort_values(by='playtime_forever', ascending=False).reset_index()
        vector = [{"Año": str(int(resultado.iloc[i]['anio_lanzamiento'])), 'Horas':format(int(
            resultado.iloc[i]['playtime_forever']), ',d').replace(",", ".")} for i in range(0, len(resultado2.index)+1)]
        retorno = {f'Usuario con más horas jugadas para el género {genero.title()}': usuario,
                   'Horas jugadas por año de lanzamiento de los juegos': vector}
    return retorno


UserForGenre('RPG')

'''def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. 
(reviews.recommend = True y comentarios positivos)
Ejemplo de retorno: 
[{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
'''


@user.get('/user4/{anio}')
def best_developer_year(anio):
    filtro = ((df_merge['posted'] == anio) & (df_merge['recommend'] == True) & (
        df_merge['sentiment_analysis'] == 1) | (df_merge['sentiment_analysis'] == 2))
    resultado = df_merge[filtro].groupby(['item_id', 'title']).count()[['recommend']].reset_index(
    ).sort_values('recommend', ascending=False).reset_index().drop('index', axis=1)
    if resultado.empty:
        retorno = {'Error': f'No hay datos para el año seleccionado {anio}'}
    else:
        retorno = {f'los tres juegos más recomendados para el año {anio}': [{f'Puesto {i+1}': {'Identificador del juego': str(
            resultado['item_id'][i]), 'Titulo':resultado['title'][i]}}for i in range(min(3, len(resultado.index)))]}
    return retorno


'''def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, 
se devuelve un diccionario con el nombre del desarrollador como llave 
y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento 
como valor positivo o negativo.
Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}
'''


@user.get('/user5/{desarrolladora}')
def developer_reviews_analysis(desarrolladora):
    filtro = (df_merge['developer'] == desarrolladora)
    resultado = df_merge[filtro].groupby(['sentiment_analysis']).count()[
        'item_id'].reset_index().set_index('sentiment_analysis')
    if resultado.empty:
        retorno = {'Error': f'No se encontro desarrolladora'}
    else:
        negativos = resultado.loc[0]['item_id']if 0 in resultado.index else 0
        neutros = resultado.loc[1]['item_id']if 1 in resultado.index else 0
        positivos = resultado.loc[2]['item_id']if 2 in resultado.index else 0
        retorno = {f'{desarrolladora}':
                   f'Negativos: {negativos}, Neutrales: {neutros}, Positivos: {positivos}'}
    return retorno


# Machine Lerning
# Si es un sistema de recomendación item-item:
'''def recomendacion_juego( id de producto ): 
Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
'''


@user.get('/user6/{id_producto}')
def recomendacion_juego(id_producto):
    if (indice[indice['item_id'] == id_producto].empty):
        retorno = {'Error': f'No se encuentra ID {id_producto}.'}

    else:
        idx = indice[indice['item_id'] == id_producto]['0'].values[0]
        puntajes_similares = list(enumerate(similitudCoseno[idx]))
        puntajes_similares = sorted(
            puntajes_similares, key=lambda x: x[1], reverse=True)
        puntajes_similares = puntajes_similares[1:6]
        juegos_indices = [int(i[0]) for i in puntajes_similares]
        titulo = df_BD[df_BD['item_id'] == id_producto]['title'].values
        retorno = {f'Recomendación de 5 juegos relacionados con ({id_producto}) {titulo}': [{f'Recomendación {i+1}': {
            'Identificador': df_BD['item_id'].iloc[juegos_indices[i]], 'Titulo':df_BD['title'].iloc[juegos_indices[i]]}} for i in range(len(juegos_indices))]}
    return retorno


# Si es un sistema de recomendación user-item:
'''def recomendacion_usuario( id de usuario ): 
Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.
'''
