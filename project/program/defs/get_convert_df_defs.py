#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:28:02 2026

@author: vboxuser
"""
from defs.convert_defs import convert_defs
from functools import partial

def get_convert_df(respondents_df):
    conv_defs = convert_defs()
    
    converters = {
        "Психологически богатая жизнь": conv_defs.oishi_categ_def,
        "Удовлетворенность жизнью": conv_defs.diner_categ_def,
        
        "Автономность": partial(conv_defs.riff_categ_def, "Автономность"),
        "Компетентность": partial(conv_defs.riff_categ_def, "Компетентность"),
        "Личностный рост": partial(conv_defs.riff_categ_def, "Личностный рост"),
        "Позитивные отношения": partial(conv_defs.riff_categ_def, "Позитивные отношения"),
        "Жизненные цели": partial(conv_defs.riff_categ_def, "Жизненные цели"),
        "Самопринятие": partial(conv_defs.riff_categ_def, "Самопринятие"),
        "Интегральный показатель психологического благополучия": partial(conv_defs.riff_categ_def, "Интегральный показатель психологического благополучия"),
        "Системная рефлексия": partial(conv_defs.leontiev_categ_def, "Системная рефлексия"),
        "Интроспекция": partial(conv_defs.leontiev_categ_def, "Интроспекция"),
        "Квазирефлексия": partial(conv_defs.leontiev_categ_def, "Квазирефлексия"),
        "Вовлеченность": partial(conv_defs.maddi_categ_def, "Вовлеченность"),
        "Контроль": partial(conv_defs.maddi_categ_def, "Контроль"),
        "Принятие риска": partial(conv_defs.maddi_categ_def, "Принятие риска"),
        "Интегральный показатель жизнестойкости": partial(conv_defs.maddi_categ_def, "Интегральный показатель жизнестойкости"),
        "Отношение к новизне": partial(conv_defs.tolerance_categ_def, "Отношение к новизне"),
        "Отношение к сложным задачам": partial(conv_defs.tolerance_categ_def, "Отношение к сложным задачам"), 
        "Отношение к неопределённым ситуациям": partial(conv_defs.tolerance_categ_def, "Отношение к неопределённым ситуациям"),
        "Предпочтение неопределенности": partial(conv_defs.tolerance_categ_def, "Предпочтение неопределенности"),
        "Толерантность/избегание неопределенности": partial(conv_defs.tolerance_categ_def, "Толерантность/избегание неопределенности"), 
        "Интегральный показатель толерантности к неопределенности": partial(conv_defs.tolerance_categ_def, "Интегральный показатель толерантности к неопределенности")
     }
    
    convert_df = respondents_df.copy().astype(object)
    
    for col, func in converters.items():
        convert_df[col] = respondents_df[col].apply(func)
        
    return convert_df.astype(str)