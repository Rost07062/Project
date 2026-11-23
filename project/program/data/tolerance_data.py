#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:29:48 2026

@author: vboxuser
"""

import numpy as np

from data.leontiev_data import leontiev_sdv, LEONTIEV_REFLEXIVITY_KEYS
from defs.increasing_defs import increase, concatenate


""" Толерантность к неопределенности """
tolerance_sdv = leontiev_sdv + len(LEONTIEV_REFLEXIVITY_KEYS)

TOLERANCE_UNCERAIN_KEYS = [i for i in range(167, 189)]
del TOLERANCE_UNCERAIN_KEYS[2]
del TOLERANCE_UNCERAIN_KEYS[18]
del TOLERANCE_UNCERAIN_KEYS[18]

TOLERANCE_UNCERAIN_KEYS = np.array(TOLERANCE_UNCERAIN_KEYS)

TOLERANCE_MAX_VAL = 8
TOLERANCE_DICT = {
    "Совершенно не согласна": "1",
	"В значительной степени не согласна": "2",
    "Отчасти не согласна": "3",
	"Нечто среднее": "4",
	"Отчасти согласна": "5",
    "В значительной степени согласна": "6",
	"Совершенно согласна": "7"}

TOLERANCE_CATEG = ["Отношение к новизне", "Отношение к сложным задачам", 
                   "Отношение к неопределённым ситуациям", "Предпочтение неопределенности",
                   "Толерантность/избегание неопределенности", 
                   "Интегральный показатель толерантности к неопределенности"]

TOLERANCE_POINTS = np.array([0 for _ in range(len(TOLERANCE_CATEG))])

TOLERANCE_NEW_REVERSE_KEYS = np.array([7])
TOLERANCE_NEW_RIGHT_KEYS = np.array([13, 14])

TOLERANCE_HARD_REVERSE_KEYS = np.array([4, 8, 9, 12])
TOLERANCE_HARD_RIGHT_KEYS = np.array([11, 16, 18])

TOLERANCE_UNCERTAIN_REVERSE_KEYS = np.array([1, 2, 5, 15])
TOLERANCE_UNCERTAIN_RIGHT_KEYS = np.array([3, 6, 10, 17, 19])

TOLERANCE_PREFERENCE_KEYS = np.array([3, 6, 10, 11, 13, 14, 16, 17, 18, 19]) # все прямые ключи
TOLERANCE_TOLERANCE_KEYS = np.array([1, 2, 4, 5, 7, 8, 9, 12, 15]) # все обратные ключи

TOLERANCE_NEW_REVERSE_KEYS, TOLERANCE_NEW_RIGHT_KEYS,\
TOLERANCE_HARD_REVERSE_KEYS, TOLERANCE_HARD_RIGHT_KEYS,\
TOLERANCE_UNCERTAIN_REVERSE_KEYS, TOLERANCE_UNCERTAIN_RIGHT_KEYS,\
TOLERANCE_PREFERENCE_KEYS, TOLERANCE_TOLERANCE_KEYS = increase([TOLERANCE_NEW_REVERSE_KEYS, TOLERANCE_NEW_RIGHT_KEYS,
                                                                TOLERANCE_HARD_REVERSE_KEYS, TOLERANCE_HARD_RIGHT_KEYS,
                                                                TOLERANCE_UNCERTAIN_REVERSE_KEYS, TOLERANCE_UNCERTAIN_RIGHT_KEYS,
                                                                TOLERANCE_PREFERENCE_KEYS, TOLERANCE_TOLERANCE_KEYS], tolerance_sdv + 1)

TOLERANCE_ALL_NEW_KEYS = concatenate(TOLERANCE_NEW_REVERSE_KEYS, TOLERANCE_NEW_RIGHT_KEYS)

TOLERANCE_ALL_HARD_KEYS = concatenate(TOLERANCE_HARD_REVERSE_KEYS, TOLERANCE_HARD_RIGHT_KEYS)

TOLERANCE_ALL_UNCERTAIN_KEYS = concatenate(TOLERANCE_UNCERTAIN_REVERSE_KEYS, TOLERANCE_UNCERTAIN_RIGHT_KEYS)

TOLERANCE_ALL_PREFERENCE_KEYS = TOLERANCE_PREFERENCE_KEYS.copy()

TOLERANCE_ALL_TOLERANCE_KEYS = TOLERANCE_TOLERANCE_KEYS.copy()

TOLERANCE_ALL_MAIN_KEYS = TOLERANCE_UNCERAIN_KEYS.copy()

TOLERANCE_ALL_UNCERTAIN_KEYS[-1] += 2
TOLERANCE_ALL_PREFERENCE_KEYS[-1] += 2

TOLERANCE_ALL_UNCERTAIN_KEYS[:2] -= 1
TOLERANCE_ALL_TOLERANCE_KEYS[:2] -= 1


class ALL_TOLERANCE:
    def __init__(self):
        self.TOLERANCE_UNCERAIN_KEYS = TOLERANCE_UNCERAIN_KEYS
        self.TOLERANCE_DICT = TOLERANCE_DICT
        self.TOLERANCE_TOLERANCE_KEYS = TOLERANCE_TOLERANCE_KEYS
        self.TOLERANCE_MAX_VAL = TOLERANCE_MAX_VAL
        self.TOLERANCE_CATEG = TOLERANCE_CATEG
        self.TOLERANCE_POINTS = TOLERANCE_POINTS
        self.TOLERANCE_ALL_NEW_KEYS = TOLERANCE_ALL_NEW_KEYS
        self.TOLERANCE_ALL_HARD_KEYS = TOLERANCE_ALL_HARD_KEYS
        self.TOLERANCE_ALL_UNCERTAIN_KEYS = TOLERANCE_ALL_UNCERTAIN_KEYS
        self.TOLERANCE_ALL_PREFERENCE_KEYS = TOLERANCE_ALL_PREFERENCE_KEYS
        self.TOLERANCE_ALL_TOLERANCE_KEYS = TOLERANCE_ALL_TOLERANCE_KEYS
        self.TOLERANCE_ALL_MAIN_KEYS = TOLERANCE_ALL_MAIN_KEYS


