import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from openpyxl import load_workbook

data1 = pd.read_excel("Data_excel.xlsx")
data2 = pd.read_csv("Data_csv.csv")
X = data2["X"]
y = data2["Y"]

# Title
st.title("Simple Linear Regression")

# Sidebar
with st.sidebar:
    sidebar_type = st.radio(
        "Choose Method",
        [
            "Raw Data",
            "Correlation",
            "Simple Linear Regression",
        ],
    )

if sidebar_type == "Raw Data":
    st.header("Data from Excel")
    st.dataframe(data1)

    st.write("X Variable is Poverty Depth Index")
    st.write("Y Variable is risk of residents being exposed to criminal acts")

elif sidebar_type == "Correlation":
    st.subheader("Correlation")

    value_correlation = np.corrcoef(X, y)[0][1]
    st.dataframe(data2.corr())
    st.write(
        "Coefficient of Correlation between X variable and Y variable is",
        value_correlation,
    )
