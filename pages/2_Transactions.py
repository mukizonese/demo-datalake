import streamlit as st
import pymysql
import pandas as pd

st.set_page_config(page_title="Transactions", page_icon="📈")

st.markdown("# Transactions")
st.sidebar.header("Transactions")
st.write(
    """This Transactions page illustrates a combination of plotting and animation with
Streamlit. !"""
)

# Connect to server
cnx = pymysql.connect(
    host="localhost",
#    host="host.docker.internal",
    port=3306,
    user="tradedb_usr",
    password="tradedb_usr",
    database='tradedb')

# Get a cursor
cur = cnx.cursor()

# Execute a query
query =  "SELECT * from HOLDINGS"
#cur.execute("SELECT * from TRADES")

# Fetch one result
result_dataFrame = pd.read_sql(query,cnx)

st.write(result_dataFrame)

# Close connection
cnx.close()
