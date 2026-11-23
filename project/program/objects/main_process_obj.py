#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 02:18:29 2026

@author: vboxuser
"""
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

from defs.data_categ_defs import replace, make_demograph_dict, replace_children_categ
from defs.increasing_defs import summ_respondent, concatenate

from data.oishi_data import ALL_OISHI
from data.riff_data import ALL_RIFF
from data.diner_data import ALL_DINER
from data.maddi_data import ALL_MADDI
from data.leontiev_data import ALL_LEONTIEV
from data.tolerance_data import ALL_TOLERANCE

from data.demograph_data import DEMOGRAPH_CATEG, DEMOGRAPH_KEYS, HEALTH_KEYS

class main_work:
    def __init__(self):
        self.oishi = ALL_OISHI()
        self.riff = ALL_RIFF()
        self.diner = ALL_DINER()
        self.maddi = ALL_MADDI()
        self.leontiev = ALL_LEONTIEV()
        self.tolerance = ALL_TOLERANCE()
 
        self.ALL_CATEG = concatenate(self.oishi.OISHI_CATEG,
                                     self.riff.RIFF_CATEG,
                                     self.diner.DINER_CATEG,
                                     self.maddi.MADDI_CATEG,
                                     self.leontiev.LEONTIEV_CATEG,
                                     self.tolerance.TOLERANCE_CATEG)
 
        self.ALL_POINTS = [self.oishi.OISHI_POINTS, self.riff.RIFF_POINTS, self.diner.DINER_POINTS,
                           self.maddi.MADDI_POINTS, self.leontiev.LEONTIEV_POINTS,
                           self.tolerance.TOLERANCE_POINTS]
 
        self.ALL_KEYS = [
            [self.oishi.OISHI_ALL_PSYCH_RICH_KEYS],
            [self.riff.RIFF_ALL_AUTON_KEYS,
             self.riff.RIFF_ALL_COMPETENCE_KEYS,
             self.riff.RIFF_ALL_PERSON_GROWTH_KEYS,
             self.riff.RIFF_ALL_POSITIVE_RELATION_KEYS,
             self.riff.RIFF_ALL_LIFE_GOALS_KEYS,
             self.riff.RIFF_ALL_SELF_ACCEPT_KEYS,
             self.riff.RIFF_ALL_MAIN_KEYS],
            [self.diner.DINER_ALL_SATISFACTION_KEYS],
            [self.maddi.MADDI_ALL_ENGAMGEMENT_KEYS,
             self.maddi.MADDI_ALL_CONTROL_KEYS,
             self.maddi.MADDI_ALL_RISK_KEYS,
             self.maddi.MADDI_ALL_MAIN_KEYS],
            [self.leontiev.LEONTIEV_ALL_SYSTEM_KEYS,
             self.leontiev.LEONTIEV_ALL_INTRO_KEYS,
             self.leontiev.LEONTIEV_ALL_QUASI_KEYS],
            [self.tolerance.TOLERANCE_ALL_NEW_KEYS,
             self.tolerance.TOLERANCE_ALL_HARD_KEYS,
             self.tolerance.TOLERANCE_ALL_UNCERTAIN_KEYS,
             self.tolerance.TOLERANCE_ALL_PREFERENCE_KEYS,
             self.tolerance.TOLERANCE_ALL_TOLERANCE_KEYS,
             self.tolerance.TOLERANCE_ALL_MAIN_KEYS],
        ]

    def replace_values(self, respondents, count_strings):
        replace(respondents, count_strings, self.oishi.OISHI_PSYCH_RICH_KEYS, 
                self.oishi.OISHI_DICT, self.oishi.OISHI_REVERSE_KEYS, self.oishi.OISHI_MAX_VAL)

        replace(respondents, count_strings, self.riff.RIFF_PSYCH_WELL_BEING_KEYS, 
                self.riff.RIFF_DICT, np.concatenate([self.riff.RIFF_AUTON_REVERSE_KEYS, 
                                          self.riff.RIFF_COMPETENCE_REVERSE_KEYS, 
                                          self.riff.RIFF_LIFE_GOALS_REVRESE_KEYS, 
                                          self.riff.RIFF_PERSON_GROWTH_REVERSE_KEYS, 
                                          self.riff.RIFF_POSITIVE_RELATION_REVERSE_KEYS, 
                                          self.riff.RIFF_SELF_ACCEPT_REVRESE_KEYS]), 
                self.riff.RIFF_MAX_VAL)

        replace(respondents, count_strings, self.diner.DINER_SATISFACTION_KEYS, 
                self.diner.DINER_DICT, [], self.diner.DINER_MAX_VAL)

        replace(respondents, count_strings, self.maddi.MADDI_RESILIENCE_KEYS, 
                self.maddi.MADDI_DICT, np.concatenate([self.maddi.MADDI_CONTROL_REVERSE_KEYS,
                                            self.maddi.MADDI_ENGANGEMENT_REVERSE_KEYS,
                                            self.maddi.MADDI_RISK_REVERSE_KEYS]),
                self.maddi.MADDI_MAX_VAL)

        replace(respondents, count_strings, self.leontiev.LEONTIEV_REFLEXIVITY_KEYS, 
                self.leontiev.LEONTIEV_DICT, [], self.leontiev.LEONTIEV_MAX_VAL)

        replace(respondents, count_strings, self.tolerance.TOLERANCE_UNCERAIN_KEYS, 
                self.tolerance.TOLERANCE_DICT, self.tolerance.TOLERANCE_TOLERANCE_KEYS, self.tolerance.TOLERANCE_MAX_VAL)
        
    def summ_all_points(self, curr_string, count_tests, all_keys):
        count_keys = [len(i) for i in self.ALL_KEYS]
        all_points = []
        for i in range(count_tests):
            all_points.append([])
            curr_points = 0
            for j in range(count_keys[i]):
                curr_points = summ_respondent(curr_string, all_keys[i][j])
                all_points[-1].append(curr_points)
        return all_points
    
    def load_respondents(self, filename):
        main_df = pd.read_excel(filename)
        respondents = main_df.drop(0)
        work_df = respondents.copy()
        self.replace_values(work_df, len(respondents))
        return work_df
    
    
    def build_tables(self, work_df):
        count_strings = len(work_df)
        count_tests = len(self.ALL_POINTS)
    
        all_respondents = []
        demograph_table = []
    
        for string in range(count_strings):
            curr_string = work_df.iloc[string]
            all_respondents.append(self.summ_all_points(curr_string, count_tests, self.ALL_KEYS))
            demograph_table.append(
                make_demograph_dict(DEMOGRAPH_KEYS, HEALTH_KEYS, DEMOGRAPH_CATEG, curr_string)
            )
    
        pre_table = [
            [value for test in respondent for value in test]
            for respondent in all_respondents
        ]
    
        respondents_df = pd.DataFrame(pre_table, columns=self.ALL_CATEG)
    
        demograph_df = pd.DataFrame(demograph_table)
        demograph_df = demograph_df.drop(columns=demograph_df.columns[0])
        replace_children_categ(demograph_df, count_strings)
    
        return respondents_df, demograph_df
    
    
    
    def process_file(self, filename):
        work_df = self.load_respondents(filename)
        respondents_df, demograph_df = self.build_tables(work_df)
        return respondents_df, demograph_df

    def find_and_save_corr(self, data_df, file_corrs_pvalues):
        spear_corr = data_df.corr(method='spearman')
        all_cols = spear_corr.columns.tolist()
        
        results_df = spear_corr.loc[all_cols, all_cols].astype(str)
     

        for i in all_cols:
            for j in all_cols:
                if i != j:
                    x = data_df[i]
                    y = data_df[j]
                    
                    rho, p_value = spearmanr(x, y)
                    if p_value < 0.001:
                        significance = "*"
                    elif p_value < 0.01:
                        significance = "**"
                    elif p_value < 0.05:
                        significance = "***"
                    else:
                        significance = ""
        
                        
                    
                    results_df.loc[j, i] = f"{significance} {results_df.loc[j, i]}".strip()
        
        results_df.to_excel(f"{file_corrs_pvalues}.xlsx")