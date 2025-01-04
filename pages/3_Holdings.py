import streamlit as st
import pymysql
import pandas as pd

st.set_page_config(page_title="Holdings", page_icon="📈")

st.markdown("# Holdings")
st.sidebar.header("Holdings")
st.write(
    """This Holdings page illustrates a combination of plotting and animation with
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
query2 =  """
SELECT UsrId, TckrSymb, SUM(Qty), AVG(AvgPric), Avg(CurValue), Avg(PNL) FROM LATEST_HOLDINGS
GROUP BY TckrSymb, UsrId
"""
#cur.execute("SELECT * from TRADES")

# Fetch one result
result_dataFrame2 = pd.read_sql(query2,cnx)

st.write(result_dataFrame2)

if st.checkbox('Show detailed'):
    # Execute a query
    query = """
    SELECT * FROM LATEST_HOLDINGS
    """
    # cur.execute("SELECT * from TRADES")

    # Fetch one result
    result_dataFrame = pd.read_sql(query, cnx)

    st.write(result_dataFrame)

# Close connection
cnx.close()
