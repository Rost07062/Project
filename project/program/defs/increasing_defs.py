#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:06:17 2026

@author: vboxuser
"""
import numpy as np
import pandas as pd

def concatenate(*array):
    main_array = []
    for i in array:
        main_array.append(i)
    return np.concatenate(main_array)


def summ_respondent(string, keys):
    return pd.to_numeric(string[keys]).sum()
        
def increase(array, num):
    return [a + num for a in array]