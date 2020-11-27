<template>
  <div class="d-flex justify-content-start">
    <ul>
      <li v-for="(comment, idx) in review_comments" :key="idx" style="text-align: left;">
        {{ comment.user }} : {{ comment.content }}
        <i class="fas fa-times" style="color: crimson;" v-if="comment.user === user" @click="deleteReviewComment(comment)"></i>
      </li> 
    </ul>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "ReviewCommentList",
  data: function () {
    return {
      review_comments: [],
      user: this.$store.state.username,
      review_comment_length: 0,
    }
  },
  props: {
    review: Object,
    refresh: Boolean,
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
    getReviewComments: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/${this.review.id}/list_create_review_comment/`, config)
        .then((res) => {
          this.review_comments = res.data
          for (var comment of this.review_comments) {
            for (var user of this.$store.state.users) {
              if (comment.user == user.id){
                comment.user = user.username
              }
            }
          }
          this.getReviewCommentLength()
          this.$emit("refresh_review_comment", this.review_comment_length)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReviewComment: function (comment) {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/movies/delete_review_comment/${comment.id}/`, config)
        .then((res) => {
          const targetCommentIdx = this.review_comments.findIndex((comment) => {
            return comment.id === res.data.id
          })
          this.review_comments.splice(targetCommentIdx, 1)
          this.getReviewCommentLength()
          this.$emit("refresh_review_comment", this.review_comment_length)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReviewCommentLength: function () {
      this.review_comment_length = this.review_comments.length
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviewComments()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
  watch: {
    refresh: function () {
      if (localStorage.getItem('jwt')) {
        this.getReviewComments()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
    review: function () {
      if (localStorage.getItem('jwt')) {
        this.getReviewComments()
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  },
}
</script>

<style>

</style>