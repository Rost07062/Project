#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:23:32 2026

@author: vboxuser

"""
import numpy as np

from data.demograph_data import DEMOGRAPH_KEYS

""" Опросник психологически богатой жизни Оиши """
oishi_sdv = len(DEMOGRAPH_KEYS)

OISHI_PSYCH_RICH_KEYS = np.array([i for i in range(16, 33)])

OISHI_MAX_VAL = 8
OISHI_DICT = {
    "Совершенно не согласна": "1",
    "Не согласна": "2",
    "Скорее не согласна": "3",
    "Нейтрально": "4",
    "Скорее согласна": "5",
    "Согласна": "6",
    "Совершенно согласна": "7"}

OISHI_CATEG = ["Психологически богатая жизнь"]

OISHI_POINTS = np.array([0])

OISHI_REVERSE_KEYS = np.array([11, 14, 15])
OISHI_REVERSE_KEYS += oishi_sdv

OISHI_ALL_PSYCH_RICH_KEYS = OISHI_PSYCH_RICH_KEYS

class ALL_OISHI:
    def __init__(self):
        self.OISHI_PSYCH_RICH_KEYS = OISHI_PSYCH_RICH_KEYS
        self.OISHI_DICT = OISHI_DICT
        self.OISHI_REVERSE_KEYS = OISHI_REVERSE_KEYS
        self.OISHI_MAX_VAL = OISHI_MAX_VAL
        self.OISHI_CATEG = OISHI_CATEG
        self.OISHI_POINTS = OISHI_POINTS
        self.OISHI_ALL_PSYCH_RICH_KEYS = OISHI_ALL_PSYCH_RICH_KEYS