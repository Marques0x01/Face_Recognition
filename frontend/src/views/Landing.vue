<template>
  <div class="app-landing d-flex">
    <div class="container text-center my-auto">
      <h1 class="mb-1">Reconhecimento Facial</h1>
      <h3 class="mb-4">
        <p>Vamos começar ?</p>
      </h3>
      <router-link to="/main" tag="button" class="btn btn-primary font-weight-bold">Vamos</router-link>
    </div>
  </div>
</template>
<script>
export default {
    name: "Landing"
}
</script>
<style lang="scss">
.app-landing {
  height: 100vh;
  background: url("../assets/app/bg-green.jpg") no-repeat center center fixed;
  background-size: cover;
  color: #ffffff;
  text-shadow: 2px 2px #0c0b0b;
}

@mixin for-phone-only {
  @media (max-width: 599px) {
    transition: 1s;
    @content;
  }
}

.app-landing h1 {
  font-size: 4em;
      transition: 1s;

  @include for-phone-only {
    font-size: 2.5em;
  }
}
</style>
