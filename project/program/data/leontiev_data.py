#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:27:42 2026

@author: vboxuser
"""
import numpy as np

from data.maddi_data import maddi_sdv, MADDI_RESILIENCE_KEYS
from defs.increasing_defs import increase

""" Тест рефлексивности Леонтьева """
leontiev_sdv = maddi_sdv + len(MADDI_RESILIENCE_KEYS)

LEONTIEV_REFLEXIVITY_KEYS = np.array([i for i in range(137, 167)])

LEONTIEV_MAX_VAL = 5
LEONTIEV_DICT = {
	"Нет": "1",
	"Скорее нет, чем да": "2",
    "Скорее да, чем нет": "3",
    "Да": "4"}

LEONTIEV_CATEG = ["Системная рефлексия", "Интроспекция", "Квазирефлексия"]

LEONTIEV_POINTS = np.array([0 for _ in range(len(LEONTIEV_CATEG))])

LEONTIEV_SYSTEM_RIGHT_KEYS = np.array([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 29, 30])

LEONTIEV_INTRO_RIGHT_KEYS = np.array([2, 5, 8 , 11, 14, 17, 20, 23, 26])

LEONTIEV_QUASI_RIGHT_KEYS = np.array([3, 6 , 9, 12, 15, 18, 21, 24, 27])

LEONTIEV_SYSTEM_RIGHT_KEYS,\
LEONTIEV_INTRO_RIGHT_KEYS,\
LEONTIEV_QUASI_RIGHT_KEYS = increase([LEONTIEV_SYSTEM_RIGHT_KEYS,
                                      LEONTIEV_INTRO_RIGHT_KEYS,
                                      LEONTIEV_QUASI_RIGHT_KEYS], leontiev_sdv)

LEONTIEV_ALL_SYSTEM_KEYS = LEONTIEV_SYSTEM_RIGHT_KEYS.copy()

LEONTIEV_ALL_INTRO_KEYS = LEONTIEV_INTRO_RIGHT_KEYS.copy()

LEONTIEV_ALL_QUASI_KEYS = LEONTIEV_QUASI_RIGHT_KEYS.copy()

class ALL_LEONTIEV:
    def __init__(self):
        self.LEONTIEV_REFLEXIVITY_KEYS = LEONTIEV_REFLEXIVITY_KEYS
        self.LEONTIEV_DICT = LEONTIEV_DICT
        self.LEONTIEV_MAX_VAL = LEONTIEV_MAX_VAL
        self.LEONTIEV_CATEG = LEONTIEV_CATEG
        self.LEONTIEV_POINTS = LEONTIEV_POINTS
        self.LEONTIEV_ALL_SYSTEM_KEYS = LEONTIEV_ALL_SYSTEM_KEYS
        self.LEONTIEV_ALL_INTRO_KEYS = LEONTIEV_ALL_INTRO_KEYS
        self.LEONTIEV_ALL_QUASI_KEYS = LEONTIEV_ALL_QUASI_KEYS
