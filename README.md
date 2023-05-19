# Google Sheets to MySQL Data Import

This script allows you to import data from a Google Sheets document into a MySQL database table. It uses the `gspread` library to access Google Sheets and the `mysql-connector-python` library to connect to MySQL.

## Prerequisites

- Python 3.x installed on your system.
- Install the required libraries using the following command:

```
   pip install -r requirements.txt
```


## Getting Started

1. Obtain Google Sheets credentials:
 - Go to the [Google Developers Console](https://console.developers.google.com/).
 - Create a new project or select an existing one.
 - Enable the Google Sheets API.
 - Create a service account and download the credentials JSON file.
 - Save the JSON file in your project directory.

2. Set up the MySQL database:
 - Create a MySQL database if you don't have one.
 - Create a table in the database with the desired structure.

3. Configure the script:
 - Open the `sheetsToSql.py` file.
 - Fill in the required values:
   - `sheet_key`: Key of the Google Sheets document.
   - `credentials_file`: Path to the downloaded credentials JSON file.
   - `sheet_name`: Name of the sheet within the Google Sheets document.
   - `mysql_host`: MySQL server address.
   - `mysql_user`: MySQL username.
   - `mysql_password`: MySQL password.
   - `mysql_database`: Name of the MySQL database.
   - `table_name`: Name of the table in the MySQL database.
   - `column_username`: Column name for the username in the table.
   - `column_email`: Column name for the email in the table.
 - Save the `sheetsToSql.py` file.

4. Run the script:
 - Open a command prompt or terminal.
 - Navigate to the project directory.
 - Execute the following command:
   ```
   python sheetsToSql.py
   ```
 - The script will connect to Google Sheets, retrieve data, and insert it into the MySQL database table.

Feel free to customize the table structure and column names in the MySQL database and update the `sheetsToSql.py` file accordingly.
