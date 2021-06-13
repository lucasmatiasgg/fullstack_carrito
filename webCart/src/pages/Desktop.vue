<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <CardProducts
        v-for="data in productsData"
        :key="data.title"
        v-bind="data"/>
  </div>
</template>

<script>
import CardProducts from 'components/CardProducts.vue'
// import { LOAD_USER_INFO } from '../store/user/types'
import { LOAD_PRODUCTS } from '../store/product/types'

export default {
  name: 'Desktop',
  components: { CardProducts },
  data () {
    return {
      // productsData
      // userName: null
    }
  },
  mounted: function () {
    console.log('MOUNTED')
    // this.$store.dispatch(LOAD_USER_INFO).then(() => {
    this.$store.dispatch(LOAD_PRODUCTS)
    // })
  },
  computed: {
    firstName: function () {
      return this.$store.state.user.firstName
    },
    productsData: function () {
      return this.$store.state.product.productList
    }
  }
}
</script>
