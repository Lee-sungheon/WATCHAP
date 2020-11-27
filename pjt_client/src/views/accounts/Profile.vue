<template>
  <div class="px-3 py-2">
    <h5>{{ profile.username }}</h5>
    <b-avatar :src="profile.profileurl" size="10rem"></b-avatar>
    <h6>{{ profile.email }}</h6>
    <hr>
    <ProfileFollow :profile="profile" @refresh_profile="refreshProfile"/>
    <h5>PlayList</h5>
    <PlayList :profile="profile"/>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileFollow from '@/views/accounts/ProfileFollow'
import PlayList from '@/views/accounts/PlayList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Profile",
  components: {
    ProfileFollow,
    PlayList,
  },
  data: function () {
    return {
      profile: [],
      refresh: this.$store.state.refresh
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
            this.$store.dispatch('getprofile', res.data)
            this.profile = this.$store.state.profile
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    refreshProfile: function () {
      this.getProfile()
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