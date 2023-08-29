<template>
  <div>
    <p>내가 <img :src="require(`@/assets/heart_after.png`)" style="height:20px;"> 한 작품들</p>

    <div v-for="(movie, idx) in movieLikes" :key="idx">
      <MyMoviesItem :movie="movie"/>
    </div>


  </div>
</template>

<script>
import MyMoviesItem from '@/components/Accounts/MyMoviesItem'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyMovies',
  components: {
    MyMoviesItem
  },
  data() {
    return {
      movieLikes: [],
      user: null,
    }
  },
  created() {
    this.myMovies()
  },
  methods: {
    myMovies() {
      this.user = this.$store.state.username  // 사용자 username

      axios({
        method: 'get',
        url: `${API_URL}/movies/user_likes/${this.user}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
          console.log(res)
          this.movieLikes = res.data
        })
        .catch((err) => {
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>