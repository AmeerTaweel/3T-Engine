<template>
  <div id="app" class="w-100 h-100 p-5">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from './components/HelloWorld.vue';

@Component({
  components: {
    HelloWorld,
  },
})
export default class App extends Vue {}
</script>

<style lang="sass">
// Color Variables
$pickled-bluewood: #2c3e50
$ocean-green: #42B983
$white: #ffffff

// Theme
$primary-color: $ocean-green
$secondary-color: $pickled-bluewood

#app 
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: $secondary-color
  background-color: $primary-color
  overflow: hidden
</style>
