export default {
  addProductsFromCart: function (state, data) {
    console.log(data)
    state.productCartList = data
  },
  setCartId: function (state, data) {
    console.log('mutation-setCartId:' + data)
    state.idCart = data
  },
  deleteProductsFromCart: function (state, data) {
    console.log('mutation-deleteProductsFromCart')
    state.productCartList = state.productCartList.filter(val => val.idProduct !== data)
  }
}
