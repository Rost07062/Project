#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:24:31 2026

@author: vboxuser
"""
import numpy as np
from data.oishi_data import oishi_sdv, OISHI_PSYCH_RICH_KEYS
from defs.increasing_defs import increase, concatenate

""" Шкала психологического благополучия Рифф """
riff_sdv = oishi_sdv + len(OISHI_PSYCH_RICH_KEYS)

RIFF_PSYCH_WELL_BEING_KEYS = np.array([i for i in range(33, 87)])

RIFF_MAX_VAL = 6
RIFF_DICT = {
    "Совершенно согласна": "5",
    "Согласна": "4",
    "Сложно сказать, и согласна, и нет": "3",
    "Не согласна": "2",
    "Категорически не согласна": "1"}

RIFF_CATEG = ["Автономность", "Компетентность", "Личностный рост", 
              "Позитивные отношения", "Жизненные цели", "Самопринятие",
              "Интегральный показатель психологического благополучия"]

RIFF_POINTS = np.array([0 for _ in range(len(RIFF_CATEG))])

RIFF_AUTON_REVERSE_KEYS = np.array([8, 15, 36, 52])
RIFF_AUTON_RIGHT_KEYS = np.array([1, 7, 22, 29, 54])

RIFF_COMPETENCE_REVERSE_KEYS = np.array([9, 16, 23, 46, 50])
RIFF_COMPETENCE_RIGHT_KEYS = np.array([2, 14, 30, 37])

RIFF_PERSON_GROWTH_REVERSE_KEYS = np.array([17, 24, 31, 51])
RIFF_PERSON_GROWTH_RIGHT_KEYS = np.array([3, 10, 21, 38, 43])

RIFF_POSITIVE_RELATION_REVERSE_KEYS = np.array([4, 18, 25, 47, 53])
RIFF_POSITIVE_RELATION_RIGHT_KEYS = np.array([11, 28, 32, 39])

RIFF_LIFE_GOALS_REVRESE_KEYS = np.array([12, 33, 40, 48])
RIFF_LIFE_GOALS_RIGHT_KEYS = np.array([5, 19, 26, 35, 45])

RIFF_SELF_ACCEPT_REVRESE_KEYS = np.array([6, 27, 42, 44])
RIFF_SELF_ACCEPT_RIGHT_KEYS = np.array([13, 20, 34, 41, 49])


RIFF_AUTON_REVERSE_KEYS, RIFF_AUTON_RIGHT_KEYS,\
RIFF_COMPETENCE_REVERSE_KEYS, RIFF_COMPETENCE_RIGHT_KEYS,\
RIFF_PERSON_GROWTH_REVERSE_KEYS, RIFF_PERSON_GROWTH_RIGHT_KEYS,\
RIFF_POSITIVE_RELATION_REVERSE_KEYS, RIFF_POSITIVE_RELATION_RIGHT_KEYS,\
RIFF_LIFE_GOALS_REVRESE_KEYS, RIFF_LIFE_GOALS_RIGHT_KEYS,\
RIFF_SELF_ACCEPT_REVRESE_KEYS, RIFF_SELF_ACCEPT_RIGHT_KEYS = increase([RIFF_AUTON_REVERSE_KEYS, 
                                                                       RIFF_AUTON_RIGHT_KEYS, RIFF_COMPETENCE_REVERSE_KEYS, 
                                                                       RIFF_COMPETENCE_RIGHT_KEYS, RIFF_PERSON_GROWTH_REVERSE_KEYS, 
                                                                       RIFF_PERSON_GROWTH_RIGHT_KEYS, RIFF_POSITIVE_RELATION_REVERSE_KEYS, 
                                                                       RIFF_POSITIVE_RELATION_RIGHT_KEYS, 
                                                                       RIFF_LIFE_GOALS_REVRESE_KEYS, RIFF_LIFE_GOALS_RIGHT_KEYS, 
                                                                       RIFF_SELF_ACCEPT_REVRESE_KEYS, RIFF_SELF_ACCEPT_RIGHT_KEYS], riff_sdv)


RIFF_ALL_AUTON_KEYS = concatenate(RIFF_AUTON_REVERSE_KEYS, RIFF_AUTON_RIGHT_KEYS)

RIFF_ALL_COMPETENCE_KEYS = concatenate(RIFF_COMPETENCE_REVERSE_KEYS, RIFF_COMPETENCE_RIGHT_KEYS)

RIFF_ALL_PERSON_GROWTH_KEYS = concatenate(RIFF_PERSON_GROWTH_REVERSE_KEYS, RIFF_PERSON_GROWTH_RIGHT_KEYS)

RIFF_ALL_POSITIVE_RELATION_KEYS = concatenate(RIFF_POSITIVE_RELATION_REVERSE_KEYS, RIFF_POSITIVE_RELATION_RIGHT_KEYS)

RIFF_ALL_LIFE_GOALS_KEYS = concatenate(RIFF_LIFE_GOALS_REVRESE_KEYS, RIFF_LIFE_GOALS_RIGHT_KEYS)

RIFF_ALL_SELF_ACCEPT_KEYS = concatenate(RIFF_SELF_ACCEPT_REVRESE_KEYS, RIFF_SELF_ACCEPT_RIGHT_KEYS)

RIFF_ALL_MAIN_KEYS = RIFF_PSYCH_WELL_BEING_KEYS.copy()

class ALL_RIFF:
    def __init__(self):
        self.RIFF_PSYCH_WELL_BEING_KEYS = RIFF_PSYCH_WELL_BEING_KEYS
        self.RIFF_DICT = RIFF_DICT
        self.RIFF_AUTON_REVERSE_KEYS = RIFF_AUTON_REVERSE_KEYS
        self.RIFF_COMPETENCE_REVERSE_KEYS = RIFF_COMPETENCE_REVERSE_KEYS
        self.RIFF_LIFE_GOALS_REVRESE_KEYS = RIFF_LIFE_GOALS_REVRESE_KEYS
        self.RIFF_PERSON_GROWTH_REVERSE_KEYS = RIFF_PERSON_GROWTH_REVERSE_KEYS
        self.RIFF_POSITIVE_RELATION_REVERSE_KEYS = RIFF_POSITIVE_RELATION_REVERSE_KEYS
        self.RIFF_SELF_ACCEPT_REVRESE_KEYS = RIFF_SELF_ACCEPT_REVRESE_KEYS
        self.RIFF_MAX_VAL = RIFF_MAX_VAL
        self.RIFF_CATEG = RIFF_CATEG
        self.RIFF_POINTS = RIFF_POINTS
        self.RIFF_ALL_AUTON_KEYS = RIFF_ALL_AUTON_KEYS
        self.RIFF_ALL_COMPETENCE_KEYS = RIFF_ALL_COMPETENCE_KEYS
        self.RIFF_ALL_PERSON_GROWTH_KEYS = RIFF_ALL_PERSON_GROWTH_KEYS
        self.RIFF_ALL_POSITIVE_RELATION_KEYS = RIFF_ALL_POSITIVE_RELATION_KEYS
        self.RIFF_ALL_LIFE_GOALS_KEYS = RIFF_ALL_LIFE_GOALS_KEYS
        self.RIFF_ALL_SELF_ACCEPT_KEYS = RIFF_ALL_SELF_ACCEPT_KEYS
        self.RIFF_ALL_MAIN_KEYS = RIFF_ALL_MAIN_KEYS

