#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:36:38 2026

@author: vboxuser
"""
from sklearn.tree import DecisionTreeRegressor, plot_tree
import pandas as pd
import matplotlib.pyplot as plt



class tree_work:
    def __init__(self, demograph_df, respondents_df):
        self.ALL_DATA = pd.concat([demograph_df, respondents_df], axis=1)
        self.demograph_df = demograph_df
    def create_tree(self):
        self.ALL_DATA["Состояние здоровья"] = self.ALL_DATA["Состояние здоровья"].str.join(" ")
        # replace_children_categ(ALL_DATA, count_strings)
        X = self.ALL_DATA[self.demograph_df.columns]
        X_encoded = pd.get_dummies(X, drop_first=True)
        
        Y = self.ALL_DATA["Интегральный показатель психологического благополучия"]
        
        model = DecisionTreeRegressor(max_depth=7, random_state=42)
        model.fit(X_encoded, Y)
        
        
        
        plt.figure(figsize=(25, 15))
        plot_tree(
            model, 
            feature_names=X_encoded.columns,
            filled=True,       # Цвет зависит от среднего значения (чем темнее, тем выше/ниже средний результат)
            rounded=True,
            fontsize=6,
            impurity=False,    # Можно отключить дисперсию, чтобы не загромождать
            proportion=False   # Отключаем доли объектов
        )
        plt.title("Дерево регрессии: как категории влияют на результат теста")
        
        plt.show()
        plt.close('all')