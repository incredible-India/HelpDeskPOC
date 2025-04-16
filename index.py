import psycopg2
import os
from groq import Groq
# from . import roll
# Database connection
conn = psycopg2.connect(
    dbname="School",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cur = conn.cursor()

# Groq API setup
client = Groq(api_key="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")

# Function to generate SQL dynamically using Groq
def generate_sql(question):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Write a PostgreSQL SQL query (only Query no other words in chat answer) to answer this question: '{question}'",
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        sql_query = chat_completion.choices[0].message.content.strip()

        # Handling triple quotes if present
        if sql_query.startswith('"""') and sql_query.endswith('"""'):
            sql_query = sql_query.strip('"""').strip()

        return sql_query
    except Exception as e:
        return f"Error generating SQL: {e}"

# Function to execute the SQL query
def execute_query(sql_query):
    try:
        cur.execute(sql_query)
        result = cur.fetchall()
        return result if result else "No data found."
    except Exception as e:
        return f"Error executing query: {e}"

# Main chatbot loop
def chat():
    print("Hello! I'm your dynamic SQL chatbot using Groq. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Generate SQL
        sql_query = generate_sql(user_input)
        
        # Display SQL query in a formatted way
        print(f"\nGenerated SQL Query:\n```sql\n{sql_query}\n```")
        
        # Execute query
        result = execute_query(sql_query)
        
        # Display results
        if isinstance(result, list):
            print("\nChatbot Results:")
            for idx, row in enumerate(result, 1):
                print(f"{idx}. {row}")
        else:
            print("Chatbot:", result)

if __name__ == '__main__':
    import retrive
    import originalModel
