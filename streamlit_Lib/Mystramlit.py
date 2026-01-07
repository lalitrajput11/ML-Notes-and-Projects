# import yfinance as yf
# import streamlit as st
# import pandas as pd

# st.title("📈 Simple Stock Price App")

# tickerSymbol = "GOOGL"

# tickerData = yf.Ticker(tickerSymbol)

# tickerDf = tickerData.history(period="1mo")

# if tickerDf.empty:
#     st.error("No data found. Please try again later.")
# else:
#     st.subheader("Closing Price")
#     st.line_chart(tickerDf["Close"])

#     st.subheader("Volume")
#     st.line_chart(tickerDf["Volume"])


import yfinance as yf
import streamlit as st

# st.title("📈 Simple Stock Price App")
st.write("""
         *Stock Price*
       Shown are the stock Closing Price and Volume  """)
tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

# tickerDf = tickerData.history(period="1mo")
tickerDf = tickerData.history(
    start="2010-05-31",
    end="2020-05-31"
)

if tickerDf.empty:
    st.error("No data found. Please try another ticker.")
else:
    st.subheader("Closing Price")
    st.line_chart(tickerDf["Close"])

    st.subheader("Volume")
    st.line_chart(tickerDf["Volume"])
