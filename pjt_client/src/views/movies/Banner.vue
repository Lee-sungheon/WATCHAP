<template>
  <v-carousel hide-delimiter-background cycle class="my-5" height="auto">
    <v-carousel-item
      v-for="(item,i) in items"
      :key="i"
    >
      <img :src="item.src" alt="" style="max-width: 100%; width: 100%;">
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "banner",
  data () {
    return {
      items: [
        {
          src: 'https://i.ibb.co/kx6WN39/banner-4.png',
        },
        {
          src: 'https://i.ibb.co/37qZ7J5/banner3.jpg',
        },
        {
          src: 'https://i.ibb.co/zVWsvqj/banner1.png',
        },
        {
          src: 'https://i.ibb.co/yfCJckq/banner2.png',
        },
      ],
    }
  }
}
</script>

<style>

</style>