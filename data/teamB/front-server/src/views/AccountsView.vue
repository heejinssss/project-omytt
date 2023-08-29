<template>
  <div>

    <!-- <div class="p-4">
      <h1 class="brand">o . my . tt</h1>
    </div> -->

    <h3 style="margin-top:50px; color: white; font-family: NanumSquareNeo-Variable;">{{ username }}님의 마이페이지</h3>
    <MyPage />
  </div>
</template>

<script>
import MyPage from '@/components/Accounts/MyPage'

export default {
  name: 'AccountsView',
  components: {
    MyPage
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.checkLogin()
  },
  methods: {
    checkLogin() {
      if(this.isLogin){
        console.log(11333333)
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    },
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>