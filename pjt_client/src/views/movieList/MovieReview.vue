<template>
  <div class="mt-5">
    <CreateToMovieReview :movie="movie" @refresh_emit="refreshList"/>
    <h5>All Review</h5>

    <div v-for="(review, idx) in movie_reviews" :key="idx" style="margin: 2% 20%;">
      <MovieReviewList :review="review" :movie="movie" @refresh_delete="refreshList"/>
    </div>
    <div v-if="movie_reviews.length === 0" style="height: 200px;" class="d-flex justify-content-center align-items-center">
      <h3>작성된 리뷰가 없습니다.</h3>
    </div>
  </div>
</template>

<script>
import CreateToMovieReview from '@/views/movieList/CreateToMovieReview'
import MovieReviewList from '@/views/movieList/MovieReviewList'
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieReview",
  components: {
    CreateToMovieReview,
    MovieReviewList,
  },
  data: function () {
    return {
      movie_reviews: [],
      refresh: 0,
    }
  },
  props: {
    movie: Object,
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
    getReviews: function () {
      const config = this.setToken()
      
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/list_create_movie_review/`, config)
        .then((res) => {
          this.movie_reviews = res.data
          for (var review of this.movie_reviews) {
            for (var user of this.$store.state.users) {
              if (review.user == user.id){
                review.user = user.username
              }
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    refreshList: function () {
      this.refresh += 1
    }
  },
  watch: {
    refresh: function () {
      if (localStorage.getItem('jwt')) {
        this.getReviews()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
    movie: function () {
      if (localStorage.getItem('jwt')) {
        this.getReviews()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>

</style>