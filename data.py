#!venv/bin python
# -*- coding: utf-8 -*-

#Script for creating randam dataset for project
#Script generates random dates, oilprices and countries

import pandas as pd
import numpy as np

def random_dates(start:str, end:str, n:int, unit='D', seed=None):
    """
    Func generates random data
    start: DD/MM/YYYY format for start date
    end: DD/MM/YYY format for end date
    n: size of array
    unit: D - days
    """
    if not seed: 
        np.random.seed(0)
    
    start = pd.to_datetime(start, dayfirst=True)
    end = pd.to_datetime(end, dayfirst=True)
    
    ndays = (end - start).days + 1
    return start + pd.to_timedelta(np.random.randint(0, ndays, n), unit=unit)

def name(x):
    if x == 1: return 'China'
    if x == 2: return 'Germany'
    if x == 3: return 'Great Britain'
    else: return 'Japan'

def dataset(start='01/01/2022', end='01/12/2022', n=1000):
    """
    Function creates dataset
    """
    data = pd.DataFrame({'date':random_dates(start,end, n),
                        'name':np.random.randint(1, 4, n),
                        'price_bbl':np.random.uniform(60, 120, n).round(2)})
    data['name'] = data.name.apply(name)
    return data