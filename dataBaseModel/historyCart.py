import config
#Agregue el primary key, porque solo estaba marcado el FK.
association_table = config.Table('history_cart', config.Base.metadata,
    config.Column('user_id', config.Integer, config.ForeignKey('user.id'), primary_key = True),
    config.Column('cart_id', config.Integer, config.ForeignKey('cart.id'), primary_key = True)
)