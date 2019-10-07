<template>
  <div class="search">
    <h4 class="text-gray mb-3">Registrar</h4>
    <label for="input-file">Carregue um arquivo e adicione um nome para realizar o registro</label>
    <div class="row">
      <div class="form-group col">
        <input type="text" class="form-control" id="name" placeholder="Digite um nome" v-model="name" />
      </div>
      <div class="input-group mb-3 col">
        <div class="custom-file">
          <input type="file" class="custom-file-input" id="input-fle" @change="onLoadFile()" />
          <label class="custom-file-label text-dark-gray" for="input-fle">Selecione o arquivo</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "Register",
    date() {
        return {
            name: ""
        }
    },
    methods: {
        onLoadFile() {
            
        }
    }
}
</script>