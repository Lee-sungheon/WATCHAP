<template>
  <div class="mt-5 ml-5">
    <br><br><br>
    <h2 class="text-left ml-2 text-white">Movie List</h2>
    <hr style="border: solid 1px white;">
    <h5 class="text-left ml-2 text-white">보고 싶은 작품을 찾아보세요!</h5>
  
    <v-container fluid>
      <v-data-iterator
        :items="items"
        :items-per-page.sync="itemsPerPage"
        :page="page"
        :search="search"
        :sort-by="sortBy.toLowerCase()"
        :sort-desc="sortDesc"
        hide-default-footer
      >
        <template v-slot:header>
          <v-toolbar
            dark
            color="black darken-3"
            class="mb-1"
          >
            <v-text-field
              v-model="search"
              clearable
              flat
              solo-inverted
              hide-details
              prepend-inner-icon="mdi-magnify"
              label="Search"
            ></v-text-field>
            <template v-if="$vuetify.breakpoint.mdAndUp">
              <v-spacer></v-spacer>
              <v-select
                v-model="genre"
                flat
                solo-inverted
                hide-details
                :items="keys2"
                prepend-inner-icon="mdi-magnify"
                label="Genre"
                @input="filterMovie"
              ></v-select>
              <v-spacer></v-spacer>
              <v-select
                v-model="sortBy"
                flat
                solo-inverted
                hide-details
                :items="keys"
                prepend-inner-icon="mdi-magnify"
                label="Sort by"
              ></v-select>
              <v-spacer></v-spacer>
              <v-btn-toggle
                v-model="sortDesc"
                mandatory
              >
                <v-btn
                  large
                  depressed
                  color="gray"
                  :value="false"
                >
                  <v-icon>mdi-arrow-up</v-icon>
                </v-btn>
                <v-btn
                  large
                  depressed
                  color="gray"
                  :value="true"
                >
                  <v-icon>mdi-arrow-down</v-icon>
                </v-btn>
              </v-btn-toggle>
            </template>
          </v-toolbar>
        </template>
        <template v-slot:default="props">
          <v-row>
            <v-col
              v-for="item in props.items"
              :key="item.title"
              cols="12"
              sm="4"
              md="3"
              lg="2"
            >
              <MovieItem :item="item" @isdetail="goDetail"/>
            </v-col>
          </v-row>
          <div v-if="movie">
            <hr>
            <MovieDetail :movie="movie" :dialog="dialog" @refresh="refreshMovies" @close_detail="closeDetail"/>
          </div>
        </template>

        <template v-slot:footer>
          <v-row
            class="mt-2"
            align="center"
            justify="center"
          >
            <span class="grey--text">Items per page</span>
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  dark
                  text
                  color="white"
                  class="ml-2"
                  v-bind="attrs"
                  v-on="on"
                >
                  {{ itemsPerPage }}
                  <v-icon>mdi-chevron-down</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(number, index) in itemsPerPageArray"
                  :key="index"
                  @click="updateItemsPerPage(number)"
                >
                  <v-list-item-title>{{ number }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-spacer></v-spacer>

            <span
              class="mr-4
              grey--text"
            >
              Page {{ page }} of {{ numberOfPages }}
            </span>
            <v-btn
              fab
              dark
              color="dark darken-3"
              class="mr-1"
              @click="formerPage"
            >
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
            <v-btn
              fab
              dark
              color="dark darken-3"
              class="ml-1"
              @click="nextPage"
            >
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </v-row>
        </template>
      </v-data-iterator>
    </v-container>
  </div>  
</template>

<script>
import MovieItem from '@/views/movieList/MovieItem'
import MovieDetail from '@/views/movieList/MovieDetail'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieList",
  components: {
    MovieItem,
    MovieDetail,
  },
  data: function() {
      return {
        items: [],
        itemsPerPageArray: [24, 36, 48],
        search: '',
        filter: {},
        sortDesc: false,
        page: 1,
        itemsPerPage:24,
        sortBy: 'title',
        keys: [
          'title',
          'vote_average',
          'release_date',
          'popularity',
        ],
        keys2: [
          '전체',
          "액션",
          "모험",
          "애니메이션",
          "코미디",
          "범죄",
          "다큐멘터리",
          "드라마",
          "가족",
          "판타지",
          "역사",
          "공포",
          "음악",
          "미스터리",
          "로맨스",
          "SF",
          "TV 영화",
          "스릴러",
          "전쟁",
          "서부"
        ],
        genres: {
          28: "액션",
          12: "모험",
          16: "애니메이션",
          35: "코미디",
          80: "범죄",
          99: "다큐멘터리",
          18: "드라마",
          10751: "가족",
          14: "판타지",
          36: "역사",
          27: "공포",
          10402: "음악",
          9648: "미스터리",
          10749: "로맨스",
          878: "SF",
          10770: "TV 영화",
          53: "스릴러",
          10752: "전쟁",
          37: "서부"
        },
        movie: '',
        dialog: false,
        genre: '',
      }
    },
    computed: {
      numberOfPages () {
        return Math.ceil(this.items.length / this.itemsPerPage)
      },
      filteredKeys () {
        return this.keys.filter(key => key !== 'title')
      },
    },
    methods: {
      nextPage () {
        if (this.page + 1 <= this.numberOfPages) this.page += 1
      },
      formerPage () {
        if (this.page - 1 >= 1) this.page -= 1
      },
      updateItemsPerPage (number) {
        this.itemsPerPage = number
      },
      setToken: function() {
        const token = localStorage.getItem('jwt')
        const config = {
          headers: {
            Authorization: `JWT ${token}`
          }
        }
        return config
      },
      getMovies: function () {
        const config = this.setToken()
        axios.get(`${SERVER_URL}/movies/`, config)
          .then((res) => {
            this.items = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      },
      goDetail: function (movie) {
      this.movie = movie
      this.dialog = true
      },
      refreshMovies: function () {
        this.getMovies()
      },
      closeDetail: function () {
        this.dialog = false
      },
      filterMovie: function () {
        if (this.genre==="전체") {
          this.getMovies()
        } else {
          const config = this.setToken()
          axios.get(`${SERVER_URL}/movies/`, config)
            .then((res) => {
              this.items = []
              for (const movie of res.data) {
                for (const gen of movie.genres) {
                  if (this.genres[gen] === this.genre) {
                    this.items.push(movie)
                    break
                  }
                }
              }
            })
            .catch((err) => {
              console.log(err)
            })
        }
      }
    },
    created: function () {
      if (localStorage.getItem('jwt')) {
        this.getMovies()
      } else {
        this.$router.push({ name: 'Login' })
      }
    }
}
</script>

<style>

</style>