<template>
  <div class="main d-flex">
    <div class="container text-center my-auto">
      <h1 class="mb-1">Reconhecimento Facial</h1>
      <h3 class="mb-4">
        <p>Vamos começar ?</p>
      </h3>
      <router-link to="/search" tag="button" class="btn btn-primary font-weight-bold">Vamos</router-link>
    </div>
    <div class="overlay"></div>
  </div>
</template>

<script>
export default {
  name: "Main"
};
</script>

<style lang="scss" scoped>
.main {
  height: 100vh;
  background: url("../assets/app/bg-green.jpg") no-repeat center center fixed;
  background-size: cover;
  color: #ffffff;
  text-shadow: 2px 2px #0c0b0b;
}
</style>