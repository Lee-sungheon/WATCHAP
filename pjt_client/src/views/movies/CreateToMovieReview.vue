<template>
  <div>
    <div class="d-flex justify-content-end" style="margin-right: 20%;">
      <i class="fas fa-edit fa-2x d-flex felx" style="color: white;" v-b-modal.modal-lg variant="primary"></i><span>Create Review</span>
    </div>
    <b-modal id="modal-lg" size="lg" title="Create Reivew" 
      body-bg-variant="dark" header-bg-variant="dark"
      body-text-variant="light" header-text-variant="light"
      hide-footer
    >
      <v-row>
        <v-col cols="12" md="1">
          <img :src="movie.poster_path" alt="" style="max-width: 100%; width: 50px;">
        </v-col>
        <v-col cols="12" md="11" class="mt-2">
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
    </b-modal>
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