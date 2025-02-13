import requests
import streamlit as st

def get_stock_price(symbol, api_key):
    base_url = "https://www.alphavantage.co/query?"
    function = "TIME_SERIES_INTRADAY"
    interval = "5min"
    complete_url = f"{base_url}function={function}&symbol={symbol}&interval={interval}&apikey={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        if "Time Series (5min)" in data:
            latest_time = list(data["Time Series (5min)"].keys())[0]
            latest_data = data["Time Series (5min)"][latest_time]
            return {
                "Time": latest_time,
                "Open": latest_data["1. open"],
                "High": latest_data["2. high"],
                "Low": latest_data["3. low"],
                "Close": latest_data["4. close"],
                "Volume": latest_data["5. volume"]
            }
        else:
            return None
    else:
        return None

def main():
    st.title("Stock Market Tracker")
    
    stock_symbol = st.text_input("Enter stock symbol:")
    api_key = "QVHP8NF4RG7WQUHN"  # Replace with your actual Alpha Vantage API key
    
    if st.button("Get Stock Price"):
        stock_price = get_stock_price(stock_symbol, api_key)
        
        if stock_price:
            st.write(f"Time: {stock_price['Time']}")
            st.write(f"Open: {stock_price['Open']}")
            st.write(f"High: {stock_price['High']}")
            st.write(f"Low: {stock_price['Low']}")
            st.write(f"Close: {stock_price['Close']}")
            st.write(f"Volume: {stock_price['Volume']}")
        else:
            st.write("Stock symbol not found or API limit reached.")

if __name__ == "__main__":
    main()