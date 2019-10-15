import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'
import router from './router'
const fs = require("fs");

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    databaseImages: [],
    resultImages: [],
    loading: false
  },
  getters: {
    databaseImages: state => state.databaseImages,
    resultImages: state => state.resultImages
  },
  mutations: {
    loadImages(state) {
      fs.readdir(process.cwd() + "/src/assets/images/database", (err, files) => {
        if (err) {
          return console.log("Unable to scan directory: " + err);
        }
        state.databaseImages = files;
      });
    },
    resetResultImages(state) {
      state.resultImages = []
    }
  },
  actions: {
    searchImage({ state }, payload) {
      state.loading = true;
      let image = {
        path: payload.path
      }
      Axios.post('recognition', image).then((res) => {
        if(!res.data){
          router.push("/Error")
          return;
        }
        router.push("/result")
        state.resultImages = res.data;

      })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => state.loading = false)
    }
  }
})
