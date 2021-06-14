<template>
  <div class="q-pa-md" style="max-width:100%">
    <div class="row justify-center">
      <q-form
        @submit="registerUser"
        @reset="onReset"
        class="q-gutter-md"
        spellcheck="false">

        <q-input
          filled
          v-model="firstName"
          label="Nombre"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
        />
        <q-input
          filled
          v-model="lastName"
          label="Apellido"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
        />

        <q-input
          filled
          v-model="userName"
          label="Usuario"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
        />

        <q-input
          filled
          v-model="password"
          label="Password"
          :rules="[ val => val && val.length > 0 || 'Este campo es obligatorio']"
        />

        <div class="row justify-center">
          <q-btn label="Registrarse" type="submit" color="secondary"/>
        </div>
        <div class="row justify-center">
          <q-btn v-on:click="goBack" label="Volver" color="secondary" />
        </div>

      </q-form>
    </div>
  </div>
</template>

<script>
import { api } from 'boot/axios'

export default {
  name: 'Register',
  data () {
    return {
      firstName: null,
      lastName: null,
      userName: null,
      password: null
    }
  },
  methods: {
    registerUser () {
      api.post('/users/create', {
        firstName: this.firstName,
        lastName: this.lastName,
        userName: this.userName,
        password: this.password
      })
        .then((response) => {
          if (!response.data.success) {
            this.$q.notify({
              color: 'negative',
              position: 'top',
              message: response.data.message,
              icon: 'report_problem'
            })
          } else {
            this.$router.push('/')
            this.$q.notify({
              color: 'positive',
              position: 'top',
              message: response.data.message,
              icon: 'check_circle'
            })
          }
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Ocurrió un error genérico',
            icon: 'report_problem'
          })
        })
    },
    goBack () {
      this.$router.push('/')
    }
  }
}
</script>
