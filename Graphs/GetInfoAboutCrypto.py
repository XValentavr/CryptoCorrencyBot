"""This module create imgae using shrimpy library"""

# project imports
import shrimpy
import plotly.graph_objects as go
# local imports
from BotInit.BotInit import bot_initializer


def send_chart(message, crypto: str) -> None:
    """
    creates chart from shrimpy and build graph
    :param message: message
    :param crypto: str
    """
    public_key = 'd63acca381d743396d51783fa8c4209dc5ca4a2941482d9cde4a2b78ce2d5a9b'
    secret_key = '2ff0461c8f8affae5fca855fcb9e0ea333f7da3692e62296964c65b1a255fa88c23a01cb71237160d571e660a20d2438588235c77886c8c1b9a0e648e3d2841f'

    # create the client
    client = shrimpy.ShrimpyApiClient(public_key, secret_key)

    candles = client.get_candles(
        'binance',
        f'{crypto.upper()}',
        'BUSD',
        '15m'
    )

    # create lists to hold our different data elements
    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []

    # convert from the Shrimpy candlesticks to the plotly graph objects format
    for candle in candles:
        dates.append(candle['time'])
        open_data.append(candle['open'])
        high_data.append(candle['high'])
        low_data.append(candle['low'])
        close_data.append(candle['close'])

    # construct the figure
    bot = bot_initializer()
    fig = go.Figure(data=[go.Candlestick(x=dates,
                                         open=open_data, high=high_data,
                                         low=low_data, close=close_data)])
    bot.send_plot(message.chat.id, fig)
