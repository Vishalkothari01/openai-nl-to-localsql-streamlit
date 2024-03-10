import streamlit as st
import openai
from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import dotenv_values
import datetime

# Load configuration
config = dotenv_values(".env")

# Initialize OpenAI with API key
openai.api_key = config["OPENAI_API_KEY"]

# Setup database connection
engine = create_engine(config["LOCAL_SQL_CONNECTION_STRING"])

def execute_sql_query(sql_query):
    """Execute SQL query and return results."""
    with engine.connect() as connection:
        result = connection.execute(text(sql_query))
        # Assuming the query returns rows, adjust as needed for your use case
        return result.fetchall()

def generate_sql_query(nl_query):
    """Translate natural language query to SQL using OpenAI."""
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Write a SQL query to {nl_query}.",
            temperature=0.5,
            max_tokens=150
        )
        full_response = response.choices[0].text.strip()
        # Basic processing to extract SQL query - this may need to be more sophisticated
        sql_query = full_response.split('\n\n')[0]  # Assumes the SQL query is before the first double newline
        return sql_query
    except Exception as e:
        return f"Error generating SQL query: {e}"

# Execute the SQL query part (use your existing execution logic)

# Streamlit interface
st.title('Natural Language to SQL')
nl_query = st.text_input("Enter your natural language query:")

if st.button('Convert and Execute'):
    if nl_query:
        # Generate SQL from natural language query
        sql_query = generate_sql_query(nl_query)
        
        if sql_query.startswith("Error"):
            st.write(sql_query)  # Show error in generating SQL
        else:
            st.text(f"Generated SQL: {sql_query}")
            
            # Execute generated SQL query
            try:
                results = execute_sql_query(sql_query)
                st.write("Query Results:", results)
                
                # Optional: Log query and result
                with open("query_logs.txt", "a") as log_file:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_file.write(f"Timestamp: {timestamp}\nNL Query: {nl_query}\nGenerated SQL: {sql_query}\nResults: {results}\n\n")
            except Exception as e:
                st.write(f"Error executing SQL query: {e}")
    else:
        st.write("Please enter a query.")
