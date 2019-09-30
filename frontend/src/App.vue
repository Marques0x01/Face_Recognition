<template>
  <div id="app">
    <Header v-if="!$route.meta.hideHeader" />
    <router-view></router-view>
  </div>
</template>

<script>
import Header from "@/components/Header";
export default {
  name: "app",
  components: {
    Header
  },
  methods: {
    testes() {
      $router.push("/search");
    }
  }
};
</script>

<style>
</style>
