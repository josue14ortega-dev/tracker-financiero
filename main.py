import streamlit as st
from supabase import create_client

url = st.secrets['SUPABASE_URL'] 
key = st.secrets['SUPABASE_KEY']
supabase = create_client(url, key)

def cargar_datos():
    respuesta = supabase.table('transacciones').select('*').execute()
    return respuesta.data


def guardar_datos(transaccion):
    respuesta = supabase.table('transacciones').insert(transaccion).execute()
    return respuesta