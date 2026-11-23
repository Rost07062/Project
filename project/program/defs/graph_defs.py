#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:11:53 2026

@author: vboxuser
"""
import matplotlib.pyplot as plt

def make_oishi_hystogram(df):
    counts = df.value_counts()
    ax = counts.plot.bar(color='skyblue', edgecolor='black')

    ax.bar_label(ax.containers[0], fmt='%d', padding=3) 
    
    plt.title('Распределение строковых значений')
    plt.xlabel('Категории')
    plt.ylabel('Количество')
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    
    plt.show()



def add_bar_labels(ax, fontsize=9):
    """Подписывает значения над каждым столбцом"""
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(
                f'{int(height)}',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom',
                fontsize=fontsize, fontweight='bold'
            )

