import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Editar_espectro:
    def __init__(self, data_frame):
        self.data_frame = data_frame


    def get_non_lectures(self):
        seled = []

        for i in self.data_frame.columns.tolist():
            try:
                int(i)
            except:
                seled.append(str(i))
        
        df_to_ret = self.data_frame[seled]

        return df_to_ret

    def get_raw_cut(self, tuple_of_cut):
        
        lambdas = []
        seled = []

        for i in self.data_frame.columns.tolist():
            try:
                lambdas.append(int(i))
            except:
                #print(f"Omitiendo {i}")
                pass
        
        for lam in lambdas:
            if lam >= min(tuple_of_cut) and lam <= max(tuple_of_cut):
                seled.append(str(lam))

        del lambdas

        df_to_ret = self.data_frame[seled]
        return df_to_ret


    def get_cut(self, tuple_of_cut, modif = True):
        lambdas = []
        seled = []

        for i in self.data_frame.columns.tolist():
            try:
                lambdas.append(int(i))
            except:
                seled.append(str(i))
        
        for lam in lambdas:
            if lam >= min(tuple_of_cut) and lam <= max(tuple_of_cut):
                seled.append(str(lam))

        del lambdas
        df_to_ret = self.data_frame[seled]

        if modif:
            self.data_frame = df_to_ret

        return df_to_ret


    def get_multiple_cuts(self, tuple_of_tuples, modif = True):
        df_to_ret = self.get_non_lectures()
        
        
        for tup in tuple_of_tuples:
            cut = self.get_raw_cut(tup)
            df_to_ret = pd.concat([df_to_ret, cut], axis=1)

        if modif:
            self.data_frame = df_to_ret

        return df_to_ret


    def save_csv(self, filename):
        self.data_frame.to_csv(filename, sep=',', index=False, encoding='utf-8')
