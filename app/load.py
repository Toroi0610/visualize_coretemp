# -*- coding: utf-8 -*-

import pandas as pd

class CoreTempLogLoader():

    def __init__(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path

    def set_datapath(self, file_path):
        self.file_path = file_path

    def get_dataframe(self):
        try:
            df = pd.read_csv(self.file_path, skiprows=8, encoding="utf-8")
        except:
            df = pd.read_csv(self.file_path, skiprows=8, encoding="shift-jis")
        df["Time"] = pd.to_datetime(df["Time"])
        return df

