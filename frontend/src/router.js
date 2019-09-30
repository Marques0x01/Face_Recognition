import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/views/Main'
import Save from '@/views/SaveFile'
import Search from '@/views/SearchFile'
import List from '@/views/ListFile'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main,
      meta: { hideHeader: true }
    },
    {
      path: '/save',
      name: 'save',
      component: Save
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/list',
      name: 'list',
      component: List
    },
  ]
})
