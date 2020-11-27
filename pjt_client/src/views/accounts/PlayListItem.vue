<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      controls
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <span v-for="(movie, idx) in playList" :key="idx">
        <MovieItem :movie="movie" @isdetail="goDetail"/>
      </span>
      <div v-if="playList.length === 0" style="width: 344px; height: 516px;" class="d-flex justify-content-center align-items-center">
        <h4><i class="fas fa-exclamation-triangle"></i>추천 영화가 없어요!</h4>
      </div>
    </b-carousel>
    <div v-if="movie">
      <hr>
      <MovieDetail :movie="movie" :dialog="dialog" @close_detail="closeDetail"/>
    </div>
  </div>
</template>

<script>
import MovieItem from "@/views/accounts/MovieItem"
import MovieDetail from '@/views/movieList/MovieDetail'

export default {
  name: "PlayListItem",
  components: {
    MovieItem,
    MovieDetail,
  },
  props: {
    playList: Array,
  },
  data() {
    return {
      slide: 0,
      sliding: null,
      movie: [],
      dialog: null,
    }
  },
  methods: {
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
    goDetail: function (movie) {
      this.movie = movie
      this.dialog = true
    },
    closeDetail: function () {
      this.dialog = false
    },
  }
}
</script>

<style>

</style>