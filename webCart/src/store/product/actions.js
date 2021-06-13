import { LOAD_PRODUCTS } from './types'
import { api } from 'boot/axios'

export default {
  [LOAD_PRODUCTS] ({ commit }) {
    console.log('FETCHING PRODUCTS')
    api.get('/products/getAllProducts')
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
          commit('addProducts', response.data.products)
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
