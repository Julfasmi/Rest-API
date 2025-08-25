import streamlit as st
import requests

st.title("🚀 FastAPI Test via Streamlit")

st.write("Masukkan ID dan data untuk berinteraksi dengan API.")

item_id = st.number_input("Item ID", min_value=1, step=1)
name = st.text_input("Name")
description = st.text_area("Description")
price = st.number_input("Price", min_value=0.0, step=0.1)

if st.button("Create Item"):
    data = {"name": name, "description": description, "price": price}
    res = requests.post(f"http://localhost:8000/items/{item_id}", json=data)
    st.json(res.json())

if st.button("Get Item"):
    res = requests.get(f"http://localhost:8000/items/{item_id}")
    st.json(res.json())
