import requests
import json
import sys

try:
    r= requests.get("https://rest.coincap.io/v3/assets?apiKey=58bdc1392a9b5e58dafcc3ba8e2dd7c6fa69a265f229e932c78c3ba1f2ed817f")
    o = r.json()
    #price = float(o["data"][0]["priceUsd"])
    price = 97845.0243

    if len(sys.argv)<=1:
        sys.exit("Missing command-line argument")
    else:
        try:
            quantity = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number ")
        else:
            amount = quantity* price
            print(f"${amount:,.4f}")


except requests.RequestException:
    print("An error occured")

