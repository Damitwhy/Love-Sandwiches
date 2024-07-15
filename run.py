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

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        print(f"The data provided is {data_str}")
        sales_data = data_str.split(",")

    #     if validate_data(sales_data):
    #         print("Data is valid!")
    #         break

    # return sales_data
get_sales_data()