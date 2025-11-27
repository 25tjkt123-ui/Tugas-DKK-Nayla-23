import streamlit as st

st.title("Kalkulator Sederhana")

a = st.number_input("Angka 1")
b = st.number_input("Angka 2")
op = st.selectbox("Operasi", ["+", "-", "×", "÷"])

if st.button("Hitung"):
    if op == "+": st.success(a + b)
    elif op == "-": st.success(a - b)
    elif op == "×": st.success(a * b)
    elif op == "÷":
        st.success("Tidak bisa bagi 0!" if b == 0 else a / b)
