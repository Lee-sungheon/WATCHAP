<template>
  <b-row>
    <v-col cols="12" md="12">
      <v-text-field
        v-model="comment"
        :counter="100"
        label="Comment"
        required
        dark
        @keypress.enter="createToReviewComment"
      ></v-text-field>
    </v-col>
  </b-row>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "CreateToReviewComment",
  props: {
    review: Object,
  },
  data: function () {
    return {
      comment: '',
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
    createToReviewComment: function () {
      const config = this.setToken()
      
      const ReviewComment = {
        review: this.review.id,
        content: this.comment,
      }
      if (ReviewComment.content) {
        axios.post(`${SERVER_URL}/movies/${this.review.id}/list_create_review_comment/`, ReviewComment, config)
          .then(() => {
            this.$emit('refresh')
            this.comment = ''
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