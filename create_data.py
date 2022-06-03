import pandas as pd
import numpy as np

# Funciones para la creacoin de los datos

def home_visitor_df(game_id):
    df = pd.read_csv('df_merged_renamed_droped_sorted_2_rs.csv')
    df = df.drop('Unnamed: 0', axis=1)
    
    home_team = int(df.query("GAME_ID == " + str(game_id))['HOME_TEAM_ID'])
    visitor_team = int(df.query("GAME_ID == " + str(game_id))['VISITOR_TEAM_ID'])
    season = int(df.query("GAME_ID == " + str(game_id))['SEASON'])
    df_aux = df[(df['SEASON'] == season)]    
    
    return home_team, visitor_team, df_aux


def porcentaje_victorias_home_team(game_id):
    #home_team = int(df_rs_03.query("GAME_ID == " + str(game_id))['HOME_TEAM_ID'])
    #visitor_team = int(df_rs_03.query("GAME_ID == " + str(game_id))['VISITOR_TEAM_ID'])
    #df_p_v_a = df_rs_03[(df_rs_03['GAME_ID'] <= game_id)]
                 
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    total_partidosH = int(len(df_p_v_a_home))
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    victorias_as_homeH = int(df_p_v_a_homeH[df_p_v_a_homeH['HOME_TEAM_WINS'] >= 1]['HOME_TEAM_WINS'].count())
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    victorias_as_visitorH = int(df_p_v_a_homeV[df_p_v_a_homeV['VISITOR_TEAM_WINS'] >= 1]['VISITOR_TEAM_WINS'].count())
    victorias_totalH = victorias_as_homeH + victorias_as_visitorH
    
    porcentaje_victorias_home_team = (victorias_totalH / total_partidosH) * 100
    
    return porcentaje_victorias_home_team


def porcentaje_victorias_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    total_partidosV = int(len(df_p_v_a_visitor))
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    victorias_as_homeV = int(df_p_v_a_visitorH[df_p_v_a_visitorH['HOME_TEAM_WINS'] >= 1]['HOME_TEAM_WINS'].count())
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    victorias_as_visitorV = int(df_p_v_a_visitorV[df_p_v_a_visitorV['VISITOR_TEAM_WINS'] >= 1]['VISITOR_TEAM_WINS'].count())
    victorias_totalV = victorias_as_homeV + victorias_as_visitorV
    
    porcentaje_victorias_visitor_team = (victorias_totalV / total_partidosV) * 100    

    return porcentaje_victorias_visitor_team


def porcentaje_victorias_last5_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last5 = df_p_v_a_homeH.tail(5)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last5 = df_p_v_a_homeV.tail(5)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last5, df_p_v_a_homeV_last5])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    total_partidosV = int(len(df_p_v_a_home))
    
    victorias_last5_as_homeV_df = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    victorias_last5_as_homeV = int(victorias_last5_as_homeV_df[victorias_last5_as_homeV_df['HOME_TEAM_WINS'] \
                                                               >= 1]['HOME_TEAM_WINS'].count())
    
    victorias_last5_as_visitorV_df = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    victorias_last5_as_visitorV = int(victorias_last5_as_visitorV_df[victorias_last5_as_visitorV_df['VISITOR_TEAM_WINS'] \
                                                                     >= 1]['VISITOR_TEAM_WINS'].count())
    
    victorias_last5_totalV = victorias_last5_as_homeV + victorias_last5_as_visitorV
    porcentaje_victorias_last5_home_team = (victorias_last5_totalV / total_partidosV) * 100
    
    return porcentaje_victorias_last5_home_team


def porcentaje_victorias_last5_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last5 = df_p_v_a_visitorH.tail(5)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last5 = df_p_v_a_visitorV.tail(5)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last5, df_p_v_a_visitorV_last5])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    total_partidosV = int(len(df_p_v_a_visitor))
    
    victorias_last5_as_homeV_df = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    victorias_last5_as_homeV = int(victorias_last5_as_homeV_df[victorias_last5_as_homeV_df['HOME_TEAM_WINS'] \
                                                               >= 1]['HOME_TEAM_WINS'].count())
    
    victorias_last5_as_visitorV_df = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    victorias_last5_as_visitorV = int(victorias_last5_as_visitorV_df[victorias_last5_as_visitorV_df['VISITOR_TEAM_WINS'] \
                                                                     >= 1]['VISITOR_TEAM_WINS'].count())
    
    victorias_last5_totalV = victorias_last5_as_homeV + victorias_last5_as_visitorV
    porcentaje_victorias_last5_visitor_team = (victorias_last5_totalV / total_partidosV) * 100
    
    return porcentaje_victorias_last5_visitor_team


