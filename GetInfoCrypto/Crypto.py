"""Use API to get info about specific cryptocurrencty"""

# project imports
import urllib.request
import json


def get_crypto_price(symbol: str, bot, message) -> None:
    """
    get cryptocurrency from service
    :param symbol: str
    :param bot: bot
    :param message: bot message
    :return:
    """
    try:
        url = f"https://data.messari.io/api/v1/assets/{symbol}/metrics"
        result = json.loads(urllib.request.urlopen(url).read())

        # if find something then get info
        if len(result) > 0:
            return result["data"]["market_data"]["ohlcv_last_1_hour"]
        else:
            bot.send_message(message.chat.id, 'Can\'t find current crypto. Try again.')

    except Exception:
        bot.send_message(message.chat.id, 'An error occured. Try again.')


def pritty_currency(value: float, bot, message) -> list:
    """
    return interesting values about currency
    :param value: float
    :param bot: bot
    :param message: bot message
    :return:
    """
    crypto = get_crypto_price(symbol=value, bot=bot, message=message)
    return crypto["open"], crypto["high"], crypto["low"], crypto["close"]
