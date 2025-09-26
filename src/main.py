import streamlit as st
from supabase import create_client, Client

@st.cache_resource
def init_connection():
    url = st.secrets["NEXT_PUBLIC_SUPABASE_URL"]
    key = st.secrets["NEXT_PUBLIC_SUPABASE_ANON_KEY"]
    return create_client(url, key)

supabase = init_connection()

@st.cache_data(ttl=600)

def run_query():
    return supabase.table("terminal_commands").select("*").execute()

rows = run_query()

for rows in rows.data:
    st.write(f"{rows}")