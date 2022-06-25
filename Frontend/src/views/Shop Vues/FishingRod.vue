<template>
  <div>
    {{ status }}
    <v-container>
      <v-row>
        <v-col>
          <v-btn width="800" height="200" color="#98FB98">
            <v-img
              height="200px"
              width="235px"
              src="../../shop/Sougayilang.jpg"
            ></v-img>
            <h1>Sougayilang</h1>
            <v-btn @click="select(), createPost()">Purchase</v-btn>
          </v-btn>
        </v-col>
        <v-col>
          <v-btn width="800" height="200" color="#98FB98">
            <v-img
              height="200px"
              width="335px"
              src="../../shop/RAD.jpeg"
            ></v-img>
            <h1>RAD</h1>
            <v-btn @click="select2(), createPost()">Purchase</v-btn>
          </v-btn>
        </v-col>
        <v-col>
          <v-btn width="800" height="200" color="#98FB98">
            <v-img
              height="200px"
              width="335px"
              src="../../shop/PLUSINNO.jpg"
            ></v-img>
            <h1>PLUSINNO</h1>
            <v-btn @click="select3(), createPost()">Purchase</v-btn>
          </v-btn>
        </v-col>
        <v-col>
          <v-btn width="800" height="200" color="#98FB98">
            <v-img
              height="200px"
              width="335px"
              src="../../shop/Zebco.png"
            ></v-img>
            <h1>Zebco</h1>
            <v-btn @click="select4(), createPost()">Purchase</v-btn>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "FishingPost",
  data() {
    return {
      stvar: "",
      vrsta: "",
      cijena: "",
      status: "",
    };
  },
  methods: {
    select() {
      this.stvar = "Sougayilang";
      this.vrsta = "pecaljka";
      this.cijena = 70;
      this.status = "Kupljeno";
      console.log(this.stvar);
    },
    select2() {
      this.stvar = "RAD";
      this.vrsta = "pecaljka";
      this.cijena = 30;
      this.status = "Kupljeno";
      console.log(this.stvar);
    },
    select3() {
      this.stvar = "PLUSINNO";
      this.vrsta = "pecaljka";
      this.cijena = 40;
      this.status = "Kupljeno";
      console.log(this.stvar);
    },
    select4() {
      this.stvar = "Zebco";
      this.vrsta = "pecaljka";
      this.cijena = 10;
      this.status = "Kupljeno";
      console.log(this.stvar);
    },
    createPost() {
      axios
        .post("http://127.0.0.1:3000/trgovina/dodaj", {
          stvar: this.stvar,
          vrsta: this.vrsta,
          cijena: this.cijena,
        })
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
      console.log("function called");
    },
  },
};
</script>
