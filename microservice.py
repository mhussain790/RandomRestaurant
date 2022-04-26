import requests
import pandas_datareader as pdr
import yfinance as yf
import datetime as dt
import time

### Global Variables ###
ticker_name = ""
ticker_date = ""


# run_Search():
    # Method that runs indefinitely that reads status.txt file and if the file contains 'run'
    # then it will open stocks.txt and read the ticker name and date.
    # The method will then call getStock to use the ticker name/date to retrieve price info.

def run_search():
    while True:
        time.sleep(5)
        with open('status.txt') as g:
            run_text = g.readline()
        if run_text == 'run':
            print('---Retrieving stock info from stocks.txt---')

            # Open stocks.txt and read each line: 1st line = ticker_name, 2nd line = date
            with open("stocks.txt") as f:
                lines = f.read() ##Assume the sample file has 3 lines
                ticker_name = lines.split('\n', 1)[0]
                ticker_date =  lines.split('\n', 2)[1]

            # Output confirmation message
            print('Run_Search Function - Running')
            print('Ticker: ' + ticker_name)
            print('Date: ' + ticker_date)

            # Run getStock method to retrieve price info
            getStock(ticker_name, ticker_date)

            # Clear status.txt
            with open('status.txt', 'w+') as h:
                h.write('')

            # Method complete status message
            print('status.txt was cleared')

# outputToFile():
    # Method that outputs data returned from getStock method to a text file named output.txt

def outputToFile(output_data):
    with open('output.txt', 'w+') as f:
        f.write(str(output_data))

# getStock():
    # Method to retrieve stock data with the stock_name and date

def getStock(stock_name, date):

    # Test Code for pdr
        # start = dt.datetime(2022, 2, 24)
        # data = pdr.get_data_yahoo('AAPL', start)

    # Data object containing price information using (ticker_name, start_date, end_date)
    data = pdr.get_data_yahoo(stock_name, date, date)

    # Call method to output data to text file
    outputToFile(data)

#### TEST CODE ###
# stock_info = yf.Ticker('MSFT').info
# # stock_info.keys() for other properties you can explore
# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']
# print('market price ', market_price)
# print('previous close price ', previous_close_price)

### Method Call ###
run_search()

