Natural Language to SQL Streamlit Application
Project Overview
This project is a Streamlit web application that translates natural language queries into SQL queries using OpenAI's GPT model. It enables users to interact with a SQL database more intuitively without needing to know SQL syntax. The application automatically converts the input from natural language to SQL, executes the query on a local SQL database, and displays the results.

Features
Natural Language Understanding: Converts user input from natural language to SQL queries.
Local Database Interaction: Executes queries on a local SQL database and displays results.
Log Queries: Maintains a log of all queries and their results for auditing purposes.
Installation
Prerequisites
Python 3.6 or newer
A local SQL Server database
An OpenAI API key
Steps
Clone this repository to your local machine:

git clone https://github.com/yourusername/openai-nl-to-sql-streamlit.git
Navigate into the project directory:

cd openai-nl-to-sql-streamlit
Install required Python libraries:
pip install -r requirements.txt
Create a .env file based on the .env.example template with your actual configuration values.
Usage
To run the Streamlit application:

streamlit run app.py
Enter your natural language query into the text input on the Streamlit interface and click the 'Convert and Execute' button to see the SQL query and its results.

Configuration
Ensure your .env file is set up correctly as per the .env.example file. It should contain your OpenAI API key and local SQL connection string.
