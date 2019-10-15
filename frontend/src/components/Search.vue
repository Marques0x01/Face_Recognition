<template>
  <div class="search">
    <h4 class="text-green mb-3">Procurar</h4>
    <label for="input-file">Carregue um arquivo para realizar a busca</label>
    <div class="input-group mb-3">
      <div class="custom-file">
        <input type="file" class="custom-file-input" id="input-fle" @change="onLoadFile($event)" />
        <label class="custom-file-label text-dark-gray" for="input-fle">{{fileName}}</label>
      </div>
    </div>
    <div class="d-flex justify-content-end">
      <button class="btn btn-success btn-sm" @click="onSearchFile()" :disabled="Object.entries(file).length === 0">Pesquisar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Search",
  data() {
    return {
      name: "",
      file: ""
    };
  },
  methods: {
    onLoadFile(ev) {
      this.name = ev.target.files[0].name;
      this.file = ev.target.files[0];
    },
    onSearchFile(){
      this.$store.dispatch("searchImage", this.file);
      console.log("teste");
    }
  },
  computed: {
    fileName() {
      if(this.name === "" || this.name === undefined || this.name === null){
        return "Selecione o arquivo"
      }
      return this.name
    }
  }
};
</script>

<style lang="scss" scoped>
</style>