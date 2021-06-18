<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" >
      <q-img :src="imageSource" height="200px" width="200px"/>
      <!-- <img :src="imageSource"/> -->
      <q-card-section>
        <div class="text-h6">{{name}}</div>
        <div class="text-subtitle2">{{description}}</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        ${{ price }}
      </q-card-section>
      <div class="q-pa-md">
        <q-input
          label="Cantidad"
          v-model.number="quantity"
          type="number"
          filled
          style="max-width: 100px"
        />
      </div>
      <q-card-actions>
        <q-btn v-on:click="addProductToCart(productId, quantity, userId)" flat color="secondary">Agregar al carrito</q-btn>
      </q-card-actions>
    </q-card>

  </div>
</template>

<script>
import { ADD_PRODUCT_TO_CART } from '../store/cart/types'
export default {
  data () {
    return {
      quantity: 1,
      userId: this.$store.state.user.userId,
      imageSource: this.$props.image
    }
  },
  props: {
    productId: {
      type: Number,
      default: 0
    },
    name: {
      type: String,
      required: true
    },
    description: {
      type: String,
      default: 'description'
    },
    price: {
      type: Number,
      default: 0
    },
    image: {
      type: String,
      default: 'https://cdn.quasar.dev/img/mountains.jpg'
    }
  },
  methods: {
    addProductToCart (productId, quantity, userId) {
      const data = { productId, quantity, userId }
      console.log('ANTES DE HACER DISPATCH addProductToCart')
      console.log(data.productId + ' - ' + data.quantity)
      this.$store.dispatch(ADD_PRODUCT_TO_CART, { data }).then(() => {
        this.$q.notify({
          color: 'positive',
          position: 'top',
          message: 'Producto agregado',
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
