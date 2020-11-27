<template>
  <div class="mx-5">
    <h2 class="text-left ml-2 text-white">Popular Movie</h2>
    <hooper :settings="hooperSettings" style="height: 18rem">
      <slide v-for="(movie, i) in movies" :key="i">
        <PopularItem :movie="movie" @isdetail="goDetail"/>
      </slide>
      <hooper-navigation slot="hooper-addons"></hooper-navigation>
      <hooper-pagination slot="hooper-addons"></hooper-pagination>
    </hooper>

    <div v-if="movie">
      <hr>
      <MovieDetail :movie="movie" @closedetail="closeDetail" @refresh="refreshMovies"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {
  Hooper, 
  Slide,
  Pagination as HooperPagination,
  Navigation as HooperNavigation
} from 'hooper'
import 'hooper/dist/hooper.css'
import PopularItem from '@/views/movies/PopularItem'
import MovieDetail from '@/views/movies/MovieDetail'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "PopularMovie",
  components: {
    Hooper,
    Slide,
    HooperPagination,
    HooperNavigation,
    PopularItem,
    MovieDetail,
  },
  data: function () {
    return {
      movies: [],
      hooperSettings: {
        itemsToShow: 6,
        itemsToSlide: 3,
        infiniteScroll: "true",
        detail: "true",
        wheelControl: false,
      },
      movie: '',
    }
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },

    getMovies: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/`, config)
        .then((res) => {
          this.movies = res.data.filter( movie => {
            return movie.popularity >= 400
          })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goDetail: function (movie) {
      this.movie = movie
    },
    closeDetail: function () {
      this.movie = ''
    },
    refreshMovies: function () {
      this.getMovies()
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>


<style>
</style>