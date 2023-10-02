import streamlit as st
import datetime


from frankfurter import Frankfurter
from currency import Currency

frank_api = Frankfurter()
curr_conv = Currency()

def main():

   
    # Display Streamlit App Title
    st.title("FX Converter")

    # Get the list of available currencies from Frankfurter
    curr_list = frank_api.get_currencies_list()

    # If the list of available currencies is None, display an error message in Streamlit App
    if curr_list is None:
        st.error("Error: Unable to fetch the list of available currencies.")
        return
    # Add input fields for capturing amount, from and to currencies
    amount = st.number_input('Amount to be converted', min_value=0.01, step=0.01, format="%f")
    
    Cur1 = st.selectbox("From Currency", curr_list)
    Cur2 = st.selectbox("To Currency", curr_list)

    # Add a button to get and display the latest rate for selected currencies and amount
    if st.button("Get Latest Rate"):
        date, rate = frank_api.get_latest_rates(Cur1, Cur2, amount)
        if date and rate:
            curr_conv.from_currency = Cur1
            curr_conv.to_currency = Cur2
            curr_conv.amount = amount
            curr_conv.rate = rate
            curr_conv.date = date
            
            st.subheader("Latest Conversion Rate")
            st.write(curr_conv.format_output())
        else:
            st.error("Error: Unable to fetch the latest conversion rate.")

    # Add a date selector (calendar)
    st.write("Select a date")
    deit = st.date_input("Select a Date", datetime.date.today())


    # Add a button to get and display the historical rate for selected date, currencies and amount
    
    if st.button("Get Historical Rate"):
        historical_rate_data = frank_api.get_historical_rate(Cur1, Cur2, str(deit))
        if historical_rate_data:
            curr_conv.from_json(historical_rate_data)
            curr_conv.amount = amount
            st.subheader("Historical Conversion Rate:")
            st.write(curr_conv.format_output())
        else:
            st.error("Error: Unable to fetch the historical conversion rate.")

if __name__ == "__main__":
    main()







