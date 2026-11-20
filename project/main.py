from scipy.stats import spearmanr
from sklearn.tree import DecisionTreeRegressor, plot_tree
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



pd.set_option('display.float_format', lambda x: f'{x:.6f}')

FILENAME = "2026-10-06 Опрос для диссертационного исследования.xlsx"


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

def hystogramm(array_columns, columns_to_plot):
    # ===== Рисуем каждый график на отдельной картинке =====
    for col in columns_to_plot:
        fig, ax = plt.subplots(figsize=(10, 6))
    
        if col in array_columns:
            # ===== СТОЛБЕЦ С МАССИВАМИ =====
            exploded = demograph_df[col].explode().dropna()
            counts = exploded.value_counts().sort_index()
            counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
            add_bar_labels(ax)
            ax.set_title(f'{col}\n(n={len(exploded)})', fontsize=14, fontweight='bold', pad=15)
            ax.set_ylabel('Количество', fontsize=12)
            ax.set_xlabel('Значение', fontsize=12)
            ax.tick_params(axis='x', rotation=45)
    
        elif pd.api.types.is_numeric_dtype(demograph_df[col]):
            # ===== ЧИСЛОВОЙ СТОЛБЕЦ =====
            data = pd.to_numeric(demograph_df[col], errors='coerce').dropna()
            ax.hist(data, bins=15, color='steelblue', edgecolor='black', alpha=0.85)
            ax.set_title(f'{col}\n(n={len(data)}, среднее={data.mean():.2f})',
                         fontsize=14, fontweight='bold', pad=15)
            ax.set_xlabel('Значение', fontsize=12)
            ax.set_ylabel('Количество', fontsize=12)
    
        else:
            # ===== КАТЕГОРИАЛЬНЫЙ СТОЛБЕЦ =====
            counts = demograph_df[col].value_counts()
            if len(counts) > 12:
                counts = counts.head(12)
                title = f'{col}\n(топ-12)'
            else:
                title = col
    
            counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
            add_bar_labels(ax)
            ax.set_title(f'{title}\n(n={demograph_df[col].notna().sum()})',
                         fontsize=14, fontweight='bold', pad=15)
            ax.set_ylabel('Количество', fontsize=12)
            ax.set_xlabel('Категория', fontsize=12)
            ax.tick_params(axis='x', rotation=45)
    
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        plt.show()
        
def find_and_save_corr(data_df, file_corrs_pvalues):
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
    
def increase(array, num):
    return [a + num for a in array]

def replace(array, strings, keys, values, reverse, max_values):
    for i in range(strings):
        row_label = array.index[i]
        for j in keys:
            if j in reverse:
                array.loc[row_label, j] = str(int(max_values) - int(values[array.loc[row_label, j]]))
            else:
                array.loc[row_label, j] = values[array.loc[row_label, j]]

def replace_values(respondents, count_strings):
    replace(respondents, count_strings, OISHI_PSYCH_RICH_KEYS, 
            OISHI_DICT, OISHI_REVERSE_KEYS, OISHI_MAX_VAL)

    replace(respondents, count_strings, RIFF_PSYCH_WELL_BEING_KEYS, 
            RIFF_DICT, np.concatenate([RIFF_AUTON_REVERSE_KEYS, 
                                      RIFF_COMPETENCE_REVERSE_KEYS, 
                                      RIFF_LIFE_GOALS_REVRESE_KEYS, 
                                      RIFF_PERSON_GROWTH_REVERSE_KEYS, 
                                      RIFF_POSITIVE_RELATION_REVERSE_KEYS, 
                                      RIFF_SELF_ACCEPT_REVRESE_KEYS]), 
            RIFF_MAX_VAL)

    replace(respondents, count_strings, DINER_SATISFACTION_KEYS, 
            DINER_DICT, [], DINER_MAX_VAL)

    replace(respondents, count_strings, MADDI_RESILIENCE_KEYS, 
            MADDI_DICT, np.concatenate([MADDI_CONTROL_REVERSE_KEYS,
                                        MADDI_ENGANGEMENT_REVERSE_KEYS,
                                        MADDI_RISK_REVERSE_KEYS]),
            MADDI_MAX_VAL)

    replace(respondents, count_strings, LEONTIEV_REFLEXIVITY_KEYS, 
            LEONTIEV_DICT, [], LEONTIEV_MAX_VAL)

    replace(respondents, count_strings, TOLERANCE_UNCERAIN_KEYS, 
            TOLERANCE_DICT, TOLERANCE_TOLERANCE_KEYS, TOLERANCE_MAX_VAL)

def concatenate(*array):
    main_array = []
    for i in array:
        main_array.append(i)
    return np.concatenate(main_array)


