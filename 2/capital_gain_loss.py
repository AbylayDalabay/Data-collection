import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['capital_gain_loss'] = stocks.apply(lambda row: (-1 if row.operation == 'Buy' else 1) * row.price, axis=1)
    FFT = stocks.groupby(['stock_name']).agg({
        'capital_gain_loss' : 'sum'
    }).reset_index().sort_values(by='stock_name')
    return FFT