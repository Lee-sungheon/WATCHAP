<template>
  <div>
    <button v-if="isLike" class="btn btn-link" style="color: crimson;" @click="likeMovie" >
      <i class="fas fa-heart fa-2x"></i>
    </button>
    <button v-else class="btn btn-link" style="color: crimson;" @click="likeMovie" >
      <i class="far fa-heart fa-2x"></i>
    </button>
    <span> {{ like_movie_len }} Users like this movie!</span>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieLike',
  data: function () {
    return {
      like_movie: this.movie.like_users,
      like_movie_len: this.movie.like_users.length,
      isLike: false
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
    likeMovie: function () {
      const config = this.setToken()
      const movieItem = {
        like_users: this.like_users
      }
      axios.post(`${SERVER_URL}/movies/${this.movie.id}/like_movie/`, movieItem, config)
        .then(() => {
          this.$emit('refresh_movie')
          this.isLike = !this.isLike
          if (this.isLike) {
            this.like_movie_len += 1
          } else {
            this.like_movie_len -= 1
          }
        })
        .catch((err) => { 
          console.log(err)
        })
    },
    update_like: function () {
      for (var i in this.like_movie) {
        for (var user of this.$store.state.users) {
          if (this.like_movie[i] == user.id){
            this.like_movie[i] = user.username
          }
        }
      }
      for (var j in this.like_movie) {
        if (this.like_movie[j] == this.$store.state.username) {
          return this.isLike = true
        }
      }
      this.isLike = false
    }
  },
  created: function () {
      this.update_like()
  },
  watch: {
    movie: function () {
      if (localStorage.getItem('jwt')) {
        this.like_movie = this.movie.like_users,
        this.like_movie_len = this.movie.like_users.length
        this.update_like()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  },
}
</script>

<style>

</style>