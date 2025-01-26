import pandas as pd
import numpy as np


def dirCalcs(data):
    df = pd.DataFrame()
    df = data
    df.columns = ['MD','INC','AZI']
    df['TVD'] = 0
    temp = pd.DataFrame()

    temp['dMD'] = df['MD'] - df['MD'].shift(1)
    temp['INCrad'] = np.radians(round(df['INC'],2))
    temp['AZIrad'] = np.radians(df['AZI'])
    temp['DL1'] = (np.cos(temp['INCrad'].shift(1))*np.cos(temp['INCrad']))+(np.sin(temp['INCrad'].shift(1))*np.sin(temp['INCrad']))*(np.cos(temp['AZIrad']-temp['AZIrad'].shift(1)))
    temp.loc[temp['DL1'] > 1, 'DL1'] = 1
    temp.loc[temp['DL1'] < -1, 'DL1'] = -1
    temp['DL'] = np.acos(temp['DL1'])
    temp['RF'] = np.tan(temp['DL']/2)/(temp['DL']/2)
    temp.loc[temp['DL'] == 0 , 'RF'] = 1
    temp['dNS'] = ((np.sin(temp['INCrad'].shift(1))*np.cos(temp['AZIrad'].shift(1)))+(np.sin(temp['INCrad'])*np.cos(temp['AZIrad'])))*(temp['RF']*(temp['dMD']*0.5))
    temp['dEW'] = ((np.sin(temp['INCrad'].shift(1))*np.sin(temp['AZIrad'].shift(1)))+(np.sin(temp['INCrad'])*np.sin(temp['AZIrad'])))*(temp['RF']*(temp['dMD']*0.5))
    temp['dTVD'] =(np.cos(temp['INCrad'].shift())+np.cos(temp['INCrad']))*(temp['RF']*(temp['dMD']*0.5))
    temp['dTVD'] = temp['dTVD'].fillna(df['MD'])

    df['DLS'] = np.degrees(temp['DL'])*100/temp['dMD']
    df['NS'] = temp['dNS'].cumsum()
    df['EW'] = temp['dEW'].cumsum()
    df['TVD'] = temp['dTVD'].cumsum()

    return df
        