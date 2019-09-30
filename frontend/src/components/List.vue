<template>
  <button class="btn btn-primary" @click="getImages">OK</button>
</template>

<script>
import axios from "axios";
export default {
  name: "List",
  methods: {
    getImages() {
      axios
        .get("/images")
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  create() {
    console.log("teste");
  }
};
</script>