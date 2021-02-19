import pandas as pd
import numpy as np
import re
from pandasql import sqldf

pysqldf = lambda q:sqldf(q,globals())


def lowerdiy(x):
    if len(x.split('[')) == 2:
        return '>=' + str(x.split('[')[1])
    else:
        return '>' + str(x.split('(')[1])
    
def upperdiy(x):
    if len(x.split(']')) == 2:
        return '<=' + str(x.split(']')[0])
    else:
        return '<' + str(x.split(')')[0])
    
def splitdiy(var,x,y):
    try:
        lower = x.split('~')[0]
        upper = x.split('~')[1]
        if re.search('inf',lowerdiy(lower)) != None:
            return 'when {0} {1} then {2} '.format(var,upperdiy(upper),y)
        elif re.search('inf',upperdiy(upper)) != None:
            return 'when {0} {1} then {2} '.format(var,lowerdiy(lower),y)
        else:
            return 'when {0} {1} and {0} {2} then {3} '.format(var,lowerdiy(lower),upperdiy(upper),y)
    except:
        return 'when {0} is null then {1} '.format(var,y)

def autosql(df):
    sqlt = ''
    for i in df['name'].unique():
        sql_slice = 'case '
        for j in range(df.query('name == @i').shape[0]):
            sql_slice = sql_slice + splitdiy(i,df.query('name == @i').iloc[j]['value'],df.query('name == @i').iloc[j]['score'])+' \n'
        sql_slice += 'end as {}, \n'.format(i)
        sqlt += sql_slice
    sqlt = sqlt[:-3]
    return print(sqlt)   
