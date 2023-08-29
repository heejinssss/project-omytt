<template>
  <div>
    <p>이미 구독 중인 OTT</p>

    <span v-for="(ott, idx) in otts" :key="idx">
      <MyOttItem :ott="ott" />
    </span>
    <button @click="sendMyOtt">저장</button>
    <!-- <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="saveMyOtt(ott.id)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
    </button>
    <button @click="sendMyOtt">저장</button> -->

  </div>
</template>

<script>
import MyOttItem from '@/components/Accounts/MyOttItem'

export default {
  name: 'MyOtt',
  components: {
    MyOttItem
  },
  computed: {
    otts() {
      return this.$store.state.otts
    },
    myOtts() {
      return this.$store.state.myOtts
    },
    // myFirstOtts() {
    //   return this.$store.state.myFirstOtts
    // }
  },
  created() {
    this.getMyOtt()
  },
  methods: {
    // saveMyOtt(input) {
    //   const myOtt = input
    //   this.$store.dispatch('saveMyOtt', myOtt)
    // },
    sendMyOtt() {
      this.$store.dispatch('sendMyOtt', this.myOtts)
    },
    // user가 가지고 있는 ott 가져오기
    getMyOtt() {
      this.$store.dispatch('getMyOtt')
      console.log("get 함수")
    }
  } 
}
</script>

<style>

</style>