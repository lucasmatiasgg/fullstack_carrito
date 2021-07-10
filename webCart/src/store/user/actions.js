import { LOAD_USER_INFO, UPDATE_PASSWORD, UPDATE_USER_DATA } from './types'
import { api } from 'boot/axios'

export default {
  [LOAD_USER_INFO] ({ commit }, data) {
    console.log('FETCHING USER INFO...')
    api.get('/users/getUserById/' + data.userId)
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
          message: 'Estamos con problemas de conexión',
          icon: 'report_problem'
        })
      })
  },

  [UPDATE_USER_DATA] ({ commit }, data) {
    console.log(data)
    api.put('/users/update/' + data.data.userId, {
      firstName: data.data.firstName,
      lastName: data.data.lastName,
      oldPassword: data.data.oldPassword
    })
      .then((response) => {
        if (!response.data.status.success) {
          console.log('Fallo el update de usuario')
        } else {
          console.log('Usuario actualizado')
        }
      }).catch(() => {
        console.log('Hubo un error inesperado')
      })
  },

  [UPDATE_PASSWORD] ({ commit }, data) {
    console.log(data)
    api.put('/users/updatePassword/' + data.data.userId, {
      newPassword: data.data.newPassword,
      oldPassword: data.data.oldPassword
    })
      .then((response) => {
        if (!response.data.status.success) {
          console.log('Fallo el update de contraseña')
        } else {
          console.log('Contraseña actualizada')
        }
      }).catch(() => {
        console.log('Hubo un error inesperado')
      })
  }
}
