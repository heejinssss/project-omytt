<template>
  <div>

    <div>
      <h1 class="brand">o . my . tt</h1>
    </div>

    <h2>{{ username }}님 안녕하세요.</h2>
    <h3>회원가입이 완료되었습니다.</h3>
    <p>당신이 이미 가입한 ott를 선택해주세요.</p>
    <!-- <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="saveMyOtt(ott.id)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
    </button> -->
    <div>
      <MyOttItem v-for="(ott, idx) in otts" :key="idx" :ott="ott"/>
    </div>
    <button @click="sendMyOtt">완료</button>
    


  </div>
</template>

<script>
import MyOttItem from '@/components/Accounts/MyOttItem'


export default {
  name: 'MyFirstOttView',
  components: {
    MyOttItem
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    otts() {
      return this.$store.state.otts
    },
    myOtts() {
      return this.$store.state.myOtts
    }
  },
  created() {
    this.getMyOtt()
  },
  methods: {
    getMyOtt() {
      this.$store.dispatch('getMyOtt')
      console.log("get 함수")
    },
    sendMyOtt() {
      this.$store.dispatch('sendMyOtt', this.myOtts)
      this.$router.push({name : 'MovieView'})
    }
    
  }
}
</script>

<style>

</style>