import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
// import { compileToFunctions } from 'vue-template-compiler'

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    username: null,
    articles: [],
    otts: null, // db의 ott리스트
    selects: [], // 내가 선택한 영화
    token: null,
    selectedId: [], // 선택된 movie.id
    finalRecommend: null,
    myOtts: [],
    myFirstOtts: [],
    // likes: false, // 좋아요
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = []
      state.movies = movies
      console.log(this.movies)
      console.log("요청 받음")
    },
    GET_OTTS(state, otts) {
      state.otts = otts
      console.log(this.otts)
    },
    // recommend 관련
    GET_SELECT(state, selects) {
      state.selects = []  // 초기화 후 다시 저장
      state.selects = selects
      console.log(this.selects)
    },
    SAVE_SELECTED(state, selectId) {
      const index = state.selectedId.indexOf(selectId)
      console.log(index)
      if (index !== -1) {  // 이미 선택된 이미지
        state.selectedId.splice(index, 1)  
      } else {
        state.selectedId.push(selectId)
        console.log(this.selectedId)
      }

      console.log(this.selectedId)
    },
    FINAL_RECOMMEND(state, finalRecommend) {
      state.finalRecommend = finalRecommend
      state.selectedId = [] // 원래 선택된 배열 초기화
    },
    // myPage
    // 내가 가지고 있는 ott 선택 후 저장
    SAVE_MYOTT(state, myOtt) {
      console.log("mutation")
      const index = state.myOtts.indexOf(myOtt)
      console.log(index)
      if (index !== -1) {  // 이미 선택된 ott
        // console.log("이미 선택")
        state.myOtts.splice(index, 1)  
      } else {
        // console.log("선택안됨")
        state.myOtts.push(myOtt)
        // console.log(state.myOtts)
      }
      console.log(state.myOtts)

    },
    GET_MY_OTTS(state, myFirstOtts) {
      state.myFirstOtts = myFirstOtts
      console.log(this.myFirstOtts)
    },
    // login 관련
    SIGN_UP_TOKEN(state, token) {
      state.token = token
      console.log("회원가입")
      router.push({name : 'MyFirstOttView'}) // signup -> 초기설정
    },
    SAVE_USERNAME(state, username) {
      state.username = username
      console.log(this.username)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log("로그인 함!!!!!")
      router.push({name : 'MovieView'}) // login -> movielist 페이지
    },
    CLEAR_USERNAME(state) {
      state.username = null
    },
    CLEAR_TOKEN(state) {
      console.log(state.token)
      state.token = null
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/tmdb/initial/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // 2) 검색
    performSearch1(context, searchQuery) {
      console.log("검색 버튼")
      const query = encodeURIComponent(searchQuery)
      axios.get(`${API_URL}/movies/search/${query}/`)
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getOtts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/ott/`,
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_OTTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 3) ott 버튼 누르기
    buttonClick(context, ott_initial) {
      const name = ott_initial
      axios({
        method: 'get',
        url: `${API_URL}/movies/tmdb/${name}`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
          // this.totalPages = Math.ceil(this.movies.length / 10)
          // this.currentPage = 1
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // recommend
    // 1) random 영화 가져오기
    getSelect(context) {
      axios({
        method: 'get',
        url: `${API_URL}/recommend/random/`,
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_SELECT', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 2) 선택한 영화 저장
    saveSelect(context, selectId) {
      // console.log('함수 들어옴')
      // console.log(selectId)
      context.commit('SAVE_SELECTED', selectId)
    },
    performSearch(context, searchQuery) {
      const query = encodeURIComponent(searchQuery)
      axios.get(`${API_URL}/movies/search/${query}/`)
        .then((res) => {
          context.commit('GET_SELECT', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 3) 선택한 영화 django로 보내기
    sendIds(context, selectedId) {
      const username = this.state.username
      const payload = selectedId
      axios({
        method: 'post',
        url: `${API_URL}/recommend/optimize_ott/${username}/`,
        data: {
          payload
        }
      })
      .then((res) => {
        console.log('response!!')
        console.log(res)
        context.commit('FINAL_RECOMMEND', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // signup
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      // const ott_user = payload.ott_user

      // console.log(ott_user)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          this.state.myFirstOtts = [] // 사용자가 가진 ott 초기화
          context.commit('SAVE_USERNAME', username)
          context.commit('SIGN_UP_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // myPage, 내가 가지고 있는 ott 선택
    saveMyOtt(context, myOtt) {
      context.commit('SAVE_MYOTT', myOtt)
      console.log("이 버튼 저장")
    },
    sendMyOtt(context, payload) {
      // const payload = selectMyOtt
      const username = this.state.username
      const token = this.state.token
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/movies/user_ott/${username}/`,
        headers: {
          Authorization: `Token ${token}`
        },
        data: {
          payload
        }
      })
      .then((res) => {
        console.log('db에 저장')
        console.log(res)
        context.dispatch('getMyOtt')
        // context.commit('GET_MY_OTTS', res.data.id)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMyOtt(context) {
      console.log("getmyott 함수 실행")
      const username = this.state.username
      const token = this.state.token
      axios({
        method: 'get',
        url: `${API_URL}/movies/user_ott/${username}/`,
        headers: {
          Authorization: `Token ${token}`
        },
      })
      .then((res) => {
        console.log('get axios 요청 받음')
        console.log(res)
        context.commit('GET_MY_OTTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // login
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        console.log(1111)
        context.commit('SAVE_USERNAME', username)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(2222222)
        console.log(err)
      })
    },
    logout(context) {
      context.commit('CLEAR_TOKEN')
      context.commit('CLEAR_USERNAME') 
    },
    checkLogin() {
      if(this.token){
        console.log("입장")
        // this.$store.dispatch('getArticles')
        return true
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')

        router.push({name : 'LogInView'})
      }
      // 로그인 되어있으면 실행
      // 로그인 X : login 페이지로 이동
    }
  },
  modules: {
  }
})
