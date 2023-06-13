import streamlit as st
import numpy as np
from scipy import stats

def main():
    st.title("Uji Hipotesis Varians dan Rata-rata Dua Populasi")

    # Input data
    st.header("Masukkan Data")
    data_pop1 = st.text_area("Data Populasi 1 (pisahkan dengan koma)")
    data_pop2 = st.text_area("Data Populasi 2 (pisahkan dengan koma)")

    # Convert input data to arrays
    try:
        data_pop1 = np.array([float(x.strip()) for x in data_pop1.split(",")])
        data_pop2 = np.array([float(x.strip()) for x in data_pop2.split(",")])
    except ValueError:
        st.warning("Masukkan data yang valid.")
        return

    # Perform hypothesis testing
    if st.button("Uji Hipotesis"):
        # Variance test
        st.subheader("Uji Hipotesis Varians")

        stat, p_value = stats.levene(data_pop1, data_pop2)
        st.write("Statistik Uji:", stat)
        st.write("Nilai p:", p_value)

        if p_value < 0.05:
            st.write("Kesimpulan: Varians dua populasi tidak sama.")
        else:
            st.write("Kesimpulan: Tidak ada bukti signifikan bahwa varians dua populasi berbeda.")

        # Mean test
        st.subheader("Uji Hipotesis Rata-rata")

        stat, p_value = stats.ttest_ind(data_pop1, data_pop2)
        st.write("Statistik Uji:", stat)
        st.write("Nilai p:", p_value)

        if p_value < 0.05:
            st.write("Kesimpulan: Rata-rata dua populasi berbeda secara signifikan.")
        else:
            st.write("Kesimpulan: Tidak ada bukti signifikan bahwa rata-rata dua populasi berbeda.")

if __name__ == "__main__":
    main()
