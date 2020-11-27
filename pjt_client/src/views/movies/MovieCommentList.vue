<template>
  <ul>
    <li v-for="(comment, idx) in movie_comments" :key="idx">
      {{ comment.user }} : {{ comment.content }} (
      <span v-for="(avg, i) in comment.rank" :key="i">
        <span v-if="i%2">
          <i class="fas fa-star" style="color: yellow"></i>
        </span>
      </span>
      <span v-if="Math.round(comment.rank)%2 === 1">
        <i class="fas fa-star-half" style="color: yellow"></i>
      </span>
      )

      <i class="fas fa-times" style="color: crimson;" v-if="comment.user === user" @click="deleteMovieComment(comment)"></i>

    </li>
  </ul>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieCommentList",
  data: function () {
    return {
      movie_comments: [],
      user: this.$store.state.username
    }
  },
  props: {
    movie: Object,
    refresh: Number,
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
    getMovieComments: function () {
      const config = this.setToken()
      
      axios.get(`${SERVER_URL}/movies/${this.movie.id}/list_create_movie_comment/`, config)
        .then((res) => {
          this.movie_comments = res.data
          
          for (var comment of this.movie_comments) {
            for (var user of this.$store.state.users) {
              if (comment.user == user.id){
                comment.user = user.username
              }
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteMovieComment: function (comment) {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/movies/delete_movie_comment/${comment.id}/`, config)
        .then((res) => {
          const targetCommentIdx = this.movie_comments.findIndex((comment) => {
            return comment.id === res.data.id
          })
          this.movie_comments.splice(targetCommentIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovieComments()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
  watch: {
    refresh: function () {
      if (localStorage.getItem('jwt')) {
        this.getMovieComments()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
    movie: function () {
      if (localStorage.getItem('jwt')) {
        this.getMovieComments()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  },
}
</script>

<style>

</style>