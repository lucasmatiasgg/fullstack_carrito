<template>
  <div v-if="productsData.length !== 0" class="q-pa-md items-start q-gutter-md">
      <h5>Carrito de compras</h5>
      <div class="row ">
      <CartProducts
          v-for="data in productsData"
          :key="data.idProduct"
          v-bind="data"/>
      </div>
      <div class="row justify-center">
          <q-btn v-on:click="buyOrder" label="Ir al resumen de compra" color="negative" />
      </div>
      <div class="row justify-center">
          <q-btn v-on:click="goBack" label="Volver" color="secondary" />
      </div>
  </div>

  <div v-else>
    <div class="row">
      <h5>En este momento no tenés articulos en tu carrito de compras</h5>
    </div>
    <div class="row">
        <q-btn v-on:click="goBack" label="Volver" color="secondary" />
    </div>
  </div>

</template>

<script>
import CartProducts from 'components/CartProducts.vue'
import { LOAD_PRODUCTS_FROM_CART } from '../store/cart/types'

export default {
  name: 'Cart',
  components: { CartProducts },
  data () {
    return {
      // productsData
      // userName: null
    }
  },
  mounted: function () {
    console.log('CART - MOUNTED')
    const idCart = this.$store.state.cart.idCart
    console.log('cartId:' + idCart)
    this.$store.dispatch(LOAD_PRODUCTS_FROM_CART, { idCart })
  },
  computed: {
    productsData: function () {
      return this.$store.state.cart.productCartList
    }
  },
  methods: {
    goBack () {
      this.$router.push('/desktop')
    },
    buyOrder () {
      this.$router.push('/BuyOrder')
    }
  }
}
</script>
