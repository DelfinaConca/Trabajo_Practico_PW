<template>
    <div id="header">
        <header>
        <nav>
            <ul>
               
                <li><router-link to="/" target="_blank">Home</router-link></li>
                <li><router-link to="/quienes-somos" target="_blank">Quiénes Somos</router-link></li>                
                <li><router-link to="/como-donar" target="_blank">Cómo Donar</router-link></li>
                <li><router-link to="/sponsors" target="_blank">Sponsors</router-link></li>
                <li><router-link to="/contacto" target="_blank">Contacto y Redes Sociales</router-link></li>
                <li><router-link to="/fundaciones" target="_blank">Nuestras Fundaciones</router-link></li>
               
            </ul>
        </nav>
    </header>
  </div>
</template>
<script>

export default {

}
</script>
<style>
header {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}
</style>