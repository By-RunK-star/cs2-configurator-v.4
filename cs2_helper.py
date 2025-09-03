import pandas as pd
import streamlit as st

# Загружаем базу сборок
@st.cache_data
def load_data():
    return pd.read_csv("builds.csv")

df = load_data()

# Интерфейс
st.title("⚙️ Конфигуратор CS2")
st.write("Выбери свой ПК и получи готовые настройки для CS2!")

cpu = st.selectbox("Выбери процессор:", sorted(df["CPU"].unique()))
gpu = st.selectbox("Выбери видеокарту:", sorted(df["GPU"].unique()))
ram = st.selectbox("Выбери объём ОЗУ:", sorted(df["RAM"].unique()))

if st.button("Найти настройки"):
    result = df[
        (df["CPU"] == cpu) &
        (df["GPU"] == gpu) &
        (df["RAM"] == ram)
    ]
    if not result.empty:
        st.subheader("✅ Рекомендованные настройки")
        st.write(result.to_dict(orient="records")[0])
    else:
        st.error("❌ Подходящей конфигурации не найдено.")
