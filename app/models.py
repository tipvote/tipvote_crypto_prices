from app import db


class BtcPrices(db.Model):
    __tablename__ = 'prices_btc'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class BchPrices(db.Model):
    __tablename__ = 'prices_bch'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class MoneroPrices(db.Model):
    __tablename__ = 'prices_monero'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class LtcPrices(db.Model):
    __tablename__ = 'prices_ltc'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


db.create_all()
db.session.commit()