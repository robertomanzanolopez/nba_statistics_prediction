# nba_statistics_prediction

Este trabajo es un análisis de las principales estadísticas que se generan durante los partidos de baloncesto en la NBA (National Basketball Asociation) y la generación de un modelo que intente predecir las mismas con el principal objetivo de saber qué equipo ganará el partido.

El trabajo se ha realizado en notebooks de jupyter:
 
 1) data_clean: Aqui se cargan los datos por primera vez y se limpian para su posterior tratamiento.
 2) modifing_dataframe: Se añaden nuevas columnas generadas apartir de los datos limpios al dataframe con el objetivo de añadir nuevas variables que mejoren el modelo.
 3) data_explorarion: Exploración de los datos y selección de variables. A traves de distintas gráficas y tablas obtenemos la conclusion de que variables pueden ser mas significativas para el objetivo.
 4) model_creation: En este notebook se aplican varias técnicas para la selección de los mejores hiperparámetros de los distintos algoritmos que se usan para el modelo final.
 5) ---------------: Aplicación del modelo.