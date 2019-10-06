<template>
  <div class="dropzone d-flex">
    <div class="container text-center my-auto">
      <div class="mb-4">
        <h1 class="mb-2">Faça o carregamento de fotos para realizar a pesquisa!</h1>
        <p>Para começar é muito facil. Carregue um arquivo de uma foto para que possamos analisar e retornamos a você o nome e a foto através do processo de reconhecimento facial.</p>
      </div>
      <div class="custom-file">
        <input type="file" class="custom-file-input" id="customFileLang" lang="es" />
        <label class="custom-file-label" for="customFileLang">Seleccionar Archivo</label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dropzone",
  methods: {
    onLoadFile(ev) {
      this.$store.dispatch("loadImage", ev.target.files[0]);
    }
  }
};
</script>

<style lang="scss" scoped>
.dropzone {
  height: 100vh;
}
</style>