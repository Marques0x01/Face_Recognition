<template>
  <div class="list mt-4">
    <h4 class="text-gray mb-3">Pesquisar</h4>
    <div class="list-form-group mb-3">
      <input
        type="text"
        class="form-control list-input"
        id="list-search"
        placeholder="Digite aqui o nome"
        v-model="searchName"
      />
    </div>
    <div class="list-items" align-h="around">
      <div class="list-item" v-for="(image, i) in filteredImages" :key="i">
        <img class="list-img" :src="require(`@/assets/images/database/${image}`)" />
        <h4 class="text-center my-2">{{image}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const fs = require("fs");

export default {
  name: "Main",
  data() {
    return {
      databaseImages: [],
      searchName: ""
    };
  },
  mounted() {
    let vm = this;
    fs.readdir(process.cwd() + "/src/assets/images/database", (err, files) => {
      if (err) {
        return console.log("Unable to scan directory: " + err);
      }
      vm.databaseImages = files;
    });
  },
  computed: {
    filteredImages() {
      return this.databaseImages.filter(img => {
        return img.match(this.searchName);
      });
    }
  }
};
</script>