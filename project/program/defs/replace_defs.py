#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:00:49 2026

@author: vboxuser
"""
import pandas as pd


            

def replace_children_categ(df, count_strings):
    """
    Категории: 0-2 Малыш
               3-6 Ребенок
               7-11 Доподросток
               12-17 Старшие подростки
               18-22 Студент
               >=23 Взрослый
    """
    categ_children = ["Малыш", "Ребенок", "Доподросток", "Подросток", "Студент", "Взрослый"]
    
    for i in range(count_strings):
        curr = list(map(lambda x: x.strip(), df.loc[i, "Возраст детей"].split(',')))
        if curr[0] != '-':
            curr = list(map(lambda x: 0 if "месяц" in x.lower() else(float(x.split()[0]) if "лет" in x.lower() else float(x)), curr))
            for j in range(len(curr)):
                curr_child = curr[j]
                if 0 <= curr_child <= 2:
                    curr[j] = categ_children[0]
                elif 3 <= curr_child <= 6:
                    curr[j] = categ_children[1]
                elif 7 <= curr_child <= 11:
                    curr[j] = categ_children[2]
                elif 12 <= curr_child <= 17:
                    curr[j] = categ_children[3]
                elif 18 <= curr_child <= 22:  
                    curr[j] = categ_children[4]
                else:
                    curr[j] = categ_children[5]
        df.loc[i, "Возраст детей"] = " ".join(sorted(list(set(curr))))
        
def make_demograph_dict(keys, health_keys, demograph_categories, curr_string):
    demograph_dict = dict.fromkeys(demograph_categories, 0)
    health_array = []
    for i in keys:
        if i in health_keys and not(pd.isna(curr_string[i])):
            health_array.append(curr_string[i])
        elif not(health_array):
            demograph_dict[demograph_categories[i]] = curr_string[i]
        elif i not in health_keys:
            demograph_dict[demograph_categories[i - 1]] = health_array.copy()
            demograph_dict[demograph_categories[i]] = curr_string[i]
            health_array.clear()

    return demograph_dict