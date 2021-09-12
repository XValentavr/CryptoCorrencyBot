import urllib.request
import json


def get_crypto_price(symbol, bot, message):
    try:
        url = f"https://data.messari.io/api/v1/assets/{symbol}/metrics"
        result = json.loads(urllib.request.urlopen(url).read())
        if len(result) > 0:
            return result["data"]["market_data"]["ohlcv_last_1_hour"]
        else:
            bot.send_message(message.chat.id, 'Can\' find current crypto. Try again.')

    except Exception:
        bot.send_message(message.chat.id, 'An error occured. Try again.')


def pritty_currency(value, bot, message):
    crypto = get_crypto_price(symbol=value, bot=bot, message=message)
    open_ = crypto["open"]
    high = crypto["high"]
    low = crypto["low"]
    close = crypto["close"]
    return open_, high, low, close
