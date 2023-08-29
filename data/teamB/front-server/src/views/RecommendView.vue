<template>
  <div>

    <p class="select m-4">당신을 위한 OTT를 찾아보세요</p> 
    <SelectMovie />
    
  </div>
</template>

<script>
import SelectMovie from '@/components/Recommend/SelectMovie'

export default {
  name: 'RecommendView',
  components: {
    SelectMovie,
  },
  computed: {
    isLogin(){
      return this.$store.getters.isLogin // 로그인 여부 -> true 또는 false
    }
  },
  created() {
    this.checkLogin()
    this.getSelect()
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
    getSelect() {
      this.$store.dispatch('getSelect')
    }
  }
}
</script>

<style>
@font-face {
  font-family: 'MBC1961M';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/MBC1961M.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'LINESeedKR-Bd';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'Arita-buri-SemiBold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Arita-buri-SemiBold.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
/* 천천히 나타나는 글자 효과 */
@keyframes text-focus-in {
  0% {
    -webkit-filter: blur(12px);
            filter: blur(12px);
    opacity: 0;
  }
  100% {
    -webkit-filter: blur(0px);
            filter: blur(0px);
    opacity: 1;
  }
}
.select {
  font-family: 'NanumSquareNeo-Variable';
  font-size: 30px;
  animation: text-focus-in 1.5s;
  color: #fdd750;
}
</style>
