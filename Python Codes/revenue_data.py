# First Lets Import all necessary libraries:
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Task 1: Lets use yfinance to extract stock data for Tesla
===========================================================
# We'll use Ticker function here. (Ticker Symbol for Tesla is "TSLA")

tesla = yf.Ticker("TSLA")

# Extracting all stock information by setting the period parameter to "max" so  we get information for the maximum amount of time and then storing it to a DataFrame
tesla_data = pd.DataFrame(tesla.history(period = "max"))
tesla_data
