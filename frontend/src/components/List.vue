<template>
  <div class="list mt-4">
    <h4 class="text-green mb-3">Pesquisar</h4>
    <div class="list-form-group mb-3">
      <input
        type="text"
        class="form-control list-input"
        id="list-search"
        placeholder="Digite aqui o nome"
        v-model="searchName"
      />
    </div>
    <div class="list-items" align-h="around">
      <div class="list-item" v-for="(image, i) in filteredImages" :key="i">
        <img class="list-img" :src="require(`@/assets/images/database/${image}`)" />
        <h4 class="text-center my-2">{{filterName(image)}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "List",
  data() {
    return {
      searchName: ""
    };
  },
  methods: {
    filterName(name) {
      return name.substring(0, name.indexOf("."));
    }
  },
  computed: {
    filteredImages() {
      return this.$store.state.databaseImages.filter(img => {
        return img.match(this.searchName);
      });
    }
  },
  created() {
    this.$store.commit("loadImages");
  }
};
</script>

<style lang="scss" scoped>
.list-img {
  width: 100%;
  height: 250px;
  border: solid 1px rgba(0, 0, 0, 0.253);
  border-radius: 10px;
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
}

.list-items {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  row-gap: 50px;
  column-gap: 150px;
  justify-content: space-around;
}

.list-item {
  border-radius: 10px;
  border: solid 1px rgba(0, 0, 0, 0.253);
}

.list-input {
  width: 500px;
}
</style>