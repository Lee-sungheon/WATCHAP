<template>
  <v-app>
    <router-link :to="searchString"></router-link>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark" style="background: black;">
      <a class="navbar-brand" href="#"><img src="./assets/logo2.png" style="height: 45px;" alt=""></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0 pl-0" style="font-size: 1.1rem">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Home' }">Home<span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'MovieList' }">Movie List<span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'PlayListHome' }">Play List<span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="login">
          <b-avatar v-b-toggle.sidebar-footer :src="profile.profileurl" class="mr-3"></b-avatar>
          <li class="nav-item mr-2" style="line-height: 0; margin-top: 8%;">
            <span class="text-white mb-0">{{user}} 님 환영합니다.</span>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" @click.native="logout" to="#">Logout</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-else>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Login' }">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Signup' }">SignUp</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <b-sidebar id="sidebar-footer" title="My Profile" aria-label="Sidebar with custom footer" right shadow>
      <template #footer="{ hide }">
        <div class="d-flex bg-dark text-light align-items-center px-3 py-2">
          <strong class="mr-auto">My Profile</strong>
          <b-button size="sm" @click="hide">Close</b-button>
        </div>
      </template>
      <Profile :user="user"/>
    </b-sidebar>

    <router-view @login="logIn"/>
  </v-app>
</template>

<script>
import axios from 'axios'
import Profile from '@/views/accounts/Profile'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'App',
  components: {
    Profile,
  },
  data: function () {
    return {
      login: false,
      user: '',
      profile: this.$store.state.profile,
      searchString: "",
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.login = false
      this.$router.push({ name : 'Login' })
    },
    logIn: function () {
      this.login = true
    },
    getUser: function () {
      axios.get(`${SERVER_URL}/accounts/get_user/`)
        .then((res) => {
          this.$store.dispatch('getuser', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getProfile: function () {
      if (this.user) {
        axios.get(`${SERVER_URL}/accounts/${this.user}/`)
          .then((res) => {
            this.$store.dispatch('getprofile', res.data)
            this.profile = this.$store.state.profile
          })
          .catch((err) => {
            console.log(err)
          })
      }
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
          this.$store.dispatch('getmovies', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
    this.getUser()
    this.getProfile()
    this.getMovies()
  },
  watch: {
    login: function() {
      this.user = this.$store.state.username
      this.getProfile()
      this.getMovies()
    }
  }
}
</script>
<style>
@font-face {
  font-family: 'LotteMartHappy';
  font-style: normal;
  font-weight: 700;
  src: url('//cdn.jsdelivr.net/korean-webfonts/1/corps/lottemart/LotteMartHappy/LotteMartHappyBold.woff2') format('woff2'), url('//cdn.jsdelivr.net/korean-webfonts/1/corps/lottemart/LotteMartHappy/LotteMartHappyBold.woff') format('woff');
}
#app {
  font-family: 'LotteMartHappy', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
