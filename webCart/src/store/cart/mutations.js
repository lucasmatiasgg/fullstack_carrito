export default {
  addProductsFromCart: function (state, data) {
    console.log(data)
    state.productCartList = data
  },
  setCartId: function (state, data) {
    console.log('mutation-setCartId:' + data)
    state.idCart = data
  }
}
