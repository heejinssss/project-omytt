<template>
  <div id="app" class="spectrum-background">
    <router-link v-if="isLogin" :to="{ name: 'MovieView', params: { id: $store.state.user } }" class="login-button"></router-link> 
    <!-- <router-link v-else to="/signup" class="login-button">Sign Up</router-link>
    <router-link v-if="!isLogin" to="/login" class="login-button" style="margin-right: 30px;">Login</router-link> -->
    <button v-if="isLogin" class="login-button" style="margin: 0 auto;" @click="logout">Logout</button>
    <!--

    -->
    <nav class="navbar navbar-expand bg-dark p-0" data-bs-theme="dark">
      <div class="m-auto">
        <div class="navbar-nav">
          <router-link v-if="isLogin" :to="{ name: 'RecommendView'}" class="nav-link px-5">Recommend</router-link>
          <router-link v-if="isLogin" :to="{ name: 'MovieView' }" class="nav-link px-5">Movie List</router-link>
          <router-link v-if="isLogin" :to="{ name: 'AccountsView' }" class="nav-link px-5">My Page</router-link>
        </div>
      </div>
    </nav>

    <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>


<style>
body {
  height: 100vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  /* position: relative; */
  background: #121212;
  /* width: 100vw; */
  height: 100vh;
}
/* .spectrum-background {
  background:
    linear-gradient(red, transparent),
    linear-gradient(to top left, lime, transparent),
    linear-gradient(to top right, blue, transparent);
  background-blend-mode: screen;
} */

/* button.login {
  position: absolute;
  top: 0;
  right: 0;
  margin-left: 100%;
  margin-inline-end: 0%;
} */
nav .nav-link.router-link-exact-active {
  color: #ffffff;
}
@font-face {
    font-family: 'Tenada';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/Tenada.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'HANAMDAUM';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/HANAMDAUM.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}
@font-face {
    font-family: 'KCCChassam';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCChassam.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'NanumSquareNeo-Variable';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
.brand {
  font-size: 80px;
  /* text-align: center; */
  font-family: 'KCCChassam';
  color: #fff;
  text-shadow: 0 0 50px #ffff00, 0 0 100px #ffff00, 0 0 20px #ffff00, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750;
  /* text-shadow: 0 0 50px #fff, 0 0 10px #fff, 0 0 15px #9CFF2E, 0 0 20px #9CFF2E, 0 0 25px #F0FF42, 0 0 30px #F0FF42, 0 0 35px #F0FF42; */
}
</style>
