import gspread
from google.oauth2.service_account import Credentials

# Define the scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Define the credentials
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(scope)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Define the sheet
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# Get the data from the sheet
sales = SHEET.worksheet("sales")

data = sales.get_all_values()

print(data)