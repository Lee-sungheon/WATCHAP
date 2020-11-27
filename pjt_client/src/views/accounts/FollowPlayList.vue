<template>
  <div class="m-2">
    <v-card
      class="mx-auto"
      width="344"
    >
      <v-img
        :src="profile.profileurl"
        height="300px"
        style="max-width: 100%;"
      ></v-img>
      <v-card-title class="d-flex justify-content-center">
        # {{ profile.username }} 님의 플레이 리스트
      </v-card-title>
      <v-card-actions>
        <v-btn
          color="orange lighten-2"
          text
        >
          살펴보기
        </v-btn>
        <v-btn
          icon
          @click="show = !show"
        >
          <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn>
      </v-card-actions>
      <v-expand-transition>
        <div v-show="show">
          <PlayListItem :playList="playList" />
        </div>
      </v-expand-transition>
    </v-card>
  </div>
</template>

<script>
import PlayListItem from "@/views/accounts/PlayListItem"
export default {
  name: "FollowPlayList",
  components: {
    PlayListItem,
  },
  data: function (){
    return {
      show: false,
      movies: this.$store.state.movies,
      users: this.$store.state.users,
      playList: [],
      profile: [],
    }
  },
  props: {
    following: Number
  },
  methods: {
    getPlaylist: function () {
      for (const movie of this.movies) {
        for (const user of movie.users_playlist) {
          if (this.following === user) {
            this.playList.push(movie)
            break
          }
        }
      }
    },
    getProfile: function () {
      for (const user of this.users) {
        if (this.following === user.id) {
          this.profile = user
          break
        }
      }
    }
  },
  mounted: function () {
    this.getPlaylist()
    this.getProfile()
  },
  watch: {
    profile: function () {
      this.getPlaylist()
      this.getProfile()
    }
  }
}
</script>

<style>

</style>