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
     
    - In the file, the "get_url" function is present so that upon calling this function, the function will call and provide GET API endpoint url and return its status code and either its content or error message as a string.
 
    - This file and this function will be used in the next next files because of the dependency of the "get_url" function.
 
    - The function takes url as an input and returns the status code and the content from the API.

- **File name: api.py**
    - In this file we first import the "requests" module for accessing API callings to get the value from an API.
    - We define a function called, "get_url" which when provided a GET API endpoint url then it will return its status code and either its content or error message as a string.

