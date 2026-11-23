#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:25:41 2026

@author: vboxuser
"""

import numpy as np

from data.riff_data import riff_sdv, RIFF_PSYCH_WELL_BEING_KEYS

""" Шкала удовлетворенности Динера """
diner_sdv = riff_sdv + len(RIFF_PSYCH_WELL_BEING_KEYS)

DINER_SATISFACTION_KEYS = np.array([i for i in range(87, 92)])

DINER_MAX_VAL = 8
DINER_DICT = {
    "Полностью не согласна": "1",
    "Не согласна": "2",
    "Скорее не согласна": "3",
    "Нечто среднее": "4",
    "Скорее согласна": "5",
    "Согласна": "6",
    "Полностью согласна": "7"}

DINER_CATEG = ["Удовлетворенность жизнью"]

DINER_POINTS = np.array([0])

DINER_ALL_SATISFACTION_KEYS = DINER_SATISFACTION_KEYS

class ALL_DINER:
    def __init__(self):
        self.DINER_SATISFACTION_KEYS = DINER_SATISFACTION_KEYS
        self.DINER_DICT = DINER_DICT
        self.DINER_MAX_VAL = DINER_MAX_VAL
        self.DINER_CATEG = DINER_CATEG
        self.DINER_POINTS = DINER_POINTS
        self.DINER_ALL_SATISFACTION_KEYS = DINER_ALL_SATISFACTION_KEYS

