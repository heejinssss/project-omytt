<template>
  <div>
    <div class="backdropcontainer"
    :style="{ backgroundImage: `linear-gradient( rgba(255, 255, 255, 0.3), rgba(0, 0, 0, 1) ), url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`}">


      <div v-if="movie">
        <p class="title">{{ movie.title }}</p>


        <div class="card" style="width:700px; margin:auto;">
          <div v-if="movie.video_key" class="card-img-top">
            <iframe id="player" width="700px" height="360px"
            :src="`https://www.youtube.com/embed/${movie.video_key}`"
            frameborder="0">
            </iframe>
          </div>

          <div class="card-img-top" v-else>
            <img :src="'https://image.tmdb.org/t/p/original'+ movie.backdrop_path" style="width:640px; height:auto;">
          </div>

          <div class="card-body">
            <div class="card-text">{{ movie.overview }}</div>
          </div>
        </div>

        <div v-if="ott_lst" class="ott" style="margin-bottom: 20px; color: white;">
          <span style="margin:px; font-size: 15px;"><strong>{{ movie.title }}, </strong></span>
          <span v-for="(ott, idx) in ott_lst" :key="idx" style="margin:5px; font-size: 20px;">
            <img :src="require(`@/assets/${ott}_long.png`)" style="height:20px;">
          </span>
          <span style="margin:px; font-size: 15px;">에서 즐기실 수 있습니다</span>
        </div>

        <span>
          <button type="button" class="like btn btnEvent" @click="userLikes(movie.id)">
            <img v-if="likes" :src="require('@/assets/heart_after.png')" style="width: 35px; height: 35px;">
            <img v-else :src="require('@/assets/heart_before.png')" style="width: 35px; height: 35px;">
          </button>
          <span style="color: white;">{{ movie.likes_count }}</span>
        </span>

        <MovieCommentCreate :movie="movie" v-if="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCommentCreate from '@/components/MovieList/MovieCommentCreate'

const API_URL = 'http://127.0.0.1:8000'

import axios from 'axios'

export default {
  name: 'MovieDetail',
  components: {
    MovieCommentCreate
  },
  data() {
    return {
      movie: null,
      ott_lst: [],
      likes: false,
      // is_liked: false
    }
  },
  computed: {
    movieProp() {
      return this.$route.params.movie || this.movie
    },
    // likes() {
    //   return this.$store.state.likes
    // }
  },
  mounted() {
    this.getDetails()
    this.getOfferOtt()
    this.getLikes()
  },
  methods: {
    getOfferOtt() {
      const movieId = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/detail/${movieId}/ott/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.otts = res.data
        this.ott_lst = this.otts.ott_lst
        console.log(this.ott_lst)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getDetails() {
      const movieId = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/detail/${movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
        this.movie.video_key = res.data.video_key
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikes() {
      console.log("좋아요 정보 가져오기")
      const movieId = this.$route.params.id
      console.log(movieId)
      axios({
        method: 'get',
        url: `${API_URL}/movies/likes/${movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.likes = res.data.likes
          this.movie.likes_count = res.data.likes_count
          console.log("좋아요 요청 들어옴")
          console.log(this.movie.likes)
          console.log(this.movie.likes_count)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 좋아요 버튼 누르기
    userLikes(movieId) {
      this.likes = !this.likes
      // localStorage.setItem('likes', JSON.stringify(this.likes))

      axios({
        method: 'post',
        url: `${API_URL}/movies/likes/${movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.movie.likes_count = res.data.likes_count // 좋아요 누른 후 count 바로 변경
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.backdropcontainer {
  background-repeat: no-repeat;
  background-position: center top;
}
p.title {
  padding-top: 40px;
  padding-bottom: 20px;
  font-family: MBC1961M;
  font-size: 50px;
  text-shadow: 10px;
  color: rgb(36, 36, 36);
}
.card {
  background: transparent;
}
.card {
  border: transparent;
}
.card-text {
  color: white;
  font-size: 20px;
  font-family: Arita-buri-SemiBold;
}
.like {
  border: none;
  outline: none;
}
</style>
