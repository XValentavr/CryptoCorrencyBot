import requests
import pandas as pd
from datetime import datetime

from CreateCommands import StartAndReset


def get_crypto_price(symbol, exchange, start_date, bot, message):
    try:
        api_key = 'CHA55GZBGSZ6PNJ7'
        api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
        df = df.rename(
            columns={'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low',
                     '4a. close (USD)': 'close',
                     '5. volume': 'volume'})
        for i in df.columns:
            df[i] = df[i].astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.iloc[::-1].drop(
            ['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis=1)
        if start_date:
            df = df[df.index >= start_date]
        return df
    except KeyError:
        bot.send_message(message.chat.id, 'An error occured. Try again.')


def pritty_currency(value, bot, message):
    date = datetime.today().strftime('%Y-%m-%d')
    crypto = get_crypto_price(symbol=value, exchange='USD', start_date=date, bot=bot, message=message)
    open_ = crypto["open"][date]
    high = crypto["high"][date]
    low = crypto["low"][date]
    close = crypto["close"][date]
    return open_, high, low, close
