<template>
  <div class="app-landing d-flex">
    <div class="container text-center my-auto">
      <h1 class="mb-1">A Procura Criminosos Ambientais</h1>
      <h5>
        Encontre informações dos maiores criminosos com nossa tecnologia de reconhecimento facial.
        <br />
      </h5>
      <h5 class="mb-4">
        <p>Vamos começar ?</p>
      </h5>
      <router-link to="/main" tag="button" class="btn btn-primary font-weight-bold">Vamos</router-link>
    </div>
  </div>
</template>
<script>
export default {
  name: "Landing"
};
</script>
<style lang="scss">
.app-landing {
  height: 100vh;
  background: url("../assets/app/bg-green.jpg") no-repeat center center fixed;
  background-size: cover;
  color: #ffffff;
  text-shadow: 1px 1px #0c0b0b;
}
</style>
