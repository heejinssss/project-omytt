<template>
  <div>
    <div class="text">
      내가 <img :src="require(`@/assets/heart_after.png`)" class="pulsate-bck" style="height:50px;"> 하는
    </div>

    <span v-for="(movie, idx) in movieLikes" :key="idx">
      <MyMoviesItem :movie="movie"/>
    </span>

  </div>
</template>

<script>
import MyMoviesItem from '@/components/Accounts/MyMoviesItem'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyMovies',
  components: {
    MyMoviesItem,
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

<style scoped>
.text {
  font-family: NanumSquareNeo-Variable;
  color: white;
  font-size: 20px;
  margin: 20px;
}
.pulsate-bck {
  -webkit-animation: pulsate-bck 0.5s ease-in-out infinite both;
  animation: pulsate-bck 0.5s ease-in-out infinite both;
}
@keyframes pulsate-bck {
  0% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  50% {
    -webkit-transform: scale(0.9);
            transform: scale(0.9);
  }
  100% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
}
</style>
