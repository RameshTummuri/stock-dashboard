import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📈 Stock Market Dashboard")

stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, INFY.NS, TCS.NS)", "AAPL")

if stock_symbol:
    stock_data = yf.Ticker(stock_symbol)
    stock_df = stock_data.history(period="6mo")

    st.subheader(f"Stock Price for {stock_symbol} (Last 6 Months)")
    st.line_chart(stock_df['Close'])

    with st.expander("📊 View Raw Data"):
        st.write(stock_df.tail())

    st.subheader("📌 Company Info")
    info = stock_data.info
    st.write(f"**Name:** {info.get('shortName')}")
    st.write(f"**Sector:** {info.get('sector')}")
    st.write(f"**Market Cap:** {info.get('marketCap')}")
