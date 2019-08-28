<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld :helloMsg="msg" :question="data.question" :choices="data.choices" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "app",
  components: {
    HelloWorld
  },
  data() {
    return {
      msg: "Hello Template",
      data: {
        question: "Any questions in the server so far",
        choices: []
      }
    };
  },
  mounted: function() {
    axios
      .get("http://localhost:8000/polls/1/", {
        headers: { Accept: "application/json" }
      })
      .then(response => {
        console.log(response);
        this.data = response.data;
      });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
