<template>
  <div class="q-pa-md" style="max-width:100%">
    <div class="row justify-center">
      <q-form
        @submit="loadData"
        @reset="onReset"
        class="q-gutter-md"
        spellcheck="false">

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
          <q-btn label="Ingresar" type="submit" color="secondary"/>
        </div>
        <div class="row justify-center">
          <q-btn v-on:click="goToRegister" label="Registrarse" color="secondary" />
        </div>

      </q-form>
    </div>
  </div>
</template>

<script>
import { api } from 'boot/axios'

export default {
  name: 'Login',
  data () {
    return {
      userName: null,
      password: null,
      accept: false
    }
  },
  methods: {
    goToRegister () {
      this.$router.push('/register')
    },
    loadData () {
      api.post('/users/validateCredentials', {
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
            this.$router.push('/desktop')
            // this.data = response.data
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
}
</script>
