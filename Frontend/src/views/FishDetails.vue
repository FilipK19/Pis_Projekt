<template>
  <div class="fish">
    <v-card color="#98FB98">
      <h3 style="color: #228b22" v-for="f in fishData" v-bind:key="f">
        <h3 v-for="a in f" v-bind:key="a">
          <h3 v-if="fish == a.vrsta">
            {{ "Ime Ribe: " + a.vrsta }} <br />
            {{ "Vrsta Ribe: " + a.voda }} <br />
            {{ "Lokacije za pecat: " + a.lokacija }}
          </h3>
        </h3>
      </h3>
    </v-card>
    <h2 v-if="fish == 'Pastrva'">
      <v-img
        height="380px"
        width="1380px"
        src="../FishPictures/pastrva.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Brancin'">
      <v-img
        height="390px"
        width="1080px"
        src="../FishPictures/brancin.png"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Orada'">
      <v-img
        height="400px"
        width="680px"
        src="../FishPictures/orada.png"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Zubatac'">
      <v-img
        height="390px"
        width="960px"
        src="../FishPictures/zubatac.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Cipal'">
      <v-img
        height="390px"
        width="1260px"
        src="../FishPictures/cipal.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Škrapina'">
      <v-img
        height="390px"
        width="860px"
        src="../FishPictures/škrapina.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Arbun'">
      <v-img
        height="390px"
        width="1060px"
        src="../FishPictures/arbun.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Trilja'">
      <v-img
        height="380px"
        width="860px"
        src="../FishPictures/trlja.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Ugor'">
      <v-img
        height="380px"
        width="960px"
        src="../FishPictures/ugor.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Morska Mačka'">
      <v-img
        height="290px"
        width="1260px"
        src="../FishPictures/morskamacka.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Skuša'">
      <v-img
        height="290px"
        width="860px"
        src="../FishPictures/skusa.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Tuna'">
      <v-img
        height="390px"
        width="960px"
        src="../FishPictures/tuna.png"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Špar'">
      <v-img
        height="390px"
        width="860px"
        src="../FishPictures/spar.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Šaran'">
      <v-img
        height="390px"
        width="960px"
        src="../FishPictures/saran.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Som'">
      <v-img height="370px" width="960px" src="../FishPictures/som.jpg"></v-img>
    </h2>
    <h2 v-if="fish == 'Smuđ'">
      <v-img
        height="350px"
        width="960px"
        src="../FishPictures/smud.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Štuka'">
      <v-img
        height="390px"
        width="1160px"
        src="../FishPictures/stuka.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Kečiga'">
      <v-img
        height="350px"
        width="960px"
        src="../FishPictures/keciga.png"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Lipljen'">
      <v-img
        height="350px"
        width="1160px"
        src="../FishPictures/lipljen.jpg"
      ></v-img>
    </h2>
    <h2 v-if="fish == 'Mladica'">
      <v-img
        height="370px"
        width="1360px"
        src="../FishPictures/mladica.jpg"
      ></v-img>
    </h2>
  </div>
</template>

<script>
export default {
  name: "FishDetails",
  props: ["fish"],
  async mounted() {
    let response = await fetch("http://localhost:3000/ribe/vrati");
    console.log(response);
    let data = await response.json();
    this.fishData = data;
  },
  data() {
    return {
      fishData: [],
      picture: "",
    };
  },
};
</script>
