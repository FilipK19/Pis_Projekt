<template>
  <div>
    <form @submit.prevent="createPost">
      <div>
        <label for="stvar">Post stvar </label>
        <input type="text" id="stvar" v-model="formData.stvar" />
      </div>
      <div>
        <label for="namjena">Post namjena </label>
        <input type="text" id="namjena" v-model="formData.namjena" />
      </div>
      <div>
        <label for="cijena">Post cijena </label>
        <input type="text" id="cijena" v-model="formData.cijena" />
      </div>
      <button>Create Post</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CreatePost",
  data() {
    return {
      formData: {
        stvar: "",
        namjena: "",
        cijena: "",
      },
    };
  },
  methods: {
    createPost() {
      axios
        .post("http://127.0.0.1:3000/stvar/dodaj", this.formData)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
      console.log("function called");
    },
  },
};
</script>

<style scoped></style>
