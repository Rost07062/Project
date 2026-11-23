#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:46:50 2026

@author: vboxuser
"""

import matplotlib.pyplot as plt
import pandas as pd
from defs.graph_defs import add_bar_labels
import math


class graph_work:
    def __init__(self, df, columns_to_plot=None, array_columns=None):
        self.df = df
        self.columns_to_plot = columns_to_plot if columns_to_plot is not None else list(df.columns)
        self.array_columns = array_columns if array_columns is not None else []

    def select(self, columns=None, indexes=None):
        df = self.df if indexes is None else self.df.iloc[indexes]
        columns = columns if columns is not None else self.columns_to_plot
        return graph_work(df, columns, self.array_columns)

    def _plot_column(self, col, ax):
        """Рисует график одного столбца в переданную ось ax."""
        if col in self.array_columns:
            exploded = self.df[col].explode().dropna()
            counts = exploded.value_counts().sort_index()
            counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
            add_bar_labels(ax)
            title = f'{col}\n(n={len(exploded)})'
            xlabel = 'Значение'
            rotate = True

        elif pd.api.types.is_numeric_dtype(self.df[col]):
            data = pd.to_numeric(self.df[col], errors='coerce').dropna()
            ax.hist(data, bins=15, color='steelblue', edgecolor='black', alpha=0.85)
            title = f'{col}\n(n={len(data)}, среднее={data.mean():.2f})'
            xlabel = 'Значение'
            rotate = False

        else:
            counts = self.df[col].value_counts()
            if len(counts) > 12:
                counts = counts.head(12)
                head = f'{col} (топ-12)'
            else:
                head = col
            counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
            add_bar_labels(ax)
            title = f'{head}\n(n={self.df[col].notna().sum()})'
            xlabel = 'Категория'
            rotate = True

        ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
        ax.set_xlabel(xlabel, fontsize=9)
        ax.set_ylabel('Количество', fontsize=9)
        if rotate:
            ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', alpha=0.3, linestyle='--')

    def hystogramm(self):
        """Каждый график на отдельной картинке (как раньше)."""
        for col in self.columns_to_plot:
            fig, ax = plt.subplots(figsize=(10, 6))
            self._plot_column(col, ax)
            plt.tight_layout()
            plt.show()

    def hystogramm_one_sheet(self, ncols=3, cell_size=(6, 4.5), save_path=None):
        """Все графики на одном листе в виде сетки."""
        n = len(self.columns_to_plot)
        nrows = math.ceil(n / ncols)

        fig, axes = plt.subplots(nrows, ncols,
                                 figsize=(cell_size[0] * ncols, cell_size[1] * nrows))
        axes = axes.flatten() if n > 1 else [axes]

        for ax, col in zip(axes, self.columns_to_plot):
            self._plot_column(col, ax)

        # скрыть пустые ячейки сетки
        for ax in axes[n:]:
            ax.set_visible(False)

        plt.tight_layout()
        if save_path:
            fig.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.show()