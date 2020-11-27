import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    username: '',
    genre: {
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
    users: [],
    profile: [],
    refresh: false,
    movies: [],
  },
  mutations: {
    LOGIN_INF: function (state, username) {
      state.username = username
    },
    GET_USER: function (state, users) {
      state.users = users
    },
    GET_PROFILE: function (state, profile) {
      state.profile = profile
    },
    REFRESH_PROFILE: function (state) {
      state.refresh = !state.refresh
    },
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
  },
  actions: {
    login: function ({ commit }, username) {
      commit('LOGIN_INF', username)
    },
    getuser: function ({ commit }, users) {
      commit('GET_USER', users)
    },
    getprofile: function ({ commit }, profile) {
      commit('GET_PROFILE', profile)
    },
    refreshProfile: function ({ commit }) {
      commit('REFRESH_PROFILE')
    },
    getmovies: function ({ commit }, movies) {
      commit('GET_MOVIES', movies)
    },
  },
  plugins: [
    createPersistedState(),
  ],
});


export default store;