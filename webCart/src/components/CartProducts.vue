<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" >
      <q-img src="https://cdn.quasar.dev/img/mountains.jpg" />

      <q-card-section>
        <div class="text-h6">{{name}}</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        Precio unitario: ${{ price }}
      </q-card-section>
      <q-card-section class="q-pt-none">
        Cantidad: {{ quantity }}
      </q-card-section>
      <q-card-section class="q-pt-none">
        Total: ${{ amount }}
      </q-card-section>
      <q-card-actions>
        <q-btn v-on:click="removeProductFromCart(name)" flat>Eliminar</q-btn>
      </q-card-actions>
    </q-card>

  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true
    },
    price: {
      type: Number,
      default: 0
    },
    quantity: {
      type: Number,
      default: 0
    },
    amount: {
      type: Number,
      default: 0
    },
    image: {
      type: String,
      default: 'https://cdn.quasar.dev/img/mountains.jpg'
    }
  },
  methods: {
    removeProductFromCart (name) {
      alert('REMOVE:' + name)
    }
  }
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
