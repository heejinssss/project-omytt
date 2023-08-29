<template>
  <div>
    <span class="commentTag"></span>
    <div class="comments">
      <MovieCommentItem
      v-for="comment in comments" 
      :key="comment.id"
      :comment="comment"/>
    </div>
    
    <form class="m-3" @submit.prevent="createComment">
      <input class="text-input" type="text" id="content" cols="50" rows="1.5"
      v-model="content" placeholder="댓글을 작성해주세요">
      <input type="submit" id="submit" value="확인" class="btn-3d red mx-3">
    </form>

  </div>
</template>

<script>
import MovieCommentItem from '@/components/MovieList/MovieCommentItem'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCommentCreate',
  components: {
    MovieCommentItem
  },
  data() {
    return {
      content: null, 
      user: null,
      comments: [],
    }
  },
  props:{
    movie: Object
  },
  created() {
    // 사용자 정보 가져오기
    this.user = this.$store.state.username
    this.getComments()
  },
  methods: {
    createComment() {
      const content = this.content
      const movieId = this.movie.id
      const userName = this.user

      console.log(userName)

      if (!content) {
        alert('댓글을 입력해주세요')
        return
      } 
      axios({
        method: 'post',
        url: `${API_URL}/movies/comment/${movieId}/`,
        data: {
          content: content,
          movie: movieId,
          username: userName
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
        console.log(res)
        this.content = null
        this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments() {
      // console.log(this.movie.id)
      const movieId = this.movie.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/comment/${movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.comments = res.data // 댓글 목록 업데이트
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
input {
  font-family: 'NanumSquareNeo-Variable';
}
.main {
  background: rgba(255, 255, 255, 0.4);
  position: absolute;
  top: 20%;
  left: 30%;
  width: 40%;
  text-align: center;
  padding: 5px;
  border-radius: 3rem;
  box-shadow: 0px 0px 8px -5px #000000;
  padding-top: 3%;
  padding-bottom: 5%;
  font-family: "Poppins", sans-serif;
}
h1 {
  cursor: default;
  user-select: none;
}
input {
  font-family: 'NanumSquareNeo-Variable';
  border-radius: 3rem;
  border: none;
  padding: 10px;
  text-align: center;
  outline: none;
  margin: 10px;
  width: 400px;
  box-sizing: border-box;
  font-weight: 400;
}
input:hover {
  box-shadow: 0px 0px 8px -5px #000000;
}
input:active {
  box-shadow: 0px 0px 8px -5px #000000;
}
.commentTag {
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
  text-align: left;
}
.commentInput {
  font-family: 'SUITE-Regular';
}
.comments {
  padding: 5px 5px 0px 5px;
  width: 700px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 6px;
}
.btn-3d {
  width: 80px;
  height: 40px;
  margin-bottom: 100px;
  position: relative;
  display: inline-block;
  color: white;
  border-radius: 6px;
  text-align: center;
  transition: top .01s linear;
  text-shadow: 0 1px 0 rgba(0,0,0,0.15);
  border: none;
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
        0 4px 0 0 #C24032,
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
