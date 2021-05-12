import config
#Agregue el primary key, porque solo estaba marcado el FK.
history_cart = config.Table('history_cart', config.Base.metadata,
    config.Column('user_id', config.Integer, config.ForeignKey('user.user_id'), primary_key = True),
    config.Column('cart_id', config.Integer, config.ForeignKey('cart.cart_id'), primary_key = True),
    config.Column('close_date', config.Date, nullable=True)
)