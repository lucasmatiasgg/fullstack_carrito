import config

association_table = config.Table('history_cart', config.Base.metadata,
    config.Column('user_id', config.Integer, config.ForeignKey('user.id')),
    config.Column('cart_id', config.Integer, config.ForeignKey('cart.id'))
)