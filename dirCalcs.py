import pandas as pd
import numpy as np
import math


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

def latLon(lat,lon):
    #Degree minute second to decimal = d + min/60 + sec/3600
    lat *= 3600
    latRad = math.radians(70.42083)

    lon *= 3600

    #Constants
    const = 500000
    cm = 540000

    cos1 = math.cos(latRad)
    cos2 = cos1 ** 2
    cos4 = cos1 ** 4
    cos6 = cos1 ** 6

    cm1 = (cm-lon)/(10**4)
    cm2 = cm1 ** 2
    cm4 = cm1 ** 4

    #Calculate x from lat lon
    a = ((1017862.150*cos1)/((1+0.006814789*cos2)**0.5))*cm1
    b = (3.91740509/(10**4)*cm2)
    c = 1-2*cos2-0.681478/(10**2)*cos4
    d = 4.60382/(10**8)*cm4
    e = 1-20*cos2+23.6047*cos4+0.4907*cos6

    x = const+a*(1-b*c+d*e)

    ##calculate y from lat lon
    f = lat-193900.054420-(1052.893943-4.483386*cos2+(2.3559/(10**2))*cos4)*(1-cos2)**0.5*cos1
    g = 24673.67480*(1-cos2)**0.5*cos1/((1+0.0068147849*cos2)**0.5)*cm2
    h = 1.958703/10**4*cm2*(-1+6*cos2+6.133306/10**2*cos4+1.8577/10**4*cos6)
    i = 1.5346/10**8*cm4*(1-60*cos2+117.5*cos4+4.089*cos6)

    y = 101.269278503*f+g*(1-h+i)    
    return(x, y)      