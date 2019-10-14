<template>
  <div id="main" class="container" v-if="!$store.state.loading">
    <div class="row mt-4">
      <div class="col-xs-12 col-md-6 app-search p-3">
        <Search />
      </div>
      <div class="col-xs-12 col-md-6 app-register p-3">
        <Register />
      </div>
    </div>
    <List />
  </div>
  <div class="loading d-flex" v-else>
    <div class="container d-flex justify-content-center my-auto">
      <div class="spinner-border text-success" style="width: 5rem; height: 5rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
import List from "@/components/List";
import Search from "@/components/Search";
import Register from "@/components/Register";

export default {
  name: "Main",
  components: {
    List,
    Search,
    Register
  }
};
</script>
<style lang="scss" scoped>
</style>