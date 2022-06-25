import plotly.express as px

def plot_stock_time_series(df):
    fig = px.line(df, x='date', y = 'close')
    fig.update_layout(
        title = '<b>Lifetime Stock Performance</b>',
        xaxis_title = 'Date',
        yaxis_title = 'Close Price'
    )
    return fig

def plot_returns(s):
    fig = px.line(s)
    fig.update_layout(
        title = '<b>Lifetime Stock Returns</b>',
        xaxis_title = 'Date',
        yaxis_title = 'Return'
    )
    return fig

