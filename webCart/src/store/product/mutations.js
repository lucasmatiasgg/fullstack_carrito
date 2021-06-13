export default {
  addProducts: function (state, data) {
    console.log(data)
    state.productList = data
  }
}
