import gspread
import mysql.connector

# Google Sheets credentials
sheet_key = ''    # Specify the key of the Google Sheets document
credentials_file = ''    # Specify the path to the credentials file
sheet_name = ''    # Specify the name of the sheet within the Google Sheets document

# MySQL server credentials
mysql_host = ''    # Specify the MySQL server address
mysql_user = ''    # Specify the MySQL username
mysql_password = ''    # Specify the MySQL password
mysql_database = ''    # Specify the name of the MySQL database

def insert_data_from_sheet_to_mysql():

    # Connect to Google Sheets
    gc = gspread.service_account(filename=credentials_file)
    sheet = gc.open_by_key(sheet_key).worksheet(sheet_name)

    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    # Get data from Google Sheets
    data = sheet.get_all_values()
    
    # Insert data into MySQL server
    for row in data[1:]:
        column1 = row[1]
        column2 = row[2]
        # Define other columns similarly for all your fields

        # Construct the SQL query
        sql = "INSERT INTO tableName (column1, column2) VALUES (%s, %s)"
        values = (column1, column2)    # Specify the values for each column

        # Execute the SQL query
        cursor.execute(sql, values)
    
    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Call the function to insert data from Google Sheets to MySQL
insert_data_from_sheet_to_mysql()
