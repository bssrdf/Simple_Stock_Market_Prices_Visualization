import matplotlib.pyplot as plt
import requests, json,time
import tkinter as tk
from tkinter import messagebox

# define variables for data retrieval
times = [] #stores the values of the time when we retrieve price data in a list.
currency = "BTC" # holds the stock symbol we will be fetching data for
prices = [] #dictionary that holds the list of prices for currency defined.
plt.style.use('dark_background')

def retrieve_data():

    # append new time to list of times
    times.append(time.strftime('%H:%M:%S'))

    # make request to API and get response as object
    api_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=USD".format(currency)
    try:
        response = json.loads(requests.get(api_url).content)

        # append new price to list of prices for graph
        price = response[currency].get('USD')
        prices.append(price)
    except:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Oops", "The stock market is close right now!\nTry the system later, Thank you.")
        exit(0)

    # clear plot
    plt.clf()

    # x axis values
    x = times

    # corresponding y axis values
    y = prices

    # avoid overlapping in x axis
    if len(x)>15:
        del x[0]
        del y[0]

    # plotting the points
    plt.plot(x,y,marker="x",color="w")

    # naming the x axis
    plt.xlabel('Current Time')

    # naming the y axis
    plt.ylabel('Prices (USD)')

    # remove top and right borders
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # giving a title to my graph
    plt.title('Bitcoin Prices')
    
    # update every 5 seconds
    plt.pause(5)


while(True):
    retrieve_data()
