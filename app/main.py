import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar Data Dashboard")

country = st.selectbox("Select Country", ["Benin", "Togo", "Sierra Leone"])
data = pd.read_csv(f"../data/{country.lower().replace(' ', '_')}_clean.csv")

st.write(f"Data Preview - {country}")
st.dataframe(data.head())

st.subheader("GHI Distribution")
fig, ax = plt.subplots()
sns.histplot(data['GHI'], kde=True, ax=ax)
st.pyplot(fig)
