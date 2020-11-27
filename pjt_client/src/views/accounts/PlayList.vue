<template>
  <div>
    <ul>
      <li v-for="(movie, idx) in playList" :key="idx">
        {{ movie.title }}  
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: "PlayList",
  data: function () {
    return {
      movies: this.$store.state.movies,
      playList: []
    }
  },
  props: {
    profile: {}
  },
  methods: {
    getPlaylist: function () {
      for (const movie of this.movies) {
        for (const user of movie.users_playlist) {
          if (this.profile.id == user) {
            this.playList.push(movie)
            break
          }
        }
      }
    },
  },
  mounted: function () {
    this.playList = []
    this.getPlaylist()
  },
  watch: {
    profile: function () {
      this.playList = []
      this.getPlaylist()
    }
  }
}
</script>

<style>

</style>