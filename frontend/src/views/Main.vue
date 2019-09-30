<template>
  <div>
    <button @click="testes()">teste</button>
  </div>
</template>

<script>
export default {
  name: "Main",
  methods: {
    testes(){
      this.$router.push("/search")
    }
  }
};
</script>