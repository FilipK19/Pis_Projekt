<template>
  <div class="profile">
    <v-container class="grey lighten-5">
      <v-row no-gutters>
        <v-col>
          <v-card width="344" height="300" color="#98FB98">
            <v-img
              height="220px"
              width="335px"
              src="../assets/profile.svg"
            ></v-img>
            <h1 v-for="p in profil" v-bind:key="p" style="color: #228b22">
              <h4 v-for="a in p" v-bind:key="a" style="color: #228b22">
                {{ a.ime }} {{ a.prezime }}
              </h4>
            </h1>
            <h3 style="color: #228b22" v-for="f in fishData" v-bind:key="f">
              <h3 v-for="a in f" v-bind:key="a">
                <h3 v-if="a.vrsta != undefined">
                  {{ a.id }}
                </h3>
              </h3>
            </h3>
            {{ i }}
          </v-card>
        </v-col>
        <v-col>
          <router-link :to="'/profile/upload/'">
            <v-btn width="344" height="150" color="#98FB98">
              <v-img
                height="150px"
                width="150px"
                src="../assets/upload.svg"
              ></v-img>
              <h1 style="color: #228b22">Upload</h1>
            </v-btn>
          </router-link>
          <v-col></v-col>
          <v-col>
            <router-link :to="'/profile/statistics/'">
              <v-btn width="344" height="150" color="#98FB98">
                <v-img
                  height="150px"
                  width="150px"
                  src="../assets/statistic.svg"
                ></v-img>
                <h2 style="color: #228b22">Fishes caught</h2>
              </v-btn>
            </router-link>
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Profile",
  async mounted() {
    let response = await fetch("http://127.0.0.1:3000/profil/vrati");
    console.log(response);
    let data = await response.json();
    this.profil = data;
    let response2 = await fetch("http://localhost:3000//upecaneribe/vrati");
    console.log(response2);
    let data2 = await response2.json();
    this.fishData = data2;
  },

  data() {
    return {
      profil: [],
      fishData: [],
      i: 0,
    };
  },
};
</script>
