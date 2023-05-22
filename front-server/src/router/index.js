import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MovieView from '@/views/MovieView'
import RecommendView from '@/views/RecommendView'
import MovieDetail from '@/components/MovieList/MovieDetail'
import SearchMovie from '@/components/MovieList/SearchMovie'


Vue.use(VueRouter)

const routes = [
  
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  {
    path: '/search-movie',
    name: 'SearchMovie',
    component: SearchMovie,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router