<template>
  <b-overlay :show="isHovered" v-b-hover="handleHover">
    <img :src="movie.poster_path" alt="" style="height: 18rem; max-width: 100%;"/>
      <template #overlay>
      <div class="text-center">
        <p class="font-weight-bold">{{movie.title}}</p>
        <span v-for="(avg, i) in Math.round(movie.vote_average)" :key="i">
          <span v-if="i%2">
            <i class="fas fa-star" style="color: red"></i>
          </span>
        </span>
        <span v-if="Math.round(movie.vote_average)%2 === 1">
          <i class="fas fa-star-half" style="color: red"></i>
        </span><hr>
        <b-button
          ref="detail"
          variant="outline-primary"
          size="sm"
          @click="isDetail"
        >
          Detail
        </b-button>
      </div>
    </template>
  </b-overlay>
</template>

<script>
export default {
  name: "PopularItem",
  props: {
    movie: Object,
  },
  data: function () {
    return {
      isHovered: false,
      show: false,
      detail: false,
    }
  },
  methods: {
    handleHover(hovered) {
      this.isHovered = hovered
    },
    isDetail: function () {
      this.$emit('isdetail',this.movie)
    }
  }
}
</script>

<style>

</style>