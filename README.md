# Building Currency Converter in Python
## Shaqran Bin Saleh
## ID: 25010238


### Description of the Project

This project deals with python programming and also the use of streamlit to make a web app which enables the users to select currencies and convert amount basing upon the two currencies rate on a particular date. The goal of your program is to display the current conversion rate between 2 currency codes at a specific date or for the latest date. It will also calculate the inverse conversion rate between these 2 currenciesThe project involves dealing with API and how to use to get values. In short we can say that doing the project, the people involved in doing it would be able to learn python programming, API handling and also making up a quick web-app using streamlit in python.

### Instructions

- Since the web application is totally dependent on python. So the first thing to do is to make sure that python is installed in the computer
- Then we need to make sure streamlit has been installed in the computer. So that we are able to run the web application.

  - We install streamlit by the following command in the terminal: "pip install streamlit"
- We make sure Requests has been installed in the computer. The requests library is a popular Python library used for making HTTP requests. It allows us to send HTTP requests to web services or websites and retrieve data from them. This is a fundamental capability when working with web-based APIs, scraping web content, or interacting with web services.

  - We install the request module by the following command in the terminal: "pip install requests"
- Finally to run the web app we have to run the file containg the main() function. So we run the app.py file.

  - We run the file using the following command: "streamlit run app.py"

### File Details and Functionality

- **File name: api.py**

    
    - This is the file that holds the GET function of the requests module for retrieving content from an API.

    - In this file we first import the "requests" module for accessing API callings to get the value from an API.
  
    - We define a function called, "get_url" which when provided a GET API endpoint url then it will return its status code and either its content or error message as a string.
 
    - This file and this function will be used in the next next files because of the dependency of the "get_url" function.
 
    - The function takes url as an input and returns the status code and the content from the API upon successful calling.

- **File name: frankfurter.py**
    
    - This is the file that holds all the functions needed to perform the retrieval of content and presenting the output with the use of the urls defined and the help of the "get_url" function which was previously created in the api.py file.
    
    - Here we import the two modules "requests" and "json". Both important in getting the data and presenting the outcome.
    
    - And we define the base url which is the basic url in opening up the API link that holds all the data and which we will further modify to access data upon our need.
 
    - A class "Frankfurter" is to be created which is going to hold all the initialized variables and the required functions for getting outcomes.
 
    - The "__init__" function is going to hold all the required variables needed to be referenced to be used in the next functions.
 
    - The "get_currencies_list" is the function which is to be used to fetch the list of currency codes.
 
    - The "get_latest_rates" is the fucntion which takes in 3 parameters. The first parameter is the currency from which an amount is to be converted, the second one is the currency to which the amount is to be converted and the final parameter is the amount. Upon successful calling of this function, it will return the date and the rate. The date is usually the latest avaliable date in the dataset as the rates are always updating.

 
    - The "get_historical_rate" is the fucntion which takes in 3 parameters. The first parameter is the currency from which the amount is to be converted, the second one is the currency to which the amount is to be converted and the final parameter is the date. Upon successful calling of this function, the function will return a dictionary variable holding all the data as asked through the parameters.
 

- **File name: currency.py**

  - This is the file that holds all the functions needed to perform the retrieval of content and presenting the output as it deals directly with the retrieved dictionary from other functions of other files.
 
  -  A class "Currency" is to be created which is going to hold all the initialized variables and the required functions for getting outcomes.
 
  -  The "__init__" function is going to hold all the required variables needed to be referenced to be used in the next functions and also in the main file.
 
  -  The "from_json" function is the function which need to be used to retrieve data from the dictionary file which gets retrieved with the help of other files and functions. This is the function which defines the variables with the required data.
 
  -  The "round_rate" function is a function that takes the rate as a parameter and returns its its rounded up value to upto 4 decimal places.
 
  -  The "reverse_rate" function is a function that returns the inverse of a dictionary's rate nd also rounding it upto 4 decimal places.
 
  -  The "format_output" function i the function which would display the outcome. This is the function which would give all the details regarding the convertion. The returened string would show the date of the convertion rate, the convertion rate, the amount when the convertion gets done , the currencies from which the convertion was done, the currency to which the convertion gets done and also the inverse of the convertion rate.


- **File name: app.py**

    
    - This is the file that holds everything needed to make the streamlit webapp. The file reference the above mentioned files and thier functions to create functionality within the streamlit app.
 
    - The file imports the "streamlit" and "datetime" module and uses the classes created on the two files "frakfurter.py" and "currency.py"


