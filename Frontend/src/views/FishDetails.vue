<template>
  <div class="fish">
    <h2 v-for="f in fishData" v-bind:key="f">
      <h2 v-if="fish == f.vrsta">
        {{ f.vrsta + " " + f.voda }} {{ (i = i + 1) }}
      </h2>
    </h2>
    <h4 v-if="i == 0">No {{ i }}</h4>
    <h5 v-if="fish == fish1">
      <v-img
        height="225px"
        width="450px"
        src="../FishPictures/pastrva.jpg"
      ></v-img>
    </h5>
  </div>
</template>

<script>
export default {
  name: "FishDetails",
  props: ["fish"],
  async mounted() {
    let response = await fetch("http://localhost:3000/fish");
    console.log(response);
    let data = await response.json();
    this.fishData = data;
  },
  data() {
    return {
      fishData: [],
      fishyo: "",
      i: -100,
      fish1: "Pastrva",
      fish2: "Srdela",
    };
  },
};
</script>
