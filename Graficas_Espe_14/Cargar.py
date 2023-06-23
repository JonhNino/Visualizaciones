import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_movie=pd.read_csv('https://raw.githubusercontent.com/cva1977/archivospandas/master/movies.txt',header=0,sep='\t')
df_actor=pd.read_csv('https://raw.githubusercontent.com/cva1977/archivospandas/master/actor.txt',header=0,sep='\t')
df_gender=pd.read_csv('https://raw.githubusercontent.com/cva1977/archivospandas/master/gender.txt',header=0,sep='\t')
df_ma=pd.read_csv('https://raw.githubusercontent.com/cva1977/archivospandas/master/actor_movies.txt',header=0,sep='\t')
print(df_gender)
print(df_movie[['mov_id','mov_title','mov_time']].sort_values(['mov_time'],ascending=False).head(5))
print(df_movie['mov_rel_country'].unique())
# select top 2 * from movies where mov_rel_country='USA'
print(df_movie[df_movie.mov_rel_country=='USA'].head(2))
# select * from movies 
#where mov_year>1990 and mov_time>100

df_movie[(df_movie.mov_year>1990) & (df_movie.mov_time>100)]
print(df_movie[(df_movie.mov_year>1990) & (df_movie.mov_time>100)])
#select mov_title,mov_year 
#from movies 
#where mov_rel_country='SW' or mov_rel_country='USA'

df_movie[(df_movie.mov_rel_country=='SW') | (df_movie.mov_rel_country=='USA')][['mov_title','mov_year']]
print(df_movie[(df_movie.mov_rel_country=='SW') | (df_movie.mov_rel_country=='USA')][['mov_title','mov_year']])

print(df_movie[(~df_movie.mov_rel_country.isin(['SW','USA']))][['mov_title','mov_year']])
#select mov_rel_country,count(*)
#from movies
#group by mov_rel_country

print(df_movie.groupby(['mov_rel_country']).agg({'mov_rel_country':'count'}))
#select *
#from movies t1 inner join gender t2 on t1.genero=t2.gen_id
#where t1.gen_title='Drama'

print(pd.merge(df_movie, df_gender[ df_gender.gen_title=='Drama'], how='inner',left_on='genero', right_on='gen_id'))