<template>
    <div class="q-pa-md items-start q-gutter-md">
        <h5>
            Orden de compra
        </h5>
        <div class="q-pa-md">
          <q-table
            title="Resumen de compra"
            :data="productsData"
            :columns="columns"
            row-key="name"
          />
        </div>
        <div>
          <h5 class="row justify-center">
            Total: ${{ total(productsData) }}
          </h5>
        </div>
        <div class="row justify-center">
          <q-btn label="Finalizar compra" type="submit" color="negative"/>
          </div>
          <div class="row justify-center">
          <q-btn v-on:click="goBack" label="Volver al carrito" color="secondary" />
          </div>
    </div>
</template>

<script>
const columns = [
  {
    name: 'name',
    label: 'Producto',
    align: 'left',
    field: 'name'
  },
  {
    name: 'quantity',
    label: 'Cantidad',
    align: 'left',
    field: 'quantity'
  },
  {
    name: 'amount',
    label: 'Monto ($)',
    align: 'left',
    field: 'amount'
  },
  {
    name: 'price',
    label: 'Precio unitario ($)',
    align: 'left',
    field: 'price'
  }
]
export default {
  data () {
    return {
      columns
    }
  },
  computed: {
    productsData: function () {
      return this.$store.state.cart.productCartList
    }
  },
  methods: {
    goBack () {
      this.$router.push('/cart')
    },
    total (productsData) {
      let total = 0
      for (let i = 0; i < productsData.length; i++) {
        total = total + productsData[i].amount
      }
      return total
    }
  }
}
</script>
