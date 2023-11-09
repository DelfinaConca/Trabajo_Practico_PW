<template>
<h1>¡Donación Realizada!</h1>
    <p>Gracias por tu generosa contribución. Tu apoyo hace una diferencia.</p>
</template>

<script>
export default {

  beforeRouteEnter(to, from, next) {
    document.title = 'Gracias por su aporte'; // Set your desired title
    next();
  },
}
</script>

<style>
</style>