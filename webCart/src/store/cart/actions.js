import { LOAD_PRODUCTS_FROM_CART, ADD_PRODUCT_TO_CART, DELETE_PRODUCT_FROM_CART } from './types'
import { api } from 'boot/axios'

export default {
  [LOAD_PRODUCTS_FROM_CART] ({ commit }, data) {
    console.log('FETCHING PRODUCTS FROM CART')
    console.log('cartId:' + data.idCart)
    api.get('/carts/getProductsByCartId/' + data.idCart)
      .then((response) => {
        if (!response.data.status.success) {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: response.data.status.message,
            icon: 'report_problem'
          })
        } else {
          console.log('ACTIONS-OK')
          console.log(response.data)
          commit('addProductsFromCart', response.data.products)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  [ADD_PRODUCT_TO_CART] ({ commit }, info) {
    console.log('ADDING PRODUCTS TO CART')
    console.log(info.data.productId + ' - ' + info.data.quantity)
    api.post('/carts/addProductToCart',
      {
        idProduct: info.data.productId,
        quantity: info.data.quantity,
        idUser: info.data.userId
      })
      .then((response) => {
        if (!response.data.status.success) {
          console.log(response.data.status.message)
        } else {
          console.log('ACTIONS-ADD_PRODUCT_TO_CART-OK')
          console.log(response.data)
          commit('setCartId', response.data.idCart)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  [DELETE_PRODUCT_FROM_CART] ({ commit }, info) {
    console.log('DELETE_PRODUCT_FROM_CART')
    console.log(info.data.idProduct + ' - ' + info.data.idCart)
    api.delete('/carts/deleteItem/',
      {
        params: {
          idCart: info.data.idCart,
          idProduct: info.data.idProduct
        }
      })
      .then((response) => {
        if (!response.data.success) {
          console.log(response.data.message)
        } else {
          console.log('DELETE_PRODUCT_FROM_CART-OK')
          console.log(response.data)
          commit('deleteProductsFromCart', info.data.idCart)
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
