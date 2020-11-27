<template>
  <div class="my-5">
    <br>
    <Banner />
    <PopularMovie />
    <LatestMovie />
    <UpcomingMovie />
  </div>
</template>

<script>
import PopularMovie from '@/views/movies/PopularMovie'
import LatestMovie from '@/views/movies/LatestMovie'
import UpcomingMovie from '@/views/movies/UpcomingMovie'
import Banner from '@/views/movies/Banner'

export default {
  name: 'Home',
  components: {
    PopularMovie,
    Banner,
    LatestMovie,  
    UpcomingMovie,
  }
}
</script>

<style>

</style>