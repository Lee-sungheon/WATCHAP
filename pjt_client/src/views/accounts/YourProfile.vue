<template>
  <div class="px-3 pt-5 pb-2">
    <h5>{{ profile.username }}</h5>
    <b-avatar :src="profile.profileurl" size="10rem"></b-avatar>
    <h6>{{ profile.email }}</h6>
    <hr>
    <YourProfileFollow :profile="profile" @refresh_profile="refreshProfile"/>
    <h5>PlayList</h5>
    <YourPlayList :profile="profile"/>
  </div>
</template>

<script>
import axios from 'axios'
import YourProfileFollow from '@/views/accounts/YourProfileFollow'
import YourPlayList from '@/views/accounts/YourPlayList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "YourProfile",
  components: {
    YourProfileFollow,
    YourPlayList,
  },
  data: function () {
    return {
      profile: []
    }
  },
  props: {
    user: String,
  },
  methods: {
    getProfile: function () {
      if (this.user) {
        axios.get(`${SERVER_URL}/accounts/${this.user}/`)
          .then((res) => {
            this.profile = res.data
            this.$emit('getprofile', this.profile)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    refreshProfile: function () {
      this.$store.dispatch('refreshProfile')
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.getProfile()
    }
  },
  computed: {
    getRefresh () {
        return this.$store.state.refresh
    }
  },
  watch: {
    user: function () {
      this.getProfile()
    },
    getRefresh: function () {
      this.getProfile()
    }
  },
}
</script>

<style>

</style>