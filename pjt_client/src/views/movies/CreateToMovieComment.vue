<template>
  <div>
    <v-row>
      <v-col cols="12" md="3" style="line-height: 60px;">
        <v-rating v-model="rating" color="yellow darken-3" background-color="grey darken-1" dense half-increments hover size="18">
        </v-rating>
      </v-col>
      <v-col cols="12" md="9">
        <v-text-field
          v-model="comment"
          :counter="50"
          label="Comment"
          required
          dark
          @keypress.enter="createToMovieComment"
        ></v-text-field>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "CreateToMovieComment",
  data: function () {
    return {
      comment: '',
      rating: 5,
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
    createToMovieComment: function () {
      const config = this.setToken()
      
      const MovieComment = {
        movie: this.movie.id,
        content: this.comment,
        rank: this.rating * 2,
      }

      if (MovieComment.content) {
        axios.post(`${SERVER_URL}/movies/${this.movie.id}/list_create_movie_comment/`, MovieComment, config)
          .then(() => {
            this.$emit('refresh')
            this.comment = ''
            this.rating = 5
          })
          .catch((err) => { 
            console.log(err)
          })
        }
    }
  }
}
</script>

<style>

</style>