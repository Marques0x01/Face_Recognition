<template>
  <div class="register">
    <h4 class="text-green mb-3">Registrar</h4>
    <label for="input-file">Carregue um arquivo e adicione um nome para realizar o registro</label>
    <div class="row">
      <div class="form-group col">
        <input type="text" class="form-control" placeholder="Digite um nome" v-model="name" />
      </div>
      <div class="input-group mb-3 col">
        <div class="custom-file">
          <input type="file" class="custom-file-input" id="input-file" @change="onLoadFile($event)" />
          <label class="custom-file-label text-dark-gray" for="input-file">{{fileName}}</label>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-end">
      <button class="btn btn-success btn-sm" @click="onSaveImage()" :disabled="fieldValidation">Registrar</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      file: {},
      name: ""
    };
  },
  methods: {
    onLoadFile(ev) {
      this.file = {
        name: ev.target.files[0].name,
        path: ev.target.files[0].path
      }
    },
    onSaveImage() {
      this.file.name = this.name;
      axios
        .post("/save-image", this.file)
        .then(res => {
          this.file = {};
          this.name = ""
          alert("Saved")
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    fileName() {
      if (this.file.name === "" || this.file.name === undefined || this.file.name === null) {
        return "Selecione o arquivo";
      }
      return this.file.name.substring(17,0)
    },
    fieldValidation(){
      return Object.entries(this.file).length == 0 || this.name === "" || this.name === undefined || this.name === null;
    }
  }
};
</script>

<style lang="scss" scoped>
</style>