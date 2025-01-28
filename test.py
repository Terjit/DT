import sqlite3
import math
import pandas as pd
conn = sqlite3.connect('dt.db')
        
cursor = conn.cursor()
wells = []

#cursor.execute("DROP TABLE DEV")

#cursor.execute("""CREATE TABLE DEV( 

#              wellName VARCHAR(255) NOT NULL,
#              MD FLOAT NOT NULL,
#              INC FLOAT NOT NULL,
#              AZI FLOAT NOT NULL,
#              TVD FLOAT,
#              DLS FLOAT,
#              NS FLOAT,
#              EW FLOAT)""")     

#cursor.execute("INSERT INTO WELLS VALUES ('Hilcorp', '500291111114', 'W-239', 70., 150., 'Producer')")
#cursor.execute("INSERT INTO WELLS VALUES ('CONOCO', '500291111112', '3T-612', 70.42095, 150.2628, 'Producer')")
#cursor.execute("INSERT INTO WELLS VALUES ('CONOCO', '500291111113', 'Nuna-1', 70.41966, 150.2681, 'Producer')")

#conn.commit()

#cursor.execute("INSERT INTO FORMATIONS VALUES ('3T-612', 'C40', '4000', '3500')")
well = '3T-616'
#data = cursor.execute(f"SELECT EW FROM DEV WHERE wellName = '{well}'")
#for item in data:
#    for subItem in item:
#        wells.append(subItem)

data = cursor.execute(f"SELECT DISTINCT wellName FROM DEV WHERE wellName like '3T%'" )

#if not data.fetchone():
#    print(True)

for item in data:
    for subItem in item:
        print(subItem)

#cursor.execute("DELETE FROM DEV WHERE wellName = '3T-612'")
#data = pd.read_csv('3T-616 Directional.csv')

#for item in data.iterrows():
#    print(item[1].iloc[0])

conn.commit()


conn.close()               
                

