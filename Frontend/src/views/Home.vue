<template>
  <div class="home">
    <v-container class="grey lighten-5">
      <v-row no-gutters>
        <v-col>
          <v-btn rounded width="344" height="300" color="#98FB98">
            <router-link to="/profile">
              <v-img
                height="225px"
                width="300px"
                src="../assets/profile.svg"
              ></v-img>
              <v-list-item-subtitle style="color: #228b22"
                >Your profile</v-list-item-subtitle
              >
            </router-link>
          </v-btn>
        </v-col>
        <v-col>
          <v-btn rounded width="344" height="300" color="#98FB98">
            <router-link to="/store">
              <v-img
                height="225px"
                width="300px"
                src="../assets/store.svg"
              ></v-img>
              <v-list-item-subtitle style="color: #228b22"
                >Buy stuff</v-list-item-subtitle
              >
            </router-link>
          </v-btn>
        </v-col>
        <v-col>
          <v-btn rounded width="344" height="300" color="#98FB98">
            <router-link to="/fish">
              <v-img
                height="225px"
                width="300px"
                src="../assets/fish.svg"
              ></v-img>
              <v-list-item-subtitle style="color: #228b22"
                >Your fish</v-list-item-subtitle
              >
            </router-link>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},

  data() {
    return {};
  },
};
</script>

<style></style>
