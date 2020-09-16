from pycoingecko import CoinGeckoAPI
from app import db
from app.models import BtcPrices, BchPrices, MoneroPrices


def get_prices_coins():
    cg = CoinGeckoAPI()

    # x = (cg.get_coins_list())
    # for value in x:
    #     print(value)
    btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
    btc_price = (btc['bitcoin']['usd'])
    btc_data = BtcPrices.query.filter_by(id=1).first()

    bch = cg.get_price(ids='bitcoin-cash', vs_currencies='usd')
    btc_cash_price = (bch['bitcoin-cash']['usd'])
    bch_data = BchPrices.query.filter_by(id=1).first()

    xmr = cg.get_price(ids='monero', vs_currencies='usd')
    xmr_price = (xmr['monero']['usd'])
    xmr_data = MoneroPrices.query.filter_by(id=1).first()

    btc_data.price = btc_price
    bch_data.price = btc_cash_price
    xmr_data.price = xmr_price

    db.session.add(btc_data)
    db.session.add(bch_data)
    db.session.add(xmr_data)

    db.session.commit()


if __name__ == '__main__':
    get_prices_coins()