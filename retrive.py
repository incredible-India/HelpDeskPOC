
import psycopg2
import csv

# Database connection
conn = psycopg2.connect(
    dbname="School",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)
cur = conn.cursor()

# Function to fetch data from the database
def fetch_data(query):
    try:
        cur.execute(query)
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Function to write data to CSV
def write_to_csv(data, column_names, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # Write header
        writer.writerows(data)         # Write data
    print(f"Db connection successfully \n reading data from tables..")

# Main function
def export_data():
    for table_name in ["Students","Teachers","Marks"]:

        query = f"SELECT * FROM {table_name};"

        # Fetch data
        data = fetch_data(query)
        if data:
            # Get column names
            cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
            columns = [col[0] for col in cur.fetchall()]

            # Export to CSV
            filename = f"./assets/{table_name}_data.csv"
            write_to_csv(data, columns, filename)
        else:
            print("No data found or error in query.")


export_data()
