#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:26:38 2026

@author: vboxuser
"""
import numpy as np

from data.diner_data import diner_sdv, DINER_SATISFACTION_KEYS
from defs.increasing_defs import concatenate, increase

""" Тест жизнестойкости Мадди """
maddi_sdv = diner_sdv + len(DINER_SATISFACTION_KEYS)

MADDI_RESILIENCE_KEYS = np.array([i for i in range(92, 137)])

MADDI_MAX_VAL = 3
MADDI_DICT = {
    "Нет": "0",
    "Скорее нет, чем да": "1",
    "Скорее да, чем нет": "2",
    "Да": "3"}

MADDI_CATEG = ["Вовлеченность", "Контроль", "Принятие риска", "Интегральный показатель жизнестойкости"]

MADDI_POINTS = np.array([0 for _ in range(len(MADDI_CATEG))])

MADDI_ENGANGEMENT_REVERSE_KEYS = np.array([2, 3, 10, 11, 14, 28, 32, 37, 38, 40, 42])
MADDI_ENGANGEMENT_RIGHT_KEYS = np.array([4, 12, 22, 23, 24, 29,
41])

MADDI_CONTROL_REVERSE_KEYS = np.array([1, 5, 6, 8, 16, 20, 27, 31,
35, 39, 43])
MADDI_CONTROL_RIGHT_KEYS = np.array([9, 15, 17, 21, 25, 44])

MADDI_RISK_REVERSE_KEYS = np.array([7, 13, 18, 19, 26, 30,
33, 36])
MADDI_RISK_RIGHT_KEYS = np.array([34, 45])

MADDI_ENGANGEMENT_REVERSE_KEYS, MADDI_ENGANGEMENT_RIGHT_KEYS,\
MADDI_CONTROL_REVERSE_KEYS, MADDI_CONTROL_RIGHT_KEYS,\
MADDI_RISK_REVERSE_KEYS, MADDI_RISK_RIGHT_KEYS = increase([MADDI_ENGANGEMENT_REVERSE_KEYS, MADDI_ENGANGEMENT_RIGHT_KEYS,
                                                           MADDI_CONTROL_REVERSE_KEYS, MADDI_CONTROL_RIGHT_KEYS, 
                                                           MADDI_RISK_REVERSE_KEYS, MADDI_RISK_RIGHT_KEYS], maddi_sdv)

MADDI_ALL_ENGAMGEMENT_KEYS = concatenate(MADDI_ENGANGEMENT_REVERSE_KEYS, MADDI_ENGANGEMENT_RIGHT_KEYS)

MADDI_ALL_CONTROL_KEYS = concatenate(MADDI_CONTROL_REVERSE_KEYS, MADDI_CONTROL_RIGHT_KEYS)

MADDI_ALL_RISK_KEYS = concatenate(MADDI_RISK_REVERSE_KEYS, MADDI_RISK_RIGHT_KEYS)

MADDI_ALL_MAIN_KEYS = concatenate(MADDI_ALL_ENGAMGEMENT_KEYS, MADDI_ALL_CONTROL_KEYS, MADDI_ALL_RISK_KEYS)

class ALL_MADDI:
    def __init__(self):
        self.MADDI_RESILIENCE_KEYS = MADDI_RESILIENCE_KEYS
        self.MADDI_DICT = MADDI_DICT
        self.MADDI_CONTROL_REVERSE_KEYS = MADDI_CONTROL_REVERSE_KEYS
        self.MADDI_ENGANGEMENT_REVERSE_KEYS = MADDI_ENGANGEMENT_REVERSE_KEYS
        self.MADDI_RISK_REVERSE_KEYS = MADDI_RISK_REVERSE_KEYS
        self.MADDI_MAX_VAL = MADDI_MAX_VAL
        self.MADDI_CATEG = MADDI_CATEG
        self.MADDI_POINTS = MADDI_POINTS
        self.MADDI_ALL_ENGAMGEMENT_KEYS = MADDI_ALL_ENGAMGEMENT_KEYS
        self.MADDI_ALL_CONTROL_KEYS = MADDI_ALL_CONTROL_KEYS
        self.MADDI_ALL_RISK_KEYS = MADDI_ALL_RISK_KEYS
        self.MADDI_ALL_MAIN_KEYS = MADDI_ALL_MAIN_KEYS