def porcentaje_victorias_last10_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last10 = df_p_v_a_homeH.tail(10)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last10 = df_p_v_a_homeV.tail(10)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last10, df_p_v_a_homeV_last10])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    total_partidosV = int(len(df_p_v_a_home))
    
    victorias_last10_as_homeV_df = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    victorias_last10_as_homeV = int(victorias_last10_as_homeV_df[victorias_last10_as_homeV_df['HOME_TEAM_WINS'] \
                                                                 >= 1]['HOME_TEAM_WINS'].count())
    
    victorias_last10_as_visitorV_df = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    victorias_last10_as_visitorV = int(victorias_last10_as_visitorV_df[victorias_last10_as_visitorV_df['VISITOR_TEAM_WINS'] \
                                                                       >= 1]['VISITOR_TEAM_WINS'].count())
    
    victorias_last10_totalV = victorias_last10_as_homeV + victorias_last10_as_visitorV
    porcentaje_victorias_last10_home_team = (victorias_last10_totalV / total_partidosV) * 100
    
    return porcentaje_victorias_last10_home_team


def porcentaje_victorias_last10_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last10 = df_p_v_a_visitorH.tail(10)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last10 = df_p_v_a_visitorV.tail(10)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last10, df_p_v_a_visitorV_last10])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    total_partidosV = int(len(df_p_v_a_visitor))
    
    victorias_last10_as_homeV_df = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    victorias_last10_as_homeV = int(victorias_last10_as_homeV_df[victorias_last10_as_homeV_df['HOME_TEAM_WINS'] \
                                                                 >= 1]['HOME_TEAM_WINS'].count())
    
    victorias_last10_as_visitorV_df = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    victorias_last10_as_visitorV = int(victorias_last10_as_visitorV_df[victorias_last10_as_visitorV_df['VISITOR_TEAM_WINS'] \
                                                                       >= 1]['VISITOR_TEAM_WINS'].count())
    
    victorias_last10_totalV = victorias_last10_as_homeV + victorias_last10_as_visitorV
    porcentaje_victorias_last10_visitor_team = (victorias_last10_totalV / total_partidosV) * 100
    
    return porcentaje_victorias_last10_visitor_team


