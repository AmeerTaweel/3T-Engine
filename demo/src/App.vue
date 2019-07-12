<template>
  <div id="app" class="w-100 h-100 p-3">
    <div id="screen" class="d-flex flex-column align-items-center h-100">
      <h1>3T Tic Tac Toe Engine Demo</h1>
      <div id="canvas" class="m-4 flex-grow-1 bg-white rounded border border-dark">
        <div class="w-100 h-100 d-flex flex-wrap">
          <div
            class="cell d-flex justify-content-center align-items-center display-1 border border-dark"
            v-for="(cell, i) in game"
            :key="i"
          >{{cell}}</div>
        </div>
      </div>
      <h1>Player: 0 | Tie: 0 | Computer: 0</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: `app`,
  data() {
    return {
      game: [`X`, `O`, `X`, `X`, `O`, `X`, `X`, `O`, `X`]
    };
  },
  methods: {
    maintainAspectRatio() {
      const screen = document.getElementById(`screen`);
      const canvas = document.getElementById(`canvas`);
      canvas.style.width = `${canvas.offsetHeight}px`;
      if (canvas.offsetHeight > screen.offsetWidth) {
        canvas.style.width = `${screen.offsetWidth}px`;
        canvas.style.height = `${screen.offsetWidth}px`;
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      // The whole view is rendered, so the DOM can be accessed safely
      this.maintainAspectRatio();
      window.addEventListener("resize", () => {
        this.maintainAspectRatio();
      });
    });
  }
};
</script>

<style lang="sass">
// Color Variables
$pickled-bluewood: #273849
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

.cell
	width: (1 / 3) * 100%
	height: (1 / 3) * 100%
	color: $secondary-color
</style>
