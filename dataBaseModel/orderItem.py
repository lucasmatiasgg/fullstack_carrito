import config

# Agregue al DER el campo id_cart, ya que siempre que hay un muchos a muchos y se rompe, las PK de ambas
# tablas, pasan como FK a la intermedia. En caso de que esta intermedia no tenga Pk, ambas serian PK.
# Pero en este caso podemos implementar un id_order

asociation_table = config.Table('order_item', config.Base.metadata,
    config.Column('cart_id', config.Integer, config.ForeignKey('cart.id'), primary_key = True),
    config.Column('item_id', config.Integer, config.ForeignKey('item.id_item'), primary_key = True)
))