def avg_points_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_points_as_homeH = df_p_v_a_homeH['PTS_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_points_as_homeV = df_p_v_a_homeV['PTS_away']
    
    df_p_v_a_home = pd.concat([avg_points_as_homeH, avg_points_as_homeV])
    avg_total_home_team = np.mean(df_p_v_a_home)
    
    return avg_total_home_team


def avg_points_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorH = df_p_v_a_visitorH['PTS_home']
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorV = df_p_v_a_visitorV['PTS_away']
    
    df_p_v_a_visitor = pd.concat([avg_points_as_visitorH, avg_points_as_visitorV])
    avg_total_visitor_team = np.mean(df_p_v_a_visitor)
    
    return avg_total_visitor_team


def avg_points_last5_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last5 = df_p_v_a_homeH.tail(5)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last5 = df_p_v_a_homeV.tail(5)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last5, df_p_v_a_homeV_last5])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_points_as_homeH = df_p_v_a_homeH['PTS_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_points_as_homeV = df_p_v_a_homeV['PTS_away']
    
    df_p_v_a_home = pd.concat([avg_points_as_homeH, avg_points_as_homeV])
    avg_total_home_team = np.mean(df_p_v_a_home)    

    return avg_total_home_team


def avg_points_last5_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last5 = df_p_v_a_visitorH.tail(5)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last5 = df_p_v_a_visitorV.tail(5)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last5, df_p_v_a_visitorV_last5])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorH = df_p_v_a_visitorH['PTS_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorV = df_p_v_a_visitorV['PTS_away']
    
    df_p_v_a_visitor = pd.concat([avg_points_as_visitorH, avg_points_as_visitorV])
    avg_total_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_total_visitor_team


def avg_points_last10_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last10 = df_p_v_a_homeH.tail(10)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last10 = df_p_v_a_homeV.tail(10)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last10, df_p_v_a_homeV_last10])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_points_as_homeH = df_p_v_a_homeH['PTS_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_points_as_homeV = df_p_v_a_homeV['PTS_away']
    
    df_p_v_a_home = pd.concat([avg_points_as_homeH, avg_points_as_homeV])
    avg_total_home_team = np.mean(df_p_v_a_home)    

    return avg_total_home_team


def avg_points_last10_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last10 = df_p_v_a_visitorH.tail(10)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last10 = df_p_v_a_visitorV.tail(10)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last10, df_p_v_a_visitorV_last10])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorH = df_p_v_a_visitorH['PTS_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_points_as_visitorV = df_p_v_a_visitorV['PTS_away']
    
    df_p_v_a_visitor = pd.concat([avg_points_as_visitorH, avg_points_as_visitorV])
    avg_total_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_total_visitor_team


def avg_fg_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg_as_homeH = df_p_v_a_homeH['FG_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg_as_homeV = df_p_v_a_homeV['FG_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg_as_homeH, avg_fg_as_homeV])
    avg_fg_home_team = np.mean(df_p_v_a_home)
    
    return avg_fg_home_team


def avg_fg_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg_as_visitorH = df_p_v_a_visitorH['FG_PCT_home']
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg_as_visitorV = df_p_v_a_visitorV['FG_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg_as_visitorH, avg_fg_as_visitorV])
    avg_fg_visitor_team = np.mean(df_p_v_a_visitor)
    
    return avg_fg_visitor_team


def avg_fg_last5_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last5 = df_p_v_a_homeH.tail(5)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last5 = df_p_v_a_homeV.tail(5)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last5, df_p_v_a_homeV_last5])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    total_partidosV = int(len(df_p_v_a_home))
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg5_as_homeH = df_p_v_a_homeH['FG_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg5_as_homeV = df_p_v_a_homeV['FG_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg5_as_homeH, avg_fg5_as_homeV])
    avg_fg5_home_team = np.mean(df_p_v_a_home)    

    return avg_fg5_home_team


def avg_fg_last5_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last5 = df_p_v_a_visitorH.tail(5)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last5 = df_p_v_a_visitorV.tail(5)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last5, df_p_v_a_visitorV_last5])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg5_as_visitorH = df_p_v_a_visitorH['FG_PCT_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg5_as_visitorV = df_p_v_a_visitorV['FG_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg5_as_visitorH, avg_fg5_as_visitorV])
    avg_fg5_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_fg5_visitor_team


def avg_fg_last10_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last10 = df_p_v_a_homeH.tail(10)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last10 = df_p_v_a_homeV.tail(10)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last10, df_p_v_a_homeV_last10])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg10_as_homeH = df_p_v_a_homeH['FG_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg10_as_homeV = df_p_v_a_homeV['FG_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg10_as_homeH, avg_fg10_as_homeV])
    avg_fg10_home_team = np.mean(df_p_v_a_home)    

    return avg_fg10_home_team


def avg_fg_last10_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last10 = df_p_v_a_visitorH.tail(10)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last10 = df_p_v_a_visitorV.tail(10)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last10, df_p_v_a_visitorV_last10])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg10_as_visitorH = df_p_v_a_visitorH['FG_PCT_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg10_as_visitorV = df_p_v_a_visitorV['FG_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg10_as_visitorH, avg_fg10_as_visitorV])
    avg_fg10_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_fg10_visitor_team


def avg_fg3_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg3_as_homeH = df_p_v_a_homeH['FG3_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg3_as_homeV = df_p_v_a_homeV['FG3_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg3_as_homeH, avg_fg3_as_homeV])
    avg_fg3_home_team = np.mean(df_p_v_a_home)
    
    return avg_fg3_home_team


