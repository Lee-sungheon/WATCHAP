<template>
  <div>
    <span style="cursor:pointer;" @click="follow">
      <i v-if="isFollow" class="fas fa-user-minus fa-2x" style="color: gray;"></i>
      <i v-else class="fas fa-user-plus fa-2x" style="color: crimson;"></i>
    </span><br><br>
    <p>followers: {{ followers_len }} </p>
    <p>follwings: {{ followings_len }} </p>
    <hr>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "ProfileFollow",
  data: function () {
    return {
      isFollow: false,
      followers_len: 0,
      followings_len: 0
    }
  },
  props: {
    profile: {},
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
    follow: function () {
      const config = this.setToken()
      const followItem = {
        follow: this.isFollow
      }
      axios.post(`${SERVER_URL}/accounts/${this.profile.username}/follow/`, followItem, config)
        .then((res) => {
          if (res.data.detail !== '본인을 팔로우 할 수 없습니다.'){
            this.isFollow = !this.isFollow
            if (this.isFollow) {
              this.followers_len += 1
            } else {
              this.followers_len -= 1
            }
            this.$emit('refresh_profile')
          }
          else {
            window.alert('본인을 팔로우 할 수 없습니다.')
          }
        })
        .catch((err) => { 
          console.log(err)
        })
    },
  },
  watch: {
    profile: function () {
      this.isFollow = false,
      this.followers_len = this.profile.followers.length,
      this.followings_len = this.profile.followings.length
    }
  } 

}
</script>

<style>

</style>