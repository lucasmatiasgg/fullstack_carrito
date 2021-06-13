export default {
  addProductsFromCart: function (state, data) {
    console.log(data)
    state.productCartList = data
  }
}
