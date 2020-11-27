<template>
  <b-col style="border-right: solid white 1px; cursor:pointer;" @click="likeReview">
    <i v-if="isLike" class="fas fa-heart fa-lg mr-3" style="color: crimson;"></i>
    <i v-else class="far fa-heart fa-lg mr-3" style="color: crimson;"></i>
    <span style="font-size: 1rem">Like</span>
  </b-col>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "ReviewLike",
  data: function () {
    return {
      like_review: this.review.like_users,
      like_review_len: this.review.like_users.length,
      isLike: false
    }
  },
  props: {
    review: Object,
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
    likeReview: function () {
      const config = this.setToken()
      const reviewItem = {
        like_users: this.like_users
      }
      axios.post(`${SERVER_URL}/movies/${this.review.id}/like_review/`, reviewItem, config)
        .then(() => {
          this.isLike = !this.isLike
          if (this.isLike) {
            this.like_review_len += 1
          } else {
            this.like_review_len -= 1
          }
          this.$emit('refresh_review', this.like_review_len)
        })
        .catch((err) => { 
          console.log(err)
        })
    },
    update_like: function () {
      for (var i in this.like_review) {
        for (var user of this.$store.state.users) {
          if (this.like_review[i] == user.id){
            this.like_review[i] = user.username
          }
        }
      }
      for (var j in this.like_review) {
        if (this.like_review[j] == this.$store.state.username) {
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
    review: function () {
      if (localStorage.getItem('jwt')) {
        this.like_review = this.review.like_users,
        this.like_review_len = this.review.like_users.length
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