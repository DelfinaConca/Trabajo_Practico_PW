<template>
  <HeaderBar/>
  <router-view></router-view>
  <FooterBar/>
</template>

<script>
import FooterBar from './components/FooterBar.vue';
import HeaderBar from './components/HeaderBar.vue'

export default {
  name: 'App',
  components: {
    FooterBar,
    HeaderBar

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
