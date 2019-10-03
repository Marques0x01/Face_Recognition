<template>
  <div id="app">
    <Header />
    <Register />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Dropzone from "@/components/Dropzone.vue";
import List from "@/views/List.vue";
import Register from "@/views/Register.vue"

export default {
  name: "app",
  components: {
    Header,
    Dropzone,
    List,
    Register
  }
};
</script>

<style>
</style>
