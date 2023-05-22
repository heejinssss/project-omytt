import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    username: null,
    articles: [],
    movies: [],
    otts: null,
    selects: null,
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // GET_ARTICLES(state, articles) {
    //   state.articles = articles
    // },
    // signup & login -> 완료하면 토큰 발급
    GET_MOVIES(state, movies) {
      state.movies = movies
      console.log(this.movies)
      console.log("요청 받음")
    },
    GET_OTTS(state, otts) {
      state.otts = otts
      console.log(this.otts)
    },
    GET_SELECT(state, selects) {
      state.selects = selects
      console.log(this.selects)
    },
    // likes 관련
    


    // login 관련
    SAVE_USERNAME(state, username) {
      state.username = username
      console.log(this.username)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'MovieView'}) // store/index.js $router 접근 불가 -> import를 해야함
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
    // likes 관련
 
    // login 관련
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

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
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
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
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
        })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
