<template>
  <div id="dropzone">
    <div class="drop m-2">
      <input type="file" class="input-file" @change="onLoadFile" />
      <p>Drag your file here</p>
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
.drop {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  cursor: pointer;
  outline: 2px dashed rgb(255, 255, 255);
  outline-offset: -10px;
  background: #adadad;
  color: rgb(255, 255, 255);
  text-shadow: black 0.1em 0.1em 0.2em;
  height: 89%;
  width: 98%;
  &:hover {
    background: rgb(196, 196, 196);
  }
}

.drop-light {
  outline: 2px dashed rgb(68, 68, 68);
  background: #e2e3e5;
  color: #383d41;
  text-shadow: none;
  &:hover {
    background: rgb(209, 209, 209);
  }
}

.input-file {
  opacity: 0;
  width: 100%;
  height: 100%;
  position: absolute;
  cursor: pointer;
}
</style>