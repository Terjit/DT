import sqlite3
import math
import pandas as pd
conn = sqlite3.connect('dt.db')
        
cursor = conn.cursor()
wells = []

#cursor.execute("DROP TABLE FORMATIONS")

#cursor.execute("""CREATE TABLE WELLS( 
#               operator VARCHAR(255) NOT NULL,
#               API VARCHAR(255) NOT NULL,
#               wellName VARCHAR(255) NOT NULL,
#               latitude FLOAT NOT NULL,
#               longitude FLOAT NOT NULL,
#               wellType VARCHAR(255) NOT NULL)
#               """)

#cursor.execute("""CREATE TABLE FORMATIONS ( 
#               wellName VARCHAR(255) NOT NULL,
#               formationName VARCHAR(255) NOT NULL,
#               MD FLOAT NOT NULL,
#               TVD FLOAT NOT NULL)
#               """)

#cursor.execute("""CREATE TABLE DEV( 
#              wellName VARCHAR(255) NOT NULL,
#              MD FLOAT NOT NULL,
#              INC FLOAT NOT NULL,
#              AZI FLOAT NOT NULL,
#              TVD FLOAT,
#              DLS FLOAT,
#              NS FLOAT,
#              EW FLOAT,
#              Planned INTEGER NOT NULL,
#              Lateral VARCHAR(255) NOT NUll, 
#              )""")     

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

#data = cursor.execute(f"SELECT DISTINCT wellName FROM DEV WHERE wellName like '3T%'" )

#if not data.fetchone():
#    print(True)

#for item in data:
#    for subItem in item:
#        print(subItem)

#cursor.execute("DELETE FROM DEV WHERE wellName = '3T-612'")
#data = pd.read_csv('3T-616 Directional.csv')

#for item in data.iterrows():
#    print(item[1].iloc[0])

#cursor.execute("ALTER TABLE DEV ADD COLUMN Lateral VCHAR(255)")

#cursor.execute("UPDATE DEV SET Lateral = 'Null'")

#data = cursor.execute("UPDATE DEV SET Planned = 0 WHERE wellName = '3S-14'")

#cursor.execute("DELETE FROM DEV WHERE wellName ='3T-616'")

data = cursor.execute("Select * from DEV")

for item in data:
    print(item)

conn.commit()


conn.close()               
                

