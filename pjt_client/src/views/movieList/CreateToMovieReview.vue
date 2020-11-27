<template>
  <div>
    <div class="d-flex justify-content-end" style="margin-right: 20%;">
      <i class="fas fa-edit fa-2x d-flex felx" style="color: white;" @click="dialog=true" variant="primary"></i><span>Create Review</span>
    </div>
    <div class="ml-5">
      <v-dialog
        v-model="dialog"
        hide-overlay
        transition="dialog-top-transition"
        width= "60%"
      >
        <v-card style="margin-top: 5%;" color="gba(255, 255, 255, 0.5)" dark>
          <v-toolbar
            dark
            color="gba(255, 255, 255, 0.5) accent-4"
            class="d-flex justify-content-end"
          >
            <v-toolbar-items class="d-flex justify-content-end">
              <v-btn
              icon
              dark
              @click="dialog=false"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>

          <v-row>
            <v-col cols="12" md="2">
              <img :src="movie.poster_path" class="ml-5" style="max-width: 100%; width: 50px;">
            </v-col>
            <v-col cols="12" md="10" class="mt-2 text-left">
              <h6>{{ movie.title }}</h6>
              {{ movie.release_date }}
            </v-col>
          </v-row>
          <hr>
          <div>
            <h6>별점 평가</h6>
            <v-rating v-model="rating" color="yellow darken-3" background-color="grey darken-1" dense half-increments hover size="30">
            </v-rating>
          </div>
          <hr>
          <div>
            <h6>Review</h6>
            <v-container fluid>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="title"
                    label="Title"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea v-model="content">
                    <template v-slot:label>
                      <div>Content</div>
                    </template>
                  </v-textarea>
                </v-col>
              </v-row>
            </v-container>
          </div>
          <button class="btn btn-light btn-block" @click="createToMovieReview">Write</button>

        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "CreateToMovieReview",
  data: function () {
    return {
      rating: 5,
      title: '',
      content: '',
      dialog: false,
    }
  },
  props: {
    movie: Object,
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
    createToMovieReview: function () {
      const config = this.setToken()
      
      const MovieReview = {
        movie: this.movie.id,
        like_users: this.movie.like_users,
        title: this.title,
        content: this.content,
        rank: this.rating * 2,
      }

      if (MovieReview.title && MovieReview.content) {
        axios.post(`${SERVER_URL}/movies/${this.movie.id}/list_create_movie_review/`, MovieReview, config)
          .then(() => {
            this.$emit('refresh_emit')
            window.alert("글작성이 완료되었습니다.")
            this.title = ''
            this.content = ''
            this.rating = 5
          })
          .catch((err) => { 
            console.log(err)
          })
        }
      else {
        window.alert("내용을 입력해주세요.")
      }
    }
  },
}
</script>

<style>

</style>