def summ_respondent(string, keys):
    return pd.to_numeric(string[keys]).sum()
        
def summ_all_points(curr_string, count_tests, all_keys):
    all_points = []
    for i in range(count_tests):
        all_points.append([])
        curr_points = 0
        for j in range(count_keys[i]):
            curr_points = summ_respondent(curr_string, all_keys[i][j])
            all_points[-1].append(curr_points)
    return all_points


def make_demograph_dict(keys, health_keys, demograph_categories, curr_string):
    demograph_dict = dict.fromkeys(demograph_categories, 0)
    health_array = []
    for i in keys:
        if i in health_keys and not(pd.isna(curr_string[i])):
            health_array.append(curr_string[i])
        elif not(health_array):
            demograph_dict[demograph_categories[i]] = curr_string[i]
        elif i not in health_keys:
            demograph_dict[demograph_categories[i - 1]] = health_array.copy()
            demograph_dict[demograph_categories[i]] = curr_string[i]
            health_array.clear()

    return demograph_dict


def replace_interpr(df, key, rows):
    for i in range(rows):
        curr = float(df.loc[i, key]) / 17
        if (curr > 5):
            df.loc[i, key] = 'Высокий балл'
        if (3.5 <= curr <= 5):
            df.loc[i, key] = 'Средний балл'
        if (curr < 3.5):
            df.loc[i, key] = 'Низкий балл'
            

def replace_children_categ(df, count_strings):
    """
    Категории: 0-2 Малыш
               3-6 Ребенок
               7-11 Доподросток
               12-17 Старшие подростки
               18-22 Студент
               >=23 Взрослый
    """
    categ_children = ["Малыш", "Ребенок", "Доподросток", "Подросток", "Студент", "Взрослый"]
    
    for i in range(count_strings):
        curr = list(map(lambda x: x.strip(), df.loc[i, "Возраст детей"].split(',')))
        if curr[0] != '-':
            curr = list(map(lambda x: 0 if "месяц" in x.lower() else(float(x.split()[0]) if "лет" in x.lower() else float(x)), curr))
            for j in range(len(curr)):
                curr_child = curr[j]
                if 0 <= curr_child <= 2:
                    curr[j] = categ_children[0]
                elif 3 <= curr_child <= 6:
                    curr[j] = categ_children[1]
                elif 7 <= curr_child <= 11:
                    curr[j] = categ_children[2]
                elif 12 <= curr_child <= 17:
                    curr[j] = categ_children[3]
                elif 18 <= curr_child <= 22:  
                    curr[j] = categ_children[4]
                else:
                    curr[j] = categ_children[5]
        df.loc[i, "Возраст детей"] = " ".join(sorted(list(set(curr))))
        
        
        
""" Демографическая анкета """
DEMOGRAPH_KEYS = np.array([i for i in range(1, 16)])

DEMOGRAPH_CATEG = ["", "Возраст", "Город", "Образование", 
                   "Cемейное положение", "Количество детей", "Возраст детей",
                   "Уход за престарелыми или болеющими родственниками",
                   "Ведет ли вы быт", "Профессиональный статус",
                   "Есть ли хобби", "Состояние здоровья", 
                   "Состояние здоровья", "Состояние здоровья", 
                   "Состояние здоровья", "Посещает психолога"]

HEALTH_KEYS = [i for i in range(11, 15)]





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




""" Тест жизнестойкости Мадди """
maddi_sdv = diner_sdv + len(DINER_SATISFACTION_KEYS)

MADDI_RESILIENCE_KEYS = np.array([i for i in range(92, 137)])

MADDI_MAX_VAL = 3
MADDI_DICT = {
    "Нет": "0",
    "Скорее нет, чем да": "1",
    "Скорее да, чем нет": "2",
    "Да": "3"}

MADDI_CATEG = ["Вовлеченность", "Контроль", "Принятие риска"]

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





ALL_CATEG = concatenate(OISHI_CATEG, 
                        RIFF_CATEG,
                        DINER_CATEG,
                        MADDI_CATEG, 
                        LEONTIEV_CATEG,
                        TOLERANCE_CATEG)


""" Заготовки гистограмм """
columns_to_plot = [
    "Возраст", "Город", "Образование", DEMOGRAPH_CATEG[4], 
    "Количество детей", "Возраст детей",
    "Уход за престарелыми или болеющими родственниками",
    "Ведет ли вы быт", "Профессиональный статус",
    "Есть ли хобби", "Состояние здоровья", "Посещает психолога"
]

# Столбцы с массивами (нужна распаковка)
array_columns = ["Состояние здоровья"]


""" Основная программа """

main_df = pd.read_excel(FILENAME)

respondents = main_df.drop(0);
count_strings = len(respondents)

work_df = respondents.copy()
replace_values(work_df, count_strings)

