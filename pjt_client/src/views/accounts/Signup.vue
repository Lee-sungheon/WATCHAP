<template>
  <div class="main-container">
    <div class="box-container">
        <h2 class="heading">
        Create Your Account
        </h2>
        <div class="form-fields">
        <input id="user_name" name="username" type="text" placeholder="User Name" v-model="credentials.username">
        </div>
        <div class="form-fields">
        <input id="email" name="email" type="text" placeholder="Email Address" v-model="credentials.email">
        </div>
        <div class="form-fields">
        <input id="password" name="password" type="password" placeholder="Password" v-model="credentials.password">
        </div>
        <div class="form-fields">
        <input id="passwordConfirmation" 
          name="passwordConfirmation" type="password" 
          placeholder="Password Confirmation"
          v-model="credentials.passwordConfirmation"
          @keypress.enter="signup"
        >
        </div>
        <div class="form-fields">
        <button class="createaccount" name="commit" type="submit" @click="signup">
            Create your account
        </button>
        </div>
        <div class="login-choice"><span>or sign up with</span></div>
        <SocialSignUp />
        <div>
            <p class="center">
                By signing up you agree to the
                <a href="#">Terms of Service</a>.
            </p>
        </div>
    </div>
    <div class="footer">
        <p>Already have an account? <router-link class="nav-link" :to="{ name: 'Login' }">Sign In</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SocialSignUp from '@/components/SocialLogin'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
  components: {
    SocialSignUp
  },
  data: function () {
    return {
      credentials: {
        username: '',
        email: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then((res) => {
          console.log(res)
          this.$router.push({ name : 'Login' })
        })
        .catch((err) => {
          console.log(err)
          window.alert(err.response.data.error)
        })
    }
  }
}
</script>