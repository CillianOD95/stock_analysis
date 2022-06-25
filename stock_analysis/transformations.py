
def convert_price_to_returns(df, series, date):
    s = df[series]
    returns = s/s.shift(1) - 1
    returns.index = df[date]
    return returns


