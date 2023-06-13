import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_excel("Data.xlsx", sheet_name="Sheet2")
X = data["X"]
y = data["Y"]

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
    st.dataframe(data)

    st.write("X Variable is Poverty Depth Index")
    st.write("Y Variable is risk of residents being exposed to criminal acts")

elif sidebar_type == "Correlation":
    st.subheader("Correlation")

    value_correlation = np.corrcoef(X, y)[0][1]
    st.dataframe(data.corr())
    st.write(
        "Coefficient of Correlation between X variable and Y variable is",
        value_correlation,
    )

elif sidebar_type == "Simple Linear Regression":
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=23
    )

    X_train = np.array(X_train).reshape(-1, 1)
    X_test = np.array(X_test).reshape(-1, 1)

    from sklearn.linear_model import LinearRegression

    slr = LinearRegression()
    slr.fit(X_train, y_train)

    y_predict_train = slr.predict(X_train)
    import matplotlib.pyplot as plt

    plt.scatter(X_train, y_train)
    plt.plot(X_train, y_predict_train, color="black")
    plt.xlabel("Indeks Kedalaman Kemiskinan")
    plt.ylabel("Risiko Penduduk Terkena Tindak Pidana")