def avg_fg3_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg3_as_visitorH = df_p_v_a_visitorH['FG3_PCT_home']
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg3_as_visitorV = df_p_v_a_visitorV['FG3_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg3_as_visitorH, avg_fg3_as_visitorV])
    avg_fg3_visitor_team = np.mean(df_p_v_a_visitor)
    
    return avg_fg3_visitor_team


def avg_fg3_last5_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last5 = df_p_v_a_homeH.tail(5)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last5 = df_p_v_a_homeV.tail(5)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last5, df_p_v_a_homeV_last5])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg35_as_homeH = df_p_v_a_homeH['FG3_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg35_as_homeV = df_p_v_a_homeV['FG3_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg35_as_homeH, avg_fg35_as_homeV])
    avg_fg35_home_team = np.mean(df_p_v_a_home)    

    return avg_fg35_home_team


def avg_fg3_last5_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last5 = df_p_v_a_visitorH.tail(5)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last5 = df_p_v_a_visitorV.tail(5)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last5, df_p_v_a_visitorV_last5])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(5)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg35_as_visitorH = df_p_v_a_visitorH['FG3_PCT_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg35_as_visitorV = df_p_v_a_visitorV['FG3_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg35_as_visitorH, avg_fg35_as_visitorV])
    avg_fg35_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_fg35_visitor_team


def avg_fg3_last10_home_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1h = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == home_team)]
    df2h = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == home_team)]
    df_p_v_a_home = pd.concat([df1h, df2h])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    df_p_v_a_homeH_last10 = df_p_v_a_homeH.tail(10)
    
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    df_p_v_a_homeV_last10 = df_p_v_a_homeV.tail(10)
    
    df_p_v_a_home = pd.concat([df_p_v_a_homeH_last10, df_p_v_a_homeV_last10])
    df_p_v_a_home = df_p_v_a_home.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    total_partidosV = int(len(df_p_v_a_home))
    
    df_p_v_a_homeH = df_p_v_a_home.query("HOME_TEAM_ID == " + str(home_team))
    avg_fg310_as_homeH = df_p_v_a_homeH['FG3_PCT_home']
        
    df_p_v_a_homeV = df_p_v_a_home.query("VISITOR_TEAM_ID == " + str(home_team))
    avg_fg310_as_homeV = df_p_v_a_homeV['FG3_PCT_away']
    
    df_p_v_a_home = pd.concat([avg_fg310_as_homeH, avg_fg310_as_homeV])
    avg_fg310_home_team = np.mean(df_p_v_a_home)    

    return avg_fg310_home_team


def avg_fg3_last10_visitor_team(game_id):
    home_team, visitor_team, df_p_v_a = home_visitor_df(game_id)
    
    df1v = df_p_v_a[(df_p_v_a['HOME_TEAM_ID'] == visitor_team)]
    df2v = df_p_v_a[(df_p_v_a['VISITOR_TEAM_ID'] == visitor_team)]
    df_p_v_a_visitor = pd.concat([df1v, df2v])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID'])
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorH_last10 = df_p_v_a_visitorH.tail(10)
    
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    df_p_v_a_visitorV_last10 = df_p_v_a_visitorV.tail(10)
    
    df_p_v_a_visitor = pd.concat([df_p_v_a_visitorH_last10, df_p_v_a_visitorV_last10])
    df_p_v_a_visitor = df_p_v_a_visitor.sort_values(['GAME_DATE', 'GAME_ID']).tail(10)
    
    df_p_v_a_visitorH = df_p_v_a_visitor.query("HOME_TEAM_ID == " + str(visitor_team))
    avg_fg310_as_visitorH = df_p_v_a_visitorH['FG3_PCT_home']
        
    df_p_v_a_visitorV = df_p_v_a_visitor.query("VISITOR_TEAM_ID == " + str(visitor_team))
    avg_fg310_as_visitorV = df_p_v_a_visitorV['FG3_PCT_away']
    
    df_p_v_a_visitor = pd.concat([avg_fg310_as_visitorH, avg_fg310_as_visitorV])
    avg_fg310_visitor_team = np.mean(df_p_v_a_visitor)

    return avg_fg310_visitor_team