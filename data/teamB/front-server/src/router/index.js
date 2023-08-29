import Vue from 'vue'
import VueRouter from 'vue-router'
import IntroView from '@/views/IntroView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MovieView from '@/views/MovieView'
import RecommendView from '@/views/RecommendView'
import AccountsView from '@/views/AccountsView'
import MyFirstOttView from '@/views/MyFirstOttView'
import MovieDetail from '@/components/MovieList/MovieDetail'


Vue.use(VueRouter)

const routes = [
  
  {
    path: '/',
    name: 'IntroView',
    component: IntroView
  },

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
    path: '/accounts',
    name: 'AccountsView',
    component: AccountsView
  },
  {
    path: '/ott',
    name: 'MyFirstOttView',
    component: MyFirstOttView
  },
  
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
