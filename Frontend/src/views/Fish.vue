<template>
  <div class="about">
    <v-container class="grey lighten-5">
      <v-row no-gutters>
        <v-col>
          <router-link :to="'/fish/FishDetails/' + input">
            <v-btn rounded x-large width="900" height="100" color="#98FB98">
              <v-img
                height="60px"
                width="60px"
                src="../assets/search.svg"
              ></v-img>
              <v-list-item-subtitle style="color: #228b22"
                >Search for specific fish</v-list-item-subtitle
              >
            </v-btn>
          </router-link>
          <v-text-field label="Enter fish" v-model="input"> </v-text-field>
          <v-col> </v-col>
        </v-col>
        <v-col>
          <v-btn rounded x-large width="900" height="100" color="#98FB98">
            <v-img
              height="60px"
              width="60px"
              src="../assets/category.svg"
            ></v-img>
            <v-list-item-subtitle style="color: #228b22"
              >Search by category</v-list-item-subtitle
            >
          </v-btn>
          <v-col> </v-col>
          <p>Random Number = {{ randomNumber }}</p>
          <v-btn flat color="#98FB98" @click="myFunction()">Randomize</v-btn>
        </v-col>
        <v-col>
          <router-link :to="'/fish/FishDetails/' + rand">
            <v-btn
              @click="randomFish()"
              rounded
              x-large
              width="900"
              height="100"
              color="#98FB98"
            >
              <v-img
                height="60px"
                width="60px"
                src="../assets/random.svg"
              ></v-img>
              <v-list-item-subtitle style="color: #228b22"
                >Learn about random fish</v-list-item-subtitle
              >
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Fish",
  components: {},

  data() {
    return {
      input: "",
      randomNumber: "",
      rand: "",
    };
  },
  methods: {
    submit() {
      console.log(this.input);
    },
    myFunction: function () {
      this.randomNumber = Math.random() * 10;
    },
    randomFish() {
      if (this.randomNumber < 1) {
        this.rand = "Pastrva";
      } else if (this.randomNumber > 1 && this.randomNumber < 2) {
        this.rand = "Srdela";
      } else if (this.randomNumber > 2 && this.randomNumber < 3) {
        this.rand = "Oslić";
      }
    },
  },
};
</script>
