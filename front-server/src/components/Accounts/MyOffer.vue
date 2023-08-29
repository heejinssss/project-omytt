<template>
  <div class="bottom-space">

    <div class="text">👇 이런 영화를 좋아하시는군요 👇</div>

    <span v-for="(offer, idx) in movieOffer" :key="idx">
      <MyOfferItem :offer="offer"/>
    </span>

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

<style scoped>
.text {
  font-family: NanumSquareNeo-Variable;
  color: white;
  font-size: 20px;
  margin: 20px;
  margin-bottom: 30px;
}
.bottom-space {
  margin-bottom: 100px;
}
</style>