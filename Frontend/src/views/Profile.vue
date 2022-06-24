<template>
  <div class="profile">
    {{ profil }}
    <v-container class="grey lighten-5">
      <v-row no-gutters>
        <v-col>
          <v-card width="344" height="300" color="#98FB98">
            <v-img
              height="250px"
              width="345px"
              src="../assets/profile.svg"
            ></v-img>
            <h1 v-for="p in profil" v-bind:key="p" style="color: #228b22">
              <h4 v-for="a in p" v-bind:key="a" style="color: #228b22">
                {{ a.ime }} {{ a.prezime }}
              </h4>
            </h1>
          </v-card>
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
  },

  data() {
    return {
      profil: [],
    };
  },
};
</script>
