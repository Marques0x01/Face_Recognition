<template>
  <div>
    <div v-for="(image, i) in databaseImages" :key="i">
      <h2>{{image}}</h2>
      <img :src="require(`@/assets/images/database/${image}`)" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
const fs = require("fs");

export default {
  name: "List",
  data() {
    return {
      databaseImages: []
    };
  },
  computed: {},
  mounted() {
    let vm = this;
    fs.readdir(process.cwd() + "/src/assets/images/database", (err, files) => {
      if (err) {
        return console.log("Unable to scan directory: " + err);
      }
      vm.databaseImages = files;
    });
  }
};
</script>