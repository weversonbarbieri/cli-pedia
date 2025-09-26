import streamlit as st
from st_supabase_connection import SupabaseConnection

# Init connecttion
conn = st.connection("supabase", type=SupabaseConnection)

rows = conn.query("*", table="terminal_commands", ttl="10m").execute()

for row in rows.data:
    st.write(f"{row['name']} has a : {row['pet']}:")

