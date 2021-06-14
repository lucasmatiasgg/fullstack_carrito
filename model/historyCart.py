import config
#Agregue el primary key, porque solo estaba marcado el FK.
history_cart = config.Table('history_cart', config.Base.metadata,
    config.Column('userId', config.Integer, config.ForeignKey('user.userId'), primary_key = True),
    config.Column('cartId', config.Integer, config.ForeignKey('cart.cartId'), primary_key = True),
    config.Column('close_date', config.Date, nullable=True)
)