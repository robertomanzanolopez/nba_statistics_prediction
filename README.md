# NBA STATISTICS ANALISIS AND PREDICTOR

El objectivo de este trabajo es realizar un análisis de las principales estadísticas que se generan durante los partidos de baloncesto en la NBA (National Basketball Asociation). Se pretende además generar un modelo predictivo que prediga para un partido que equipo ganará basandose en las estadísticas de los partidos jugados anteriormente.


#### ÍNDICE:


1. Origen de los datos.


2. Herramientas utilizadas.
 
 
3. Distribución del repositorio.
 
 
4. Orden de ejecución de los notebooks.


    
#### 1. Origen de los datos:
Para llevar acabo el trabajo los datos han sido obtenidos de un repositorio en kaggle (https://www.kaggle.com/nathanlauga/nba-games/version/8?select=games.csv), obtenidos previamente de la API que proporciona la propia NBA.
    
#### 2. Herramientas utilizadas:
- Jupyter notebooks: 

Aqui se realiza la mayor parte del trabajo por la comodidad de su uso. En ellos se realiza la limpieza de los datos, se añaden datos adicionales, se exploran en su totalidad y se crea un modelo.
    
    
- Tableau: 

Ha sido el medio escogido para la visualización de los datos.

#### 3. Distribución del repositorio:
3.1 Data: Aqui estan los archivos .csv que se han usado, y los que se han generado posteriomente.
    
3.2 Notebooks:

- data_clean.ipynb:

  - Carga de los datos por primera vez (previamente descargados del origen de los datos).
 
  - Modificación de algun tipo de dato.
 
  - Comprobación de valores no válidos (Nans y huecos en blanco).
 
  - Limpieza de filas con valores no válidos.
 
  - Comprobación de la cantidad de partidos para cada temporada.
 
  - División del dataframe para tener solo los partidos correspondiente a la temporada regular.
 
  - Dataframe generado: df_all_rs.csv
 
 
- modifing_dataframe1.ipynb: 

  - Carga de dataframe con los nombres, nicnames e ids de todos los equipos (30).
 
  - Dataframe: df_teams
 
  - Merge del dataframe generado anteriomente (df_all_rs) y el nuevo (df_teams) para tener el nombre y nickname de los equipos.
 
  - Eliminado, renombrado y reordenado de columnas del dataframe.
 
  - Se añade nueva columna VISITOR TEAM WINS que indica si el partido lo gana el equipo que juega como visitante.
 
  - Dataframe generado: df_merged_renamed_droped_sorted_2_rs.csv
 
 
- create_data.py:Modulo con las funciones que se utilizan para generar nuevos datos a partir del dataframe anterior. Funciones:
  - home_visitor_df: Para un game id dado devuelve, el equipo de casa, el visitante y un dataframe auxiliar con todos los datos de la temporada correspondiente a dicho equipo.
 
  - porcentaje_victorias_home_team: Calcula el porcentaje de victorias que lleva en toda la temporada hasta ese partido para el equipo que juega en casa.
 
  - porcentaje_victorias_visitor_team: Calcula el porcentaje de victorias que lleva en toda la temporada hasta ese partido para el equipo que juega como visitante.
 
  - porcentaje_victorias_last5_home_team: Calcula el porcentaje de victorias que lleva en los últimos 5 partidos jugados para el equipo que juega en casa.
 
  - porcentaje_victorias_last5_visitor_team: Calcula el porcentaje de victorias que lleva en los últimos 5 partidos jugados para el equipo que juega como visitante.
 
  - porcentaje_victorias_last10_home_team: Calcula el porcentaje de victorias que lleva en los últimos 10 partidos jugados para el equipo que juega en casa.
 
  - porcentaje_victorias_last10_visitor_team: Calcula el porcentaje de victorias que lleva en los últimos 10 partidos jugados para el equipo que juega como visitante.
 
  - avg_points_home_team: Calcula la media de puntos que lleva en toda la temporada hasta ese partido para el equipo que juega en casa.
 
  - avg_points_visitor_team: Calcula la media de puntos que lleva en toda la temporada hasta ese partido para el equipo que juega como visitante.
 
  - avg_points_last5_home_team: Calcula la media de puntos que lleva en los últimos 5 partidos para el equipo que juega en casa.
 
  - avg_points_last5_visitor_team: Calcula la media de puntos que lleva en los últimos 5 partidos para el equipo que juega como visitante.
 
  - avg_points_last10_home_team: Calcula la media de puntos que lleva en los últimos 10 partidos para el equipo que juega en casa.
 
  - avg_points_last10_visitor_team: Calcula la media de puntos que lleva en los últimos 10 partidos para el equipo que juega como visitante.
 
  - avg_fg_home_team: Calcula la media de del porcentaje de acierto en tiros de campo que lleva en toda la temporada hasta ese partido para el equipo que juega en casa.
 
  - avg_fg_visitor_team: Calcula la media de del porcentaje de acierto en tiros de campo que lleva en toda la temporada hasta ese partido para el equipo que juega como visitante.
 
  - avg_fg_last5_home_team: Calcula la media de del porcentaje de acierto en tiros de campo de los últimos 5 partidos para el equipo que juega en casa.
 
  - avg_fg_last5_visitor_team: Calcula la media de del porcentaje de acierto en tiros de campo de los últimos 5 partidos para el equipo que juega como visitante.
 
  - avg_fg_last10_home_team: Calcula la media de del porcentaje de acierto en tiros de campo de los últimos 10 partidos para el equipo que juega en casa.
 
  - avg_fg_last10_visitor_team: Calcula la media de del porcentaje de acierto en tiros de campo de los últimos 10 partidos para el equipo que juega como visitante.
 
  - avg_fg3_home_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos que lleva en toda la temporada hasta ese partido para el equipo que juega en casa.
 
  - avg_fg3_visitor_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos que lleva en toda la temporada hasta ese partido para el equipo que juega como visitante.
 
  - avg_fg3_last5_home_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos de los últimos 5 partidos para el equipo que juega en casa.
 
  - avg_fg3_last5_visitor_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos de los últimos 5 partidos para el equipo que juega como visitante.
 
  - avg_fg3_last10_home_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos de los últimos 10 partidos para el equipo que juega en casa.
 
  - avg_fg3_last10_visitor_team: Calcula la media de del porcentaje de acierto en tiros de tres puntos de los últimos 10 partidos para el equipo que juega como visitante.


- modifing_dataframe2.ipynb: 

  - Creación nuevas columnas:
  
    - PERCENT_VIC_UNITL_THIS_GAME_HOME_TEAM
   
    - PERCENT_VIC_UNITL_THIS_GAME_VISITOR_TEAM
   
    - PERCENT_VIC_LAST5_GAMES_HOME_TEAM
   
    - PERCENT_VIC_LAST5_GAMES_VISITOR_TEAM
   
    - PERCENT_VIC_LAST10_GAMES_HOME_TEAM
   
    - PERCENT_VIC_LAST10_GAMES_VISITOR_TEAM
   
    - AVG_POINTS_UNTIL_THIS_GAME_HOME_TEAM
   
    - AVG_POINTS_UNTIL_THIS_GAME_VISITOR_TEAM
   
    - AVG_POINTS_LAST5_HOME_TEAM
   
    - AVG_POINTS_LAST5_VISITOR_TEAM
   
    - AVG_POINTS_LAST10_HOME_TEAM
   
    - AVG_POINTS_LAST10_VISITOR_TEAM
   
    - AVG_FGPERCENT_UNTIL_THIS_GAME_HOME_TEAM
   
    - AVG_FGPERCENT_UNTIL_THIS_GAME_VISITOR_TEAM
   
    - AVG_FGPERCENT_LAST5_HOME_TEAM
   
    - AVG_FGPERCENT_LAST5_VISITOR_TEAM
   
    - AVG_FGPERCENT_LAST10_HOME_TEAM
   
    - AVG_FGPERCENT_LAST10_VISITOR_TEAM
   
    - AVG_FG3PCT_UNTIL_THIS_GAME_HOME_TEAM
   
    - AVG_FG3PCT_UNTIL_THIS_GAME_VISITOR_TEAM
   
    - AVG_FG3PCT_LAST5_HOME_TEAM
   
    - AVG_FG3PCT_LAST5_VISITOR_TEAM
   
    - AVG_FG3PCT_LAST10_HOME_TEAM
   
    - AVG_FG3PCT_LAST10_VISITOR_TEAM
   
 - Generación de tantas listas como columnas nuevas tenemos con la funciones creadas anteriormente y un map.
 
 - Inserción de los nuevos datos en las correspondientes columnas.
 
 - Se reordenan una última vez las columnas.
 
 - Dataframe generado: df_complete.csv


- data_explorarion: Exploración de los datos y selección de variables. A traves de distintas gráficas y tablas obtenemos la conclusion de que variables pueden ser mas significativas para el objetivo.

 - Exploración de la matriz de correlación.
 
 - Gráficos que muestran la evolución a lo largo de los últimos años de las siguientes estadísticas:
 
   - Puntos anotados por el equipo de casa, el equipo que juega como visitante y la media.
  
   - Asistencias repartidas por el equipo de casa, el equipo que juega como visitante y la media.
  
   - Rebotes cogidos por el equipo de casa, el equipo que juega como visitante y la media.
  
   - Porcentaje de acierto en tiros de 2 del equipo de casa, del equipo que juega como visitante y la media.
  
   - Porcentaje de acierto en tiros de 3 del equipo de casa, del equipo que juega como visitante y la media.
  
   - Porcentaje de acierto en tiros libres del equipo de casa, del equipo que juega como visitante y la media.
   
 - Exploración mas detallada de las columnas con mayor correlación:
 
   - Correlación entre puntos y victorias
   
   - Correlación entre asistencias y victorias
   
   - Correlación entre asistencias y puntos
   
   - Correlación entre rebotes y victorias
   
   - Correlación entre %fg y victorias
   
   - Correlación entre %fg y puntos
   
   - Correlación entre %fg3 y victorias
   
   - Correlación entre %fg3 y puntos

 - Conclusiones
 

- model_creation: En este notebook se aplican varias técnicas para la selección de los mejores hiperparámetros de los distintos algoritmos que se usan para el modelo final. 

 - Los algoritmos utilizados son: 

   - Gaussian Naive Bayes
 
   - Regresión Logística
 
   - SVC
 
   - Decission Tree Classifier
 
   - Random Forest Classifier 

 - Para la selección de hiperparametros se ha optado por:

   - GridSearchCV
   
   - RandomSearchCV
   
   - 

 - Modelo generado: modelo_final.pkl
 


#### 4. Orden de ejecución de los notebooks:
Los notebooks deben ejecutarse por completo y en un orden específico:
 1. data_clean.ipynb


 2. data_modifing1.ipynb


 3. data_modifing2.ipynb


 4. data_exploration.ipynb


 5. model_creation.ipynb