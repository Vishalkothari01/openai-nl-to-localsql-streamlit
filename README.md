# Natural Language to SQL Streamlit App using OpenAI's GPT-3 model

## Description
This project is a Streamlit web application that translates natural language queries into SQL queries using OpenAI's GPT-3 model and executes them on a local SQL database. It's designed to simplify database interactions, making it easier for users without deep SQL knowledge to retrieve data using natural language.

## Features
- Natural language understanding to generate SQL queries.
- Execution of SQL queries on a local SQL database.
- Display of query results within the Streamlit UI.
- Logging of queries and results for auditing purposes.

## Installation

### Prerequisites
- Python 3.8+
- An OpenAI API key
- A local SQL database (SQL Server)
- ODBC driver for your SQL database

### Setup

1. Clone this repository:
git clone https://github.com/yourusername/openai-nl-to-sql-streamlit.git

2. Navigate to the project directory:
cd openai-nl-to-sql-streamlit

3. Install required Python packages:
pip install -r requirements.txt

4. Configure your `.env` file based on the `.env.example` provided in the repository. Update the `OPENAI_API_KEY` and `LOCAL_SQL_CONNECTION_STRING` with your details.

### Running the Application

1. Start the Streamlit app:
streamlit run app.py

2. Open your web browser and go to the address shown in the terminal to interact with the application.

## Usage
- Upon launching the app, you'll see a text input where you can type your natural language query.
- After inputting your query, click the "Convert and Execute" button. The app will display the generated SQL query and the results of its execution.

