import streamlit as st
from st_supabase_connection import SupabaseConnection

# Init connecttion
conn = st.connection(
    name="supabase", 
    type=SupabaseConnection,
    url=st.secrets["connections"]["supabase"]["NEXT_PUBLIC_SUPABASE_URL"],
    key=st.secrets["connections"]["supabase"]["NEXT_PUBLIC_SUPABASE_ANON_KEY"]
)

rows = conn.query("*", table="terminal_commands", ttl="10m").execute()

for row in rows.data:
    st.write(f"Command: {row}")

