import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    image: null
  },
  getters: {
    image: state => state.image 
  },
  mutations: {
    'SET_IMAGE'(state, payload){
      state.image = payload;
    }
  },
  actions: {
    loadImage({ commit }, payload) {
      let image = {
        path: payload.path
      }
      commit('SET_IMAGE', payload)
      Axios.post('recognition', image).then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.error(error);
      });
    }
  }
})
