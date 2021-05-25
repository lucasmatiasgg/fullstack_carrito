<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <!-- <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg"> -->
          </q-avatar>
          Carrito de Compras
        </q-toolbar-title>

        <q-btn flat round dense icon="shopping_cart" @click="handleShoppingClick" class="q-mr-sm" />

        <q-btn flat round dense icon="account_circle" @click="handleUserClick" class="q-mr-sm" />
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" behavior="desktop" elevated>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      left: false
    }
  },
  methods: {
    handleShoppingClick: function (event) {
      alert('Shopping Action!')
      console.log(event)
    },
    handleUserClick: function (event) {
      alert('User Action!')
      console.log(event)
    }
  }
}
</script>
