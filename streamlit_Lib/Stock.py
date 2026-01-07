import yfinance as yf
import pandas as pd
import streamlit as st 

st.title("Simple Stock Price App")
st.write("""
        *Stock Price*
        Shown are the *Closing Price* and *Its Volume*""")

tickertitle = "AAPL"
tickerData= yf.Ticker(tickertitle)

tickerDf=tickerData.history(
    start='2010-5-31',
    end='2020-5-31'
)
# print(tickerDf.head())
if tickerDf.empty:
    st.error("No Data Found, Please Try Other")
else:
    st.subheader("Closing Price")
    st.line_chart(tickerDf["Close"])
    
    st.subheader("Volume")
    st.line_chart(tickerDf['Volume'])