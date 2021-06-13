<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <!-- <img src={{logo}}> -->
          </q-avatar>
          Changos! shop
        </q-toolbar-title>

        <q-btn flat round dense icon="shopping_cart" @click="handleShoppingClick" class="q-mr-sm" />

        <q-btn flat round dense icon="logout" @click="handleLogout" class="q-mr-sm" />
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" behavior="desktop" elevated>
      <q-scroll-area class="fit">
          <q-list>
            <template v-for="(menuItem, index) in menuList">
              <q-item :key="index" clickable :active="menuItem.label === 'Outbox'" v-ripple>
                <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                </q-item-section>
                <q-item-section v-on:click="handleClick(menuItem.label)">
                  {{ menuItem.label }}
                </q-item-section>
              </q-item>
              <q-separator :key="'sep' + index"  v-if="menuItem.separator" />
            </template>

          </q-list>
        </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>

const menuList = [
  {
    icon: 'settings',
    label: 'Preferencias',
    separator: true
  }
]

export default {
  data () {
    return {
      left: false,
      menuList
    }
  },
  methods: {
    handleShoppingClick: function (event) {
      this.$router.push('/cart')
    },
    handleLogout: function (event) {
      // ACA TENTEMOS QUE LIMIAR EL STORE
      this.$router.push('/')
    },
    handleClick: function (name) {
      console.log(name)
      if (name === 'Preferencias') {
        alert('Aca hay que redirigir a preferencias')
      }
    }
  }
}
</script>
