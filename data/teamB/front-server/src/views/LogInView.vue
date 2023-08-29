<template>
  <div class="spectrum-background">

    <form @submit.prevent="login">
      <h3>Login Here</h3>

      <label for="username">Username</label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password">Password</label>
      <input type="password" id="password" v-model="password">

      <input class="check btn-3d red" type="submit" value="submit">
    </form>
    
    <router-link to="/signup" class="login-button">아직 회원이 아니신가요?</router-link>

  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
  }
}
</script>

<style scoped>
/* 배경 색 시도 */
.spectrum-background {
  background:
    linear-gradient(red, transparent),
    linear-gradient(to top left, lime, transparent),
    linear-gradient(to top right, blue, transparent);
  background-blend-mode: screen;
}

@font-face {
  font-family: 'omyu_pretty';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/omyu_pretty.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
*,
*:before,
*:after{
  box-sizing: border-box;
}
body {
  background-color: #080710;
}
.login-button {
  position: absolute;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-decoration: none; /* 밑줄 제거 */
  color: white;
}
form {
  height: 500px;
  width: 400px;
  background-color: rgba(255,255,255,0.13);
  position: absolute;
  transform: translate(-50%,-50%);
  top: 40%;
  left: 50%;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255,255,255,0.1);
  box-shadow: 0 0 40px rgba(8,7,16,0.6);
  padding: 50px 35px;
}
form * {
  font-family: 'NanumSquareNeo-Variable';
  color: #ffffff;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}
form h3 {
  font-size: 33px;
  font-weight: 500;
  line-height: 42px;
  text-align: center;
  color: white;
}
label {
  display: block;
  margin-top: 30px;
  margin-bottom: 10px;
  font-size: 15px;
  font-weight: 500;
}
input {
  display: inline-block;
  height: 40px;
  width: 80%;
  background-color: rgba(254, 253, 253, 0.92);
  color: black;
  border-radius: 3px;
  padding: 0 10px;
  margin-top: 8px;
  font-weight: 300;
}
/* 3D Button */
.btn-3d {
  width: 150px;
  margin-top: 90px;
  position: relative;
  display: inline-block;
  font-size: 18px;
  color: white;
  border-radius: 6px;
  text-align: center;
  transition: top .01s linear;
  text-shadow: 0 1px 0 rgba(0,0,0,0.15);
}
.btn-3d.red:hover    {background-color: #e74c3c;}
.btn-3d.blue:hover   {background-color: #699DD1;}
.btn-3d.green:hover  {background-color: #80C49D;}
.btn-3d.purple:hover {background-color: #D19ECB;}
.btn-3d.yellow:hover {background-color: #F0D264;}
.btn-3d.cyan:hover   {background-color: #82D1E3;}

.btn-3d:active {
  top: 9px;
}
/* 3D button colors */
.btn-3d.red {
  background-color: #e74c3c;
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 #C24032,
        0 8px 0 1px rgba(0,0,0,0.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.red:active {
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.blue {
  background-color: #6DA2D9;
  box-shadow: 0 0 0 1px #6698cb inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(110, 164, 219, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.blue:active {
  box-shadow: 0 0 0 1px #6191C2 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.green {
  background-color: #82c8a0;
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(126, 194, 155, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.green:active {
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.purple {
  background-color: #cb99c5;
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(189, 142, 183, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.purple:active {
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.cyan {
  background-color: #7fccde;
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(102, 164, 178, .6),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.cyan:active {
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.yellow {
  background-color: #F0D264;
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(196, 172, 83, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.yellow:active {
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
</style>