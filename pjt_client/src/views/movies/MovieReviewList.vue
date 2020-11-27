<template>
  <b-card bg-variant="secondary" text-variant="white">
    <div style="margin: 0; padding: 0;">
      <div class="d-flex justify-content-between">
        <h5><a v-b-toggle :href="toggle_href" @click.prevent>
          <b-avatar :src="profile.profileurl" class="mr-3"></b-avatar>
           </a>
        {{ review.user }}</h5>
        <b-sidebar :id="toggle_id" title="Your Profile" aria-label="Sidebar with custom footer" shadow>
          <template #footer="{ hide }">
          <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
            <strong class="mr-auto">Your Profile</strong>
            <b-button size="sm" @click="hide">Close</b-button>
          </div>
          </template>
          <YourProfile :user="review.user" @getprofile="getProfile" />
        </b-sidebar>
        <v-menu v-if="review.user === user" bottom left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              dark
              icon
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item-group color="indigo"> 
              <v-list-item style="cursor:pointer">
                <v-list-item-title @click="$bvModal.show(modalUpdate)">Update</v-list-item-title>
              </v-list-item>
              <v-list-item style="cursor:pointer">
                <v-list-item-title @click="deleteReview">Delete</v-list-item-title>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-menu>
      </div>

      <b-modal :id="modalUpdate" size="lg" title="Update Reivew" 
      body-bg-variant="dark" header-bg-variant="dark"
      body-text-variant="light" header-text-variant="light"
      hide-footer>
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
      <button class="btn btn-light btn-block" @click="updateReview">Update</button>
    </b-modal>
      <small class="d-flex justify-content-start">글 작성 : {{ created_at }} | 글 수정 : {{ updated_at }}</small>
      <v-row>
        <v-col
          v-for="value in ['-lg']"
          :key="value"
          cols="12"
          md="2"
        >
          <div
            :class="`rounded${value}`"
            class="pa-4 text-center blue-grey lighten-1 text-no-wrap outlined" style="padding:5px !important;"
          ><i class="fas fa-star mr-3" style="color: yellow"></i> {{ review.rank }}</div>
        </v-col>
      </v-row>
      <h4 class="d-flex justify-content-start">{{ review.title }}</h4>
      <p class="d-flex justify-content-start">{{ review.content }}</p>
    </div>
    <hr>
    <div class="d-flex justify-content-start">
      <i class="fas fa-heart mx-3"><span class="ml-3">{{ like_review_len }} 개</span></i>
      <i class="fas fa-comment-alt ml-3"><span class="ml-3">{{ comment_review_len }} 개</span></i>
    </div>
    <hr>
    <ReviewCommentList :review="review" :refresh="refresh" @refresh_review_comment="refreshComment"/>
    <hr>
    <b-container style="margin: 0; padding: 0;">
      <b-row>
        <ReviewLike :review="review" @refresh_review="refreshReview"/>
        <b-col @click="isComment" style="cursor:pointer"><i class="fas fa-comment-alt fa-lg mr-3"></i>
        <span style="font-size: 1rem">Comment</span></b-col>
      </b-row>
    </b-container>
    <hr v-show="isco">
    <CreateToReviewComment :review="review" @refresh="refreshList" v-show="isco"/>
  </b-card>
</template>

<script>
import axios from'axios'
import ReviewLike from '@/views/movies/ReviewLike'
import CreateToReviewComment from '@/views/movies/CreateToReviewComment'
import ReviewCommentList from '@/views/movies/ReviewCommentList'
import YourProfile from '@/views/accounts/YourProfile'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieReivewList",
  components: {
    ReviewLike,
    CreateToReviewComment,
    ReviewCommentList,
    YourProfile,
  },
  data: function () {
    return {
      user: this.$store.state.username,
      rating: this.review.rank/2,
      title: this.review.title,
      content: this.review.content,
      modalUpdate: 'modal-update' + this.review.id,
      like_review_len: this.review.like_users.length,
      comment_review_len: 0,
      isco: false,
      refresh: true,
      toggle_id: 'sidebar-footer-you' + this.review.id,
      toggle_href: '#sidebar-footer-you' + this.review.id,
      profile: [],
      created_at: this.review.created_at.substring(0, 10) + ' ' + this.review.created_at.substring(11, 19),
      updated_at: this.review.updated_at.substring(0, 10) + ' ' + this.review.updated_at.substring(11, 19),
    }
  },
  props: {
    review: Object,
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
    updateReview: function() {
      const config = this.setToken()
      const reviewItem = {
        movie: this.movie.id,
        like_users: this.movie.like_users,
        title: this.title,
        content: this.content,
        rank: this.rating * 2,
      }
      axios.put(`${SERVER_URL}/movies/update_delete_movie_review/${this.review.id}/`, reviewItem, config)
        .then(() => {
          this.$emit('refresh_delete')
          window.alert('글수정이 완료되었습니다.')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview: function () {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/movies/update_delete_movie_review/${this.review.id}/`, config)
        .then(() => {
          this.$emit('refresh_delete')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    refreshReview: function (like_review_len) {
      this.like_review_len = like_review_len
      this.created_at = this.review.created_at.substring(0, 10) + ' ' + this.review.created_at.substring(11, 19),
      this.updated_at = this.review.updated_at.substring(0, 10) + ' ' + this.review.updated_at.substring(11, 19)
    },
    isComment: function () {
      this.isco = !this.isco
    },
    refreshList: function () {
      this.refresh = !this.refresh
    },
    refreshComment: function (review_comment_length) {
      this.comment_review_len = review_comment_length
    },
    getProfile: function (profile) {
      this.profile = profile
    }
  },
  watch: {
    review: function () {
      this.review.rank = this.review.rank / 2
      this.like_review_len = this.review.like_users.length,
      this.created_at = this.review.created_at.substring(0, 10) + ' ' + this.review.created_at.substring(11, 19),
      this.updated_at = this.review.updated_at.substring(0, 10) + ' ' + this.review.updated_at.substring(11, 19)
    },
  },
  created: function() {
    this.review.rank = this.review.rank / 2
    this.like_review_len = this.review.like_users.length,
    this.created_at = this.review.created_at.substring(0, 10) + ' ' + this.review.created_at.substring(11, 19),
    this.updated_at = this.review.updated_at.substring(0, 10) + ' ' + this.review.updated_at.substring(11, 19)
  },
}
</script>

<style scoped>
  hr {
    background-color: white;
    height: 0.01em;
  }
</style>