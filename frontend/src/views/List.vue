<template>
  <div>
    <div v-for="(image, i) in databaseImages" :key="i">
      <h2>{{image.name}}</h2>
      <!-- <img :src="require(image.path)"> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "List",
  data() {
    return {
      databaseImages: []
    };
  },
  computed: {

  },
  mounted() {
    axios
      .get("/images")
      .then(res => {
        this.databaseImages = res.data;
        console.log(this.databaseImages);
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>