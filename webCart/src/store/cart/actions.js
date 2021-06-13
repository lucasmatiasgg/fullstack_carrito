import { LOAD_PRODUCTS_FROM_CART } from './types'
import { api } from 'boot/axios'

export default {
  [LOAD_PRODUCTS_FROM_CART] ({ commit }) {
    console.log('FETCHING PRODUCTS FROM CART')
    api.get('/carts/getProductsByCartId/1')
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
      .catch(() => {
        this.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Loading failed',
          icon: 'report_problem'
        })
      })
  }
}
