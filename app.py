import streamlit as st
import requests

st.set_page_config(
    page_title="TickrX",
    page_icon="icon.png",
    menu_items={
        "About":
        "TickrX offers immediate access to NASDAQ stock prices. Simply enter a stock symbol to view the latest market data in seconds. Ideal for investors and traders who need fast, reliable stock information. Experience seamless tracking with TickrX—your go-to tool for real-time market insights."
    })

st.write("<h2 style='color:#FF8343;'>Real Time NASDAQ Stock Tracker</h2>",
         unsafe_allow_html=True)

symbol = st.text_input("Stock Symbol", placeholder="GOOG")

btn = st.button("Track Stock")
if btn:
  if (len(symbol) >= 1):
    api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(
        symbol.strip())
    response = requests.get(
        api_url,
        headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    if response.status_code == requests.codes.ok:
      data = response.json()
      if (len(data) >= 1):

        st.write(
            f"<h2 style='color:#88D66C;'>{data['name']} ({data['ticker']})</h2>",
            unsafe_allow_html=True)

        st.write(f"<h2 style='color:#FFDA76;'>{data['price']} USD</h2>",
                 unsafe_allow_html=True)

      else:
        st.info("Stock Information Unavailable.")
  else:
    st.warning("Provide Stock Symbol!")
