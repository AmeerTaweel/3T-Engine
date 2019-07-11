<template>
  <div id="app" class="w-100 h-100 p-5">
    
  </div>
</template>

<script lang="ts">
import { Vue } from 'vue-property-decorator';

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
