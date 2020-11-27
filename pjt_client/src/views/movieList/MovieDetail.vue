<template>
  <v-row justify="center">
    
    <v-dialog
      v-model="dialog"
      hide-overlay
      transition="dialog-top-transition"
    >
      <v-card style="margin-top: 5%;" color="gba(255, 255, 255, 0.5)" dark>
        <v-toolbar
          dark
          color="gba(255, 255, 255, 0.5) accent-4"
        >
        <v-tabs centered class="pl-5">
          <v-tab @click="tap=true">Detail</v-tab>
          <v-tab @click="tap=false">Review</v-tab>
        </v-tabs>
          <v-toolbar-items class="d-flex justify-content-end">
            <v-btn
            icon
            dark
            @click="closeDetail"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>

        <div class="container text-left my-2" v-if="tap">
          <div class="row">
            <div class="col-sm">
              <h1> {{ movie.title }} </h1>
              <hr class="my-4">
              <p>평점 : {{ movie.vote_average }}</p>
              <p>개봉일 : {{ movie.release_date }}</p>
              <p>장르 : <span v-for="(gen, idx) in movie.genres" :key="idx"> #{{ genre[gen] }} </span></p>
              <hr>
              <v-row class="d-flex justify-content-center">
                <v-col cols="12" md="6" style="border-right: 1px solid gray;">
                  <MovieLike :movie="movie" @refresh_movie="refreshMovie"/>
                </v-col>
                <v-col cols="12" md="6">
                  <MovieSelect :movie="movie" @refresh_movie="refreshMovie"/>
                </v-col>
              </v-row>
              <hr>
              <p>
                {{ movie.overview }}
              </p>
              <hr class="my-4">
              <h3> Comments </h3> 
              <MovieCommentList :movie="movie" :refresh="refresh" />
              <CreateToMovieComment :movie="movie" @refresh="refreshList"/>
            </div>
            <div class="col-sm">
              <img :src="movie.poster_path" alt="" style="max-width: 100%;">
            </div>
          </div>
        </div>
        <MovieReview v-if="tap===false" :movie="movie"/>
        <hr class="my-1">

      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import CreateToMovieComment from '@/views/movies/CreateToMovieComment'
import MovieCommentList from '@/views/movies/MovieCommentList'
import MovieReview from '@/views/movieList/MovieReview'
import MovieLike from '@/views/movies/MovieLike'
import MovieSelect from '@/views/movies/MovieSelect'

export default {
  name: "MovieDetail",
  components: {
    CreateToMovieComment,
    MovieCommentList,
    MovieReview,
    MovieLike,
    MovieSelect,
  },
  data () {
    return {
      genre: [],
      yourLocalVariable: 0,
      comment: '',
      rating: 5,
      refresh: 0,
      tap: true,
      like_movie: [],
      isLike: false,
    }
  },
  props: {
    movie: {},
    dialog: Boolean,
  },
  methods: {
    refreshList: function () {
      this.refresh += 1
    },
    refreshMovie: function () {
      this.$emit('refresh')
    },
    closeDetail: function () {
      this.$emit('close_detail')
    }
  },
  created: function () {
      this.genre = this.$store.state.genre
  },
  mutated: function () {
    this.like_movie = this.movie.like_users
  }
}
</script>

<style>

</style>