import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'
const fs = require("fs");

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    databaseImages: []
  },
  getters: {
    databaseImages: state => state.databaseImages
  },
  mutations: {
    loadImages(state) {
      fs.readdir(process.cwd() + "/src/assets/images/database", (err, files) => {
        if (err) {
          return console.log("Unable to scan directory: " + err);
        }
        state.databaseImages = files;
      });
    }
  },
  actions: {
    searchImage({ }, payload) {
      let image = {
        path: payload.path
      }
      Axios.post('recognition', image).then((res) => {
        console.log(res);
      })
        .catch((error) => {
          console.error(error);
        });
    }
  }
})
