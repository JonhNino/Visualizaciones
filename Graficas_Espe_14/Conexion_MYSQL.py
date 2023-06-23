#import mysql.connector as connection
#import pandas as pd
#try:
#    mydb = connection.connect(host="localhost", database = 'agricultura_especializacion',user="root", passwd="",use_pure=True,port = 3306)
#    query = "Select * from cosecha;"
#    result_dataFrame = pd.read_sql(query,mydb)
#    mydb.close() #close the connection
#except Exception as e:
#    mydb.close()
#    print(str(e))


import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import geopandas 
try:
    engine = create_engine('mysql+mysqlconnector://root:@localhost/classicmodels')
    query = "SELECT * FROM offices;"
    result_dataFrame = pd.read_sql(query, engine)
    engine.dispose() #close the connection
except Exception as e:
    print(str(e))
x_values = result_dataFrame['country'].unique()
y_values = result_dataFrame['country'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.show()
#fig, ax= plt.subplots()
colores =["#EE6055","#60D394","#AAF683","#FFD977"]
fig, ax = plt.subplots()
ax.pie(y_values, labels=x_values, autopct='%1.1f%%', startangle=90)
plt.show()
world = geopandas.read_file(geopandas.datasets.get_path('offices'))
#cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
world.head()
world.plot()