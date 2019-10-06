<template>
  <div class="list container">
    <div class="form-group mt-5">
      <label for="list-search">Digite o nome:</label>
      <input
        type="text"
        class="form-control"
        id="list-search"
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

<style lang="scss" scoped>
.list-img {
  width: 350px;
  height: 350px;
  border: solid 1px rgba(0, 0, 0, 0.253);
  border-radius: 10px;
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
}

.list-items {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  row-gap: 50px;
  justify-items: center;
}

.list-item {
  border-radius: 10px;
  border: solid 1px rgba(0, 0, 0, 0.253);
}
</style>