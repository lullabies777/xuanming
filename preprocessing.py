import pandas as pd
from datetime import datetime
import time
import numpy as np


def get_sex(id):
    ## 男生 1 女生 0
    if len(id) == 18:
        num = int(id[16:17])
        if num % 2 == 0 :
            return(0)
        else:
            return(1)
    else:
        num = int(id[14:15])
        if num % 2 == 0 :
            return(0)
        else:
            return(1)
        
def get_age(id,apply):
    '''
       id: 身份证
       apply: 申请时间 年月日 
    '''
    if len(apply) == 10:
        day1 = datetime.strptime(apply, '%Y-%m-%d')
    else:
        day1 = datetime.strptime(apply, '%Y%m%d')
    
    if len(id) == 18:
        year = int(id[6:10])
    else:
        year = 1900 + int(id[6:8])
    age = day1.year - year
    return age




def get_days(apply,his):
    ## apply 具体到日期
    ## his 自动识别是以月是颗粒还是日为颗粒
    if his == 'nan':
        return np.nan
    if isinstance(his,float):
        his = int(float(his))
    if len(his.split('.')) > 1:
        his = str(int(float(his)))
    if len(his) < 8:
        if len(apply) == 10:
            day1 = datetime.strptime(apply, '%Y-%m-%d')
        else:
            day1 = datetime.strptime(apply, '%Y%m%d')
        if len(his) == 7:
            day2 = datetime.strptime(his, '%Y-%m')
        else:
            day2 = datetime.strptime(his, '%Y%m')
        months = 12*(day1.year - day2.year) + day1.month - day2.month
        return months
    else:
        if len(apply) == 10:
            day1 = datetime.strptime(apply, '%Y-%m-%d')
        else:
            day1 = datetime.strptime(apply, '%Y%m%d')
        if len(his) == 10:
            day2 = datetime.strptime(his, '%Y-%m-%d')
        else:
            day2 = datetime.strptime(his, '%Y%m%d')
        return(day1-day2).days