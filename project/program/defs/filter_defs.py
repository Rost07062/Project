#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:41:33 2026

@author: vboxuser
"""
import pandas as pd

def demograph_filter(demograph_df, respondents_df):
    demograph_filter = demograph_df[(pd.to_numeric(demograph_df['Возраст']).between(40, 55)) &
                (demograph_df['Профессиональный статус'].str.contains("Работаю по найму", case=False, na=False))&
                (demograph_df['Количество детей'].isin(["1", "2"]))& # 6 человек отметается когда убираю "Нет детей"
                (demograph_df['Ведет ли вы быт'].str.contains('Да', case=False, na=False))
                ]
    
    filter_indexses = demograph_filter.index.tolist()
    
    filter_respondents = respondents_df.iloc[filter_indexses]
    
    return filter_indexses, filter_respondents