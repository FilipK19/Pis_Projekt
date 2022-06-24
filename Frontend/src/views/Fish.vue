<template>
  <div class="about">
    <v-container class="grey lighten-5">
      <v-col no-gutters>
        <v-col>
          <v-text-field label="Enter fish name" v-model="input"> </v-text-field>
          <router-link :to="'/fish/FishDetails/' + input">
            <v-btn rounded x-large width="400" height="70" color="#98FB98">
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
        </v-col>
        <v-col>
          <v-btn rounded x-large width="400" height="70" color="#98FB98">
            <v-img
              height="60px"
              width="60px"
              src="../assets/category.svg"
            ></v-img>
            <v-list-item-subtitle style="color: #228b22"
              >Search by category</v-list-item-subtitle
            >
          </v-btn>
        </v-col>
        <v-col>
          <router-link :to="'/fish/FishDetails/' + rand">
            <v-btn
              @click="randomNum(), randomFish()"
              rounded
              x-large
              width="400"
              height="70"
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
      </v-col>
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
      ranFish: "",
      rand: "Pastrva",
    };
  },
  methods: {
    submit() {
      console.log(this.input);
    },

    randomNum: function () {
      this.randomNumber = Math.floor(Math.random() * (21 - 1 + 1) + 1);
    },

    randomFish() {
      if (this.randomNumber == 1) {
        this.rand = "Pastrva";
      } else if (this.randomNumber == 2) {
        this.rand = "Brancin";
      } else if (this.randomNumber == 3) {
        this.rand = "Orada";
      } else if (this.randomNumber == 4) {
        this.rand = "Zubatac";
      } else if (this.randomNumber == 5) {
        this.rand = "Cipal";
      } else if (this.randomNumber == 6) {
        this.rand = "Škrapina";
      } else if (this.randomNumber == 7) {
        this.rand = "Arbun";
      } else if (this.randomNumber == 8) {
        this.rand = "Trilja";
      } else if (this.randomNumber == 9) {
        this.rand = "Ugor";
      } else if (this.randomNumber == 10) {
        this.rand = "Morska Mačka";
      } else if (this.randomNumber == 11) {
        this.rand = "Skuša";
      } else if (this.randomNumber == 12) {
        this.rand = "Šaran";
      } else if (this.randomNumber == 13) {
        this.rand = "Tuna";
      } else if (this.randomNumber == 14) {
        this.rand = "Špar";
      } else if (this.randomNumber == 15) {
        this.rand = "Šaran";
      } else if (this.randomNumber == 16) {
        this.rand = "Som";
      } else if (this.randomNumber == 17) {
        this.rand = "Smuđ";
      } else if (this.randomNumber == 18) {
        this.rand = "Štuka";
      } else if (this.randomNumber == 19) {
        this.rand = "Kečiga";
      } else if (this.randomNumber == 20) {
        this.rand = "Lipljen";
      } else if (this.randomNumber == 21) {
        this.rand = "Mladica";
      }
    },
  },
};
</script>
