<template>
  <div>
    <p>내가 좋아요 표시한 장르를 기반으로 추천하는 영화입니다</p>

    <div v-for="(offer, idx) in movieOffer" :key="idx">
      <MyOfferItem :offer="offer"/>
    </div>

  </div>
</template>

<script>
import MyOfferItem from '@/components/Accounts/MyOfferItem'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyOffer',
  components: {
    MyOfferItem
  },
  data() {
    return {
      movieOffer: [],
      user: null,
    }
  },
  created() {
    this.myOffer()
  },
  methods: {
    myOffer() {
      this.user = this.$store.state.username  // 사용자 username

      axios({
        method: 'get',
        url: `${API_URL}/movies/user_offer/${this.user}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
          console.log(res)
          this.movieOffer = res.data
        })
        .catch((err) => {
          alert("좋아하는 영화를 선택해주세요")
          this.$router.push('movie')  // 좋아요를 누른 영화가 없다면, 좋아하는 영화 표시하기
          console.log(err)
      })
    }
  }

}
</script>

<style>

</style>