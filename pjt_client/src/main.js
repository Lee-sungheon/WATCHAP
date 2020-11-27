import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/css/style.css'
import PortalVue from 'portal-vue'
import vuetify from './plugins/vuetify'
import firebase from 'firebase'
import "firebase/auth"

require('firebase/auth')

Vue.config.productionTip = false

var firebaseConfig = {
  apiKey: "AIzaSyDgXtxqEoyXBV8Opmn59OJQ8SETlEiWQtw",
  authDomain: "ringed-inn-296013.firebaseapp.com",
  databaseURL: "https://ringed-inn-296013.firebaseio.com",
  projectId: "ringed-inn-296013",
  storageBucket: "ringed-inn-296013.appspot.com",
  messagingSenderId: "274960293407",
  appId: "1:274960293407:web:b65eef24d853316283bf2a",
  measurementId: "G-TFNWVH0DC6"
};

Vue.use(PortalVue)
Vue.use(BootstrapVue)

firebase.initializeApp(firebaseConfig)
firebase.analytics()

new Vue({
  router,
  store,
  el: '#app',
  vuetify,
  render: h => h(App)
})
