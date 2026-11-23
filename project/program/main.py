import pandas as pd

from defs.filter_defs import demograph_filter
from defs.get_convert_df_defs import get_convert_df

# from data.demograph_data import DEMOGRAPH_CATEG

from objects.main_process_obj import main_work
from objects.tree_process_obj import tree_work
from objects.graph_process_obj import graph_work




pd.set_option('display.float_format', lambda x: f'{x:.6f}')

FILENAME = "../2026-10-06 Опрос для диссертационного исследования.xlsx"



        
if __name__ == "__main__":

    process = main_work()
    
    respondents_df, demograph_df = process.process_file(FILENAME)
    
    
    process_tree = tree_work(demograph_df, respondents_df)
    
    
    filter_indexses, filter_respondents = demograph_filter(demograph_df, respondents_df)
    
    conv_resp = get_convert_df(respondents_df)
    conv_filt_resp = get_convert_df(filter_respondents)
    
    # gw = graph_work(
    #     demograph_df,
    #     columns_to_plot=[
    #         "Возраст", "Город", "Образование", DEMOGRAPH_CATEG[4],
    #         "Количество детей", "Возраст детей",
    #         "Уход за престарелыми или болеющими родственниками",
    #         "Ведет ли вы быт", "Профессиональный статус",
    #         "Есть ли хобби", "Состояние здоровья", "Посещает психолога",
    #     ],
    #     array_columns=["Состояние здоровья"]
    #     )
    # gw.hystogramm()
    
    # print(conv_resp.columns.tolist())
    
    
    # conv_graph = graph_work(
    #     conv_resp,
    #     columns_to_plot=conv_resp.columns.tolist(),
    #     array_columns=[])
    # conv_graph.hystogramm_one_sheet()
    
    conv_filt_graph = graph_work(
        conv_filt_resp,
        columns_to_plot=conv_filt_resp.columns.tolist(),
        array_columns=[])
    conv_filt_graph.hystogramm_one_sheet()
    
    # process_tree.create_tree()
