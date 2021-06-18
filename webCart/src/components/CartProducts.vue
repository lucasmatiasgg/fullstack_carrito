<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" >
      <q-img :src="imageSource" height="200px" width="200px"/>
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
        <q-btn v-on:click="removeProductFromCart(idCart, idProduct)" flat>Eliminar</q-btn>
      </q-card-actions>
    </q-card>

  </div>
</template>

<script>
import { DELETE_PRODUCT_FROM_CART } from '../store/cart/types'
export default {
  data () {
    return {
      imageSource: this.$props.image
    }
  },
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
    },
    idProduct: {
      type: Number,
      required: true
    }
  },
  computed: {
    idCart: function () {
      return this.$store.state.cart.idCart
    }
  },
  methods: {
    removeProductFromCart (idCart, idProduct) {
      const data = { idCart, idProduct }
      console.log('REMOVE PRODUCT:' + idCart + '-' + idProduct)
      this.$store.dispatch(DELETE_PRODUCT_FROM_CART, { data }).then(() => {
        this.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Producto eliminado',
          icon: 'check_circle'
        })
      }
      )
    }
  }
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
