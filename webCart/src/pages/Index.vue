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

const productsData = [
  {
    title: 'Producto1',
    subtitle: 'Subtitulo1',
    description: 'Descripcion 1',
    image: 'https://cdn.quasar.dev/img/mountains.jpg'
  },
  {
    title: 'Producto2',
    subtitle: 'Subtitulo2',
    description: 'Descripcion 2',
    image: 'https://cdn.quasar.dev/img/mountains.jpg'
  },
  {
    title: 'Producto3',
    subtitle: 'Subtitulo3',
    description: 'Descripcion 3',
    image: 'https://cdn.quasar.dev/img/mountains.jpg'
  }
]

export default {
  name: 'PageIndex',
  components: { CardProducts },
  data () {
    return {
      productsData
    }
  }
}
</script>
