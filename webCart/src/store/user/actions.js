import { LOAD_USER_INFO } from './types'
import { api } from 'boot/axios'

export default {
  [LOAD_USER_INFO] ({ commit }) {
    console.log('FETCHING USER INFO...')
    api.get('/users/getUserById/1')
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
          commit('loadUserInfo', response.data.userInfo)
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
