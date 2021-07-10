<template>
    <div>
        <h5>Modificar datos de usuario</h5>
        <div class="q-pa-md" style="max-width:100%">
            <div class="row justify-center">
                <q-form
                    @submit="updateData()"
                    @reset="onReset"
                    class="q-gutter-md"
                    spellcheck="false">

                    <q-input
                    filled
                    v-model="firstName"
                    label="Nuevo nombre"
                    lazy-rules
                    :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
                    />
                    <q-input
                    filled
                    v-model="lastName"
                    label="Nuevo apellido"
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
import { LOAD_USER_INFO, UPDATE_USER_DATA } from '../store/user/types'

export default {
  name: 'Preferences',
  data () {
    return {
      firstName: this.$store.state.user.firstName,
      lastName: this.$store.state.user.lastName,
      oldPassword: null
    }
  },
  mounted: function () {
    const userId = this.$store.state.user.userId
    console.log('Estoy en mounted')
    this.$store.dispatch(LOAD_USER_INFO, { userId })
  },
  methods: {
    updateData () {
      const userId = this.$store.state.user.userId
      const data = {
        firstName: this.firstName,
        lastName: this.lastName,
        oldPassword: this.oldPassword,
        userId
      }
      console.log('Preference userid: ' + userId)
      this.$store.dispatch(UPDATE_USER_DATA, { data }).then(() => {
        this.$q.notify({
          color: 'positive',
          position: 'top',
          message: 'Usuario actualizado',
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
