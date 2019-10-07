<template>
  <div id="main" class="container">
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