all_points = [OISHI_POINTS, RIFF_POINTS, DINER_POINTS, MADDI_POINTS, LEONTIEV_POINTS, TOLERANCE_POINTS]
all_keys = [[OISHI_ALL_PSYCH_RICH_KEYS], 
            [RIFF_ALL_AUTON_KEYS, 
             RIFF_ALL_COMPETENCE_KEYS, 
             RIFF_ALL_PERSON_GROWTH_KEYS, 
             RIFF_ALL_POSITIVE_RELATION_KEYS, 
             RIFF_ALL_LIFE_GOALS_KEYS,
             RIFF_ALL_SELF_ACCEPT_KEYS,
             RIFF_ALL_MAIN_KEYS], 
            [DINER_ALL_SATISFACTION_KEYS], 
            [MADDI_ALL_ENGAMGEMENT_KEYS,
             MADDI_ALL_CONTROL_KEYS,
             MADDI_ALL_RISK_KEYS],
            [LEONTIEV_ALL_SYSTEM_KEYS,
             LEONTIEV_ALL_INTRO_KEYS,
             LEONTIEV_ALL_QUASI_KEYS],
            [TOLERANCE_ALL_NEW_KEYS,
             TOLERANCE_ALL_HARD_KEYS,
             TOLERANCE_ALL_UNCERTAIN_KEYS,
             TOLERANCE_ALL_PREFERENCE_KEYS,
             TOLERANCE_ALL_TOLERANCE_KEYS,
             TOLERANCE_ALL_MAIN_KEYS]]

all_respondents = [None for _ in range(count_strings)]

count_keys = [len(i) for i in all_keys]
count_tests = len(all_points)
demograph_table = []

for string in range(count_strings):
    curr_string = work_df.iloc[string]
    all_respondents[string] = summ_all_points(curr_string, count_tests, all_keys)

    demograph_table.append(make_demograph_dict(DEMOGRAPH_KEYS, HEALTH_KEYS, DEMOGRAPH_CATEG, curr_string))
    
pre_table = []
for respondent in all_respondents:
    test_row = []
    for tests in respondent:
        test_row.extend(tests)
    pre_table.append(test_row)
    
    
respondents_df = pd.DataFrame(pre_table, columns=ALL_CATEG)
demograph_df = pd.DataFrame(demograph_table)
demograph_df = demograph_df.drop(columns=demograph_df.columns[0])
replace_children_categ(demograph_df, count_strings)

oishi_categ = respondents_df.copy().astype(str)

replace_interpr(oishi_categ, "Психологически богатая жизнь", count_strings)

OISHI_INTERPR = oishi_categ["Психологически богатая жизнь"]
        
demograph_filter = demograph_df[(pd.to_numeric(demograph_df['Возраст']).between(40, 55)) &
            (demograph_df['Профессиональный статус'].str.contains("Работаю по найму", case=False, na=False))&
            (demograph_df['Количество детей'].isin(["1", "2"]))& # 6 человек отметается когда убираю "Нет детей"
            (demograph_df['Ведет ли вы быт'].str.contains('Да', case=False, na=False))
            ]

filter_indexses = demograph_filter.index.tolist()

filter_respondents = respondents_df.iloc[filter_indexses]

filter_oishi_interpr = OISHI_INTERPR.iloc[filter_indexses]

make_oishi_hystogram(filter_oishi_interpr)
make_oishi_hystogram(OISHI_INTERPR)

hystogramm(demograph_df, demograph_df.columns)
find_and_save_corr(filter_respondents, "Сводки_корреляций_к_значимости_с_фильтром")
find_and_save_corr(respondents_df, "Сводки_корреляций_к_значимости_без_фильтра")


""" Работа с деревом """

ALL_DATA = pd.concat([demograph_df, respondents_df], axis=1)
ALL_DATA["Состояние здоровья"] = ALL_DATA["Состояние здоровья"].str.join(" ")
# replace_children_categ(ALL_DATA, count_strings)
X = ALL_DATA[demograph_df.columns]
X_encoded = pd.get_dummies(X, drop_first=True)

Y = ALL_DATA["Интегральный показатель психологического благополучия"]

model = DecisionTreeRegressor(max_depth=7, random_state=42)
model.fit(X_encoded, Y)



plt.figure(figsize=(25, 15))
plot_tree(
    model, 
    feature_names=X_encoded.columns,
    filled=True,       # Цвет зависит от среднего значения (чем темнее, тем выше/ниже средний результат)
    rounded=True,
    fontsize=6,
    impurity=False,    # Можно отключить дисперсию, чтобы не загромождать
    proportion=False   # Отключаем доли объектов
)
plt.title("Дерево регрессии: как категории влияют на результат теста")

plt.show()
plt.close('all')

