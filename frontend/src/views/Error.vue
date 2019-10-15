<template>
  <div class="search-error d-flex">
    <div class="container text-center my-auto">
      <h2 class="mb-4">Erro no reconhecimento</h2>
      <h5 class="mb-4">
        <p>
          Não foi possivel achar nenhuma imagem correspondente a imagem carregada ao nosso sistema.
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
  height: 100vh;
}
</style>
