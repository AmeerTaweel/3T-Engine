<template>
  <div id="app" class="w-100 h-100 p-3">
    <div class="d-flex flex-column align-items-center h-100">
      <h1>3T Tic Tac Toe Engine Demo</h1>
      <div class="w-75 m-4 flex-grow-1 bg-white rounded border-secondary">edf</div>
      <h1>Player: 0 | Tie: 0 | Computer: 0</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
}
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
  color: white
  background-color: $primary-color
  overflow: hidden

.border-secondary
  border: 3px solid $secondary-color
</style>
