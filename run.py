# -*- coding: utf-8 -*-

import streamlit as st
import plotly.express as px

from app.load import CoreTempLogLoader

ctll = CoreTempLogLoader()
ctll.set_datapath("log_coretemp/CT-Log 2020-11-02 22-14-57.csv")
df = ctll.get_dataframe()

# Temp Chart
temp_columns = df.columns[["Temp" in col for col in df.columns]]
temp_fig = px.line(df,
                   x="Time",
                   y=temp_columns,
                   title="Core Temp (C)"
                   )

st.plotly_chart(temp_fig)

# CPU Power Chart
cpu_power_fig = px.area(df,
                        x="Time",
                        y=['CPU 0 Power'],
                        title="CPU Power (W)"
                        )

st.plotly_chart(cpu_power_fig)

