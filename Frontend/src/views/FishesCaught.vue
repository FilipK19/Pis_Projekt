<template>
  <div>
    <h3 style="color: #228b22" v-for="f in fishData" v-bind:key="f">
      <h3 v-for="a in f" v-bind:key="a">
        <h3 v-if="a.vrsta != undefined">
          {{ "Ime: " + a.vrsta + " | " }}
          {{ "Vrsta: " + a.voda + " | " }}
          {{ "Mjesto: " + a.lokacija }}
        </h3>
      </h3>
    </h3>
  </div>
</template>

<script>
export default {
  name: "FishDetails",
  props: ["fish"],
  async mounted() {
    let response = await fetch("http://localhost:3000//upecaneribe/vrati");
    console.log(response);
    let data = await response.json();
    this.fishData = data;
  },
  data() {
    return {
      fishData: [],
    };
  },
};
</script>
