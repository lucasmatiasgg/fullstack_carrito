<template>
  <div v-if="productCartList !== []" class="q-pa-md row items-start q-gutter-md">
      <CartProducts
          v-for="data in productsData"
          :key="data.name"
          v-bind="data"/>
      <div class="row justify-center">
          <q-btn v-on:click="buyOrder" label="Finalizar Compra" color="negative" />
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
    console.log('MOUNTED')
    this.$store.dispatch(LOAD_PRODUCTS_FROM_CART)
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
      console.log('Compra realizada!')
    }
  }
}
</script>
