<template>
  <div id="app">
    <Header />
    <!-- <Dropzone /> -->
    <List />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Dropzone from '@/components/Dropzone.vue'
import List from '@/components/List.vue'

export default {
  name: "app",
  components: {
    Header,
    Dropzone,
    List
  }
};
</script>

<style>

</style>
