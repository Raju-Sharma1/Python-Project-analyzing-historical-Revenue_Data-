# First Lets Import all necessary libraries:
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

# TASK 1: Using yfinance API to extract stock data for Tesla:
#===========================================================

# Using Ticker function. (Ticker Symbol for Tesla is "TSLA")
tesla = yf.Ticker("TSLA")

# Extracting all stock information by setting the period parameter to "max" so  we get information for the maximum amount of time and then storing it to a DataFrame
tesla_data = pd.DataFrame(tesla.history(period = "max"))
tesla_data

# Reseting the index and then storing it into a DataFrame
tesla_data.reset_index(inplace = True)
tesla_data.head() # viewing the first 5 rows from the DataFrame
#=================================================================


# TASK 2: Web Scrapping to extract Tesla Revenue Data
#=================================================================

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text # Using requests get function to extract webpage data and converting it into text format.

# After data is extracted, we'd have to parse the HTML raw data into searchable format.
# Here I will be using BeautifulSoup library to parse the data using parser "html.parser"
soup = BeautifulSoup(html_data, "html.parser")

# Extracting the table Tesla Revenue and storing it into a DataFrame. Creating columns "Date" and "Revenue" to store the data extracted from the webpage table.
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"]) # variable keeping the DataFrame with columns "Date" and "Revenue"

tbody = soup.find("tbody")
for row in tbody.find_all("tr"): # looping through the tbody to find all table rows.
    col = row.find_all("td") # storing all table data to col variable
    date = col[0].text.strip() # indexing the date no. to get all date rows into text and clearing whitespace.
    revenue = col[1].text.strip() # indexing the revenue no. to get all revenue rows into text and clearing whitespace.

    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index = True) # storing extracted data to the DataFrame.
tesla_revenue

# Removing comma and $ sign from the revenue column.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

# Removing nulls and empty string from the revenue column.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Viewing the last 5 rows from the DataFrame.
tesla_revenue.tail()
#=================================================================


# TASK 3: Using yfinance API to extract stock data for GameStop:
#=================================================================

# Using Ticker(). (Ticker symbol for GameStop is "GME")
GameStop = yf.Ticker("GME")

# Extracting all stock information by setting the period parameter to "max" so  we get information for the maximum amount of time and then storing it to a DataFrame.
gme_data = pd.DataFrame(GameStop.history(period = "max"))
gme_data

# Reseting the index and then storing it into a DataFrame
gme_data.reset_index(inplace=True)
#=================================================================


# TASK 4: Web Scrapping to extract GameStop Revenue Data
#=================================================================
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url).text

# After data is extracted, we'd have to parse the HTML raw data into searchable format.
# Here I will be using BeautifulSoup library to parse the data using parser "html.parser"
soup = BeautifulSoup(html_data_2, "html.parser")

# Extracting the table GameStop Revenue and storing it into a DataFrame. Creating columns "Date" and "Revenue" to store the data extracted from the webpage table.
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
tbody = soup.find("tbody")

for row in tbody.find_all("tr"): #looping through table data
    col = row.find_all("td")
    date = col[0].text.strip() # indexing date column
    revenue = col[1].text.strip() # indexing revenue column

    gme_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})], ignore_index = True) # storing extracted date to the DataFram
gme_revenue

# Removing comma and $ sign from the revenue column.
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True)

# Removing nulls and empty string from the revenue column.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Viewing the last 5 rows from the DataFrame.
gme_revenue.tail()
