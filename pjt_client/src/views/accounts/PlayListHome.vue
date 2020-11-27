<template>
  <div class="mt-5 ml-5">
    <br><br><br>
    <h2 class="text-left ml-2 text-white">Play List</h2>
    <hr style="border: solid 1px white;">
    <h5 class="text-left ml-2 text-white">내 친구의 플레이 리스트를 엿보세요!</h5>

    <div class="mx-2 d-flex flex-wrap justify-content-center align-items-center">
      <div>
        <FollowPlayList :following="profile.id" />
      </div>
      <div v-for="(following, idx) in followings" :key="idx">
        <FollowPlayList :following="following" />
      </div>
    </div>

  </div>


</template>

<script>
import FollowPlayList from '@/views/accounts/FollowPlayList'

export default {
  name: 'PlayListHome',
  components: {
    FollowPlayList,
  },
  data: function () {
    return {
      profile: {},
      followings: [],
    }
  },
  created: function () {
    this.profile = this.$store.state.profile
    this.followings = this.profile.followings
  }
}
</script>

<style>

</style>