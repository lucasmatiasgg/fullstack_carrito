<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" >
      <q-img src="https://cdn.quasar.dev/img/mountains.jpg" />

      <q-card-section>
        <div class="text-h6">{{title}}</div>
        <div class="text-subtitle2">{{subtitle}}</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        {{ description }}
      </q-card-section>
    </q-card>

  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      default: 'Subtitulo'
    },
    description: {
      type: String,
      default: 'description'
    },
    image: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
