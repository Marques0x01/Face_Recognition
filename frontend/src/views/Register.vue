<template>
    <div>
        <input type="file" @change="onLoadImage">
        <input type="text" v-model="imageName">
        <button class="btn btn-primary" @click="onSaveImage">Save Image</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Register",
    data(){
        return {
            loadedImage: null,
            imageName: ""
        }
    },
    methods: {
        onLoadImage(ev) {
            let file = ev.target.files[0];
            this.loadedImage = {
                name: file.name,
                path: file.path
            }
        },
        onSaveImage() {
            this.loadedImage.name = this.imageName
            console.log(this.loadedImage);
            axios.post("/save-image", this.loadedImage).then(res => {
                console.log(res);
            }).catch(err => {
                console.log(err);
            })
        }
    }
}
</script>