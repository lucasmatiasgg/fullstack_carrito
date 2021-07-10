<template>
    <div>
        <h5>Modificar contraseña</h5>
        <div class="q-pa-md" style="max-width:100%">
            <div class="row justify-center">
                <q-form
                    @submit="updatePassword()"
                    @reset="onReset"
                    class="q-gutter-md"
                    spellcheck="false">

                    <q-input
                    filled
                    v-model="newPassword"
                    type="password"
                    label="Nueva contraseña"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
                    />

                    <q-input
                    filled
                    v-model="oldPassword"
                    type="password"
                    label="Contraseña actual"
                    :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
                    />

                    <div class="row justify-center">
                    <q-btn label="Aceptar" type="submit" color="secondary"/>
                    </div>
                    <div class="row justify-center">
                    <q-btn v-on:click="goBack" label="Volver" color="secondary" />
                    </div>

                </q-form>
            </div>
        </div>
    </div>
</template>

<script>
import { UPDATE_PASSWORD } from '../store/user/types'

export default {
  name: 'ChangePassword',
  data () {
    return {
      newPassword: null,
      oldPassword: null
    }
  },

  methods: {
    updatePassword () {
      const userId = this.$store.state.user.userId
      const data = {
        newPassword: this.newPassword,
        oldPassword: this.oldPassword,
        userId
      }
      console.log('Change password - userid: ' + userId)
      this.$store.dispatch(UPDATE_PASSWORD, { data }).then(() => {
        this.$q.notify({
          color: 'positive',
          position: 'top',
          message: 'Password actualizada',
          icon: 'check_circle'
        })
      })
    },
    goBack () {
      this.$router.push('/desktop')
    }
  }
}
</script>
