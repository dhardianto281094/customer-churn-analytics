import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_overview():
    st.title("📊 Telco Churn Overview")
    st.write("Insight pelanggan berdasarkan data yang telah dieksplorasi.")

    # Ganti dengan link raw dari GitHub
    url = "https://raw.githubusercontent.com/dhardianto281094/customer-churn-analytics/main/telco_customer_churn_final.csv"
    df = pd.read_csv(url)

    st.subheader("Distribusi Churn")
    churn_counts = df['Churn'].value_counts()
    st.bar_chart(churn_counts)

    st.subheader("Distribusi berdasarkan Gender")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Gender', hue='Churn', ax=ax)
    st.pyplot(fig)

    st.subheader("Pelanggan berdasarkan Internet Type")
    st.bar_chart(df['Internettype'].value_counts())
