from api import get_url
import requests
import json

BASE_URL = "https://api.frankfurter.app"

class Frankfurter:

    def __init__(self):
        self.base_url: str = BASE_URL
        self.curr_url: str = 'https://api.frankfurter.app/currencies'
        self.curr_list: list = []

    def get_currencies_list(self):
        """
        Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
        After the API call, it will perform a check to see if the API call was successful.
        If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
        Otherwise it will return the value None.

        Parameters
        ----------
        None

        Returns
        -------
        list
            List of available currencies or None in case of error
        """
        response= requests.get(self.curr_url)
        dic = response.json()
        self.curr_list = list(dic.keys())
        
        return self.curr_list


    def get_latest_rates(self, from_currency, to_currency, amount):
        """
        Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
        After the API call, it will perform a check to see if the API call was successful.
        If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
        Otherwise it will return the value None twice.

        Parameters
        ----------
        from_currency : str
            Code for the origin currency
        to_currency : str
            Code for the destination currency
        amount : float
            The amount (in origin currency) to be converted

        Returns
        -------
        str
            Date of latest FX conversion rate or None in case of error
        float
            Latest FX conversion rate or None in case of error
        """
        url = f"{self.base_url}/latest?from={from_currency}&to={to_currency}"
        response = requests.get(url)

        if response.status_code == 200:
                data = response.json()
                date = data.get('date')
                rate_dat = data.get('rates', {})
                rate = rate_dat.get(to_currency)
                return date, rate
            
        else:
            print(f"API call failed with status code {response.status_code}")
            return None, None
        

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
        After the API call, it will perform a check to see if the API call was successful.
        If it is the case, it will load the response as JSON, extract the conversion rate and return it.
        Otherwise it will return the value None.

        Parameters
        ----------
        from_currency : str
            Code for the origin currency
        to_currency : str
            Code for the destination currency
        amount : float
            The amount (in origin currency) to be converted
        from_date : str
            Date when the conversion rate was recorded

        Returns
        -------
        float
            Latest FX conversion rate or None in case of error
        """
        
        endpoint= f"{self.base_url}/{from_date}?from={from_currency}&to={to_currency}"
        
        data = (get_url(endpoint).json())
        return data