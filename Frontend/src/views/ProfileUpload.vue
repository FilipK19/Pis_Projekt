<template>
  <div>
    <form @submit.prevent="createPost">
      <div>
        <label for="vrsta">Napišite ime upecane ribe </label>
        <input type="text" id="vrsta" v-model="formData.vrsta" />
      </div>
      <div>
        <label for="voda">Napišite vrstu upecane ribe </label>
        <input type="text" id="voda" v-model="formData.voda" />
      </div>
      <div>
        <label for="lokacija">Napišite gdje ste ju upecali </label>
        <input type="text" id="lokacija" v-model="formData.lokacija" />
      </div>
      <button>Create Post</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProfilUpload",
  data() {
    return {
      formData: {
        vrsta: "",
        voda: "",
        lokacija: "",
      },
    };
  },
  methods: {
    createPost() {
      axios
        .post("http://127.0.0.1:3000/upecaneribe/dodaj", this.formData)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
      console.log("function called");
    },
  },
};
</script>

<style scoped></style>
