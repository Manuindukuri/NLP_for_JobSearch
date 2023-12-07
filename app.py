import os
import openai
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from snowflake.connector import connect
from snowflake.snowpark.session import Session

# Load environment variables from the .env file
load_dotenv()

# Environment Variables
snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
snowflake_user = os.getenv("SNOWFLAKE_USER")
snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
snowflake_table = os.getenv("SNOWFLAKE_TABLE")
snowflake_role = os.getenv("SNOWFLAKE_ROLE")

# Function to establish a connection to Snowflake
def get_snowflake_connection():
    return connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        database=snowflake_database,
        role=snowflake_role
    )

# Create a connection
conn = get_snowflake_connection()

# Create a cursor
cursor = conn.cursor()

# Define a SQL query
query = f"""
SELECT *
FROM {snowflake_table};
"""

# Execute the query and convert the result to a Pandas dataframe
cursor.execute(query)
df = cursor.fetch_pandas_all()

# Add Streamlit features to your app to display the results of your query
st.dataframe(df)

# Close the cursor and connection
cursor.close()
conn.close()
