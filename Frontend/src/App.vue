<template>
  <div id="app">
    <div id="nav">
      <!--<router-link to="/">Home</router-link> |
      <router-link to="/store">Store</router-link> |
      <router-link to="/profile">Profile</router-link>-->
      <v-toolbar dark prominent src="./assets/bar.png"> </v-toolbar>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style lang="scss">
#app {
  background-image: url(./assets/backg.png);
  background-size: cover;
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
