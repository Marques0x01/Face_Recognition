<template>
  <div class="container">
    <div class="results-header p-5">
      <h3 class="text-center mb-4">Abaixo você verá a foto e o nome da pessoa procurada</h3>
      <div class="results-option-item">
        <p>Voltar para pagina inicial</p>
      <router-link to="/main" tag="button" class="btn btn-success btn-sm">Clique aqui</router-link>
      </div>
    </div>

    <div class="results">
      <div class="result-item" v-for="(image, i) in storeResultImages" :key="i">
        <img class="result-image" :src="require(`@/assets/images/database/${image}`)" />
        <h4 class="my-2">{{filterName(image)}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Result",
  computed: {
    ...mapGetters({ storeResultImages: "resultImages" })
  },
  methods: {
    filterName(name) {
      return name.substring(0, name.indexOf("."));
    }
  },
  created() {
    if (!this.storeResultImages) {
      this.$router.push("/main");
    }
  },
  beforeDestroy() {
    this.$store.commit("resetResultImages");
  }
};
</script>

<style lang="scss" scoped>
.results {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.results-option {
  display: grid;
  grid-template-columns: 1fr;
  justify-items: center;
}

.results-option-item {
  display: grid;
  justify-items: center;
}

.result-header {
}
.result-item {
  display: grid;
  grid-template-columns: 1fr;
  justify-items: center;
}

.result-image {
  border-radius: 10px;
  border: solid 1px rgba(0, 0, 0, 0.253);
  width: 300px;
}
</style>