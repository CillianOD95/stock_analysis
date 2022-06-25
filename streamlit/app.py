import streamlit as st
import requests
import plotly.express as px
import pandas as pd
import os
import plotly.graph_objects as go

import sys
sys.path.append('C:/Users/cilli/random_projects/stock_analysis')

from stock_analysis.plots import plot_returns, plot_stock_time_series, plot_returns
from stock_analysis.transformations import convert_price_to_returns

st.set_page_config(page_title='Test',layout='wide')

@st.cache
def load_stock_data():
    return pd.read_csv('C:/Users/cilli/random_projects/stock_analysis/data/stocks/sample_stocks.csv')

st.title('Simple Stock Analysis!')

df = load_stock_data()

stock_list = list(df['symbol'].unique())
stock_list.sort()
symbol = st.sidebar.selectbox("Stock symbol:", stock_list)


comp_name = df[df['symbol']==symbol]['name'].iloc[0] + ' (' + df[df['symbol']==symbol]['sector'].iloc[0] + ')'
st.header(f'Performance of {comp_name}')

col1, col2 = st.columns(2)

with col1:
    fig = plot_stock_time_series(df[df['symbol']==symbol])

    st.plotly_chart(fig)

with col2:
    s = convert_price_to_returns(df[df['symbol']==symbol], 'close', 'date')
    fig = plot_returns(s)
    st.plotly_chart(fig)
