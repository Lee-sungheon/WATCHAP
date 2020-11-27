<template>
  <div>
    <button v-if="isSelect" class="btn btn-link" style="color: blue;" @click="selectMovie" >
      <i class="far fa-play-circle fa-2x"></i>
    </button>
    <button v-else class="btn btn-link" style="color: gray;" @click="selectMovie" >
      <i class="far fa-play-circle fa-2x"></i>
    </button>
    <span> {{ select_movie_len }} Users Select this movie!</span>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieSelect",
  data: function () {
    return {
      select_movie: this.movie.users_playlist,
      select_movie_len: this.movie.users_playlist.length,
      isSelect: false
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
    selectMovie: function () {
      const config = this.setToken()
      const movieItem = {
        select_users: this.select_users
      }
      axios.post(`${SERVER_URL}/movies/${this.movie.id}/select_movie/`, movieItem, config)
        .then(() => {
          this.$emit('refresh_movie')
          this.isSelect = !this.isSelect
          if (this.isSelect) {
            this.select_movie_len += 1
          } else {
            this.select_movie_len -= 1
          }
        })
        .catch((err) => { 
          console.log(err)
        })
    },
    update_select: function () {
      for (var i in this.select_movie) {
        for (var user of this.$store.state.users) {
          if (this.select_movie[i] == user.id){
            this.select_movie[i] = user.username
          }
        }
      }
      for (var j in this.select_movie) {
        if (this.select_movie[j] == this.$store.state.username) {
          return this.isSelect = true
        }
      }
      this.isSelect = false
    }
  },
  created: function () {
    this.update_select()
  },
  watch: {
    movie: function () {
      if (localStorage.getItem('jwt')) {
        this.select_movie = this.movie.users_playlist,
        this.select_movie_len = this.movie.users_playlist.length
        this.update_select()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  },
}
</script>

<style>

</style>