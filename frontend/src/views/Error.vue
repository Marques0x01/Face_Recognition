<template>
  <div class="search-error d-flex">
    <div class="container text-center my-auto">
      <h2 class="mb-4">Nenhum terrorista encontrado</h2>
      <h5 class="mb-4">
        <p>
          Não foi possivel achar nenhum criminoso que corresponda a imagem carregada ao nosso sistema.
          <br />Por favor retorne para página inicial tente novamente para tentar novamente
        </p>
      </h5>
      <router-link to="/main" tag="button" class="btn btn-primary btn-sm">Retornar</router-link>
    </div>
  </div>
</template>
<script>
export default {
  name: "Landing"
};
</script>
<style lang="scss">
.search-error {
  background: url("../assets/app/error.png") no-repeat bottom fixed;
  background-color: #d04745;
  color: #ffffff;
  height: 100vh;
}
</style>
