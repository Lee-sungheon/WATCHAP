import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Home from '@/views/movies/Home'
import MovieList from '@/views/movieList/MovieList'
import PlayListHome from '@/views/accounts/PlayListHome'

Vue.use(VueRouter)

const routes = [
  {
    path: "/:searchString",
    props: true
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/playlisthome',
    name: 'PlayListHome',
    component: PlayListHome,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList,
  },
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
