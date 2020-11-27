<template>
  <div>
    <div class="main-container">
      <div class="box-container">
        <h2 class="heading">Sign In</h2>
        <div class="form-fields">
          <input id="username" name="username" type="text" placeholder="username" v-model="credentials.username">
        </div>
        <div class="form-fields">
          <input id="password" name="password" type="password" placeholder="Password" v-model="credentials.password" @keypress.enter="login">
        </div>
        <div class="form-fields">
          <button class="signIn" name="commit" @click="login">
            Sign In
          </button>
        </div>
        <div class="login-choice"><span>or Sign In with</span></div>
        <SocialLogin />
      </div>
      <div class="footer">
        <p>Don't have an account? <router-link class="nav-link" :to="{ name: 'Signup' }">Create one now</router-link></p>
      </div>
    </div>
  </div>

  
  
</template>

<script>

import axios from 'axios'
import SocialLogin from '@/components/SocialLogin'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  components: {
    SocialLogin,
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login', this.credentials.username)
          this.$router.push( { name : 'Home' })
          this.$store.dispatch('login', this.credentials.username)
        })
        .catch((err) => {
          this.credentials.username = ''
          this.credentials.password = ''
          window.alert("로그인 정보가 일치하지 않습니다.")
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  /* Made with love by Mutiullah Samim*/

  html,body{
  background-image: url('http://getwallpapers.com/wallpaper/full/a/5/d/544750.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  height: 100%;
  font-family: 'Numans', sans-serif;
  }

  .container{
  height: 100%;
  align-content: center;
  }

  .card{
  height: 320px;
  margin-top: auto;
  margin-bottom: auto;
  width: 400px;
  background-color: rgba(0,0,0,0.5) !important;
  }

  .social_icon span{
  font-size: 60px;
  margin-left: 10px;
  color: #FFC312;
  }

  .social_icon span:hover{
  color: white;
  cursor: pointer;
  }

  .card-header h3{
  color: white;
  }

  .social_icon{
  position: absolute;
  right: 20px;
  top: -45px;
  }

  .input-group-prepend span{
  width: 50px;
  background-color: #FFC312;
  color: black;
  border:0 !important;
  }

  input:focus{
  outline: 0 0 0 0  !important;
  box-shadow: 0 0 0 0 !important;

  }

  .remember{
  color: white;
  }

  .remember input
  {
  width: 20px;
  height: 20px;
  margin-left: 15px;
  margin-right: 5px;
  }

  .login_btn{
  color: black;
  background-color: #FFC312;
  width: 100px;
  }

  .login_btn:hover{
  color: black;
  background-color: white;
  }

  .links{
  color: white;
  }

  .links a{
  margin-left: 4px;
  }
</style>