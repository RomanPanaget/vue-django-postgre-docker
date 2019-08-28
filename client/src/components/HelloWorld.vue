<template>
  <div class="hello">
    <h1>{{ helloMsg }}</h1>

    <h3>{{ question }}</h3>
    <div v-if="choices && choices.length > 0" class="inline">
      <button
        v-for="(choice, index) in choices"
        v-bind:key="index"
        class="button right-bottom-margin"
      >{{ choices[index] }}</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["helloMsg", "question", "choices"]
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.inline {
  margin: 20px auto;
  max-width: 500px;
}
.right-bottom-margin {
  margin: 2px 10px;
}
.button {
  color: #42b983;
  background-color: white;
  border-color: #42b983;
  font-size: 12px;
  border-radius: 50px;
  padding: 6px 12px;
  cursor: pointer;
  outline: none;
}
.button:hover,
.button:active {
  color: white;
  background-color: #42b983;
  border-color: white;
}
</style>
