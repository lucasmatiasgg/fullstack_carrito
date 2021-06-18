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
    console.log(data.idCart)
    state.productCartList.remove(data.idCart)
  }
}
