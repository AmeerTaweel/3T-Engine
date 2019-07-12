<template>
  <div id="app" class="w-100 h-100 p-3">
    <div id="screen" class="d-flex flex-column align-items-center h-100">
      <h1 class="unselectable-text">3T Tic Tac Toe Engine Demo</h1>
      <div id="canvas" class="m-4 flex-grow-1 bg-white rounded border border-dark">
        <div class="w-100 h-100 d-flex flex-wrap">
          <div class="cell d-flex justify-content-center align-items-center display-1 border border-dark" v-for="(cell, i) in gameDisp" :key="i" @click="userInput(i)">{{cell}}</div>
        </div>
      </div>
      <h1 class="unselectable-text">Player: 0 | Tie: 0 | Computer: 0</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: `app`,
  data() {
    return {
      gameDisp: [],
      game: [],
      types: [],
      blockUserInput: true
    };
  },
  methods: {
    maintainAspectRatio() {
      const screen = document.getElementById(`screen`)
      const canvas = document.getElementById(`canvas`)
      canvas.style.width = `${canvas.offsetHeight}px`
      if (canvas.offsetHeight > screen.offsetWidth) {
        canvas.style.width = `${screen.offsetWidth}px`
        canvas.style.height = `${screen.offsetWidth}px`
      }
    },
    newGame() {
      this.gameDisp = new Array(9).fill(``)
      this.game = new Array(9).fill(0)
      const pTypes = [{ num: 1, disp: `X` }, { num: 2, disp: `O` }]
      const rTypes = [[0, 1], [1, 0]]
      const cTypes = rTypes[Math.round(Math.random())]
      this.types = [pTypes[cTypes[0]], pTypes[cTypes[1]]]
      if(this.types[0].num === 1) {
        this.userTurn()
      }
    },
    userTurn() {
      this.blockUserInput = false
    },
    userInput(i) {
      if(!this.blockUserInput && this.game[i] === 0) {
        this.fillCell(i, this.types[0])
        this.blockUserInput = true
      }
    },
    fillCell(i, type) {
      this.$set(this.gameDisp, i, type.disp)
      this.$set(this.game, i, type.num)
    }
  },
  created() {
    this.newGame()
  },
  mounted() {
    this.$nextTick(() => {
      // The whole view is rendered, so the DOM can be accessed safely
      this.maintainAspectRatio()
      window.addEventListener("resize", () => {
        this.maintainAspectRatio()
      })
    })
  }
}
</script>

<style lang="sass">
// Theme
$primary-color: #FFEB3B
$secondary-color: #273849

#app
	font-family: 'Avenir', Helvetica, Arial, sans-serif
	-webkit-font-smoothing: antialiased
	-moz-osx-font-smoothing: grayscale
	text-align: center
	color: $secondary-color
	background-color: $primary-color
	overflow: hidden

.cell
	width: (1 / 3) * 100%
	height: (1 / 3) * 100%
	color: $secondary-color

.unselectable-text
  -webkit-user-select: none /* Safari */        
  -moz-user-select: none /* Firefox */
  -ms-user-select: none /* IE10+/Edge */
  user-select: none /* Standard */
</style>
