<template>
 <section clsss="fundaciones">
    <h3>Fundación Unicef</h3>
        <img src="../../public/logo-unicef.png" alt="UNICEF">
        <p>Se dedican a llevarle agua potable y comida a los pueblos de escasos recursos en África.</p>
        <a href="https://www.unicef.org/">Visitar pagina de UNICEF</a> <br>
        
        
    <h3>Fundación Caritas</h3>
        <img src="../../public/logo-caritas.png" alt="CARITAS">
        <p>Proporcionar ayuda a los sobrevivientes de desastres naturales, ayudar a las comunidades a prepararse para emergencias, incluida la capacitación en primeros auxilios y a cómo prevenir enfermedades.</p>
                <a href="https://www.caritas.org/">Visitar pagina de CARITAS</a> <br>
        
    <h3>Fundación Techo</h3>
        <img src="../../public/logo-techo.png" alt="UNICEF">
        <p>Construyen viviendas dignas en asientamientos marginales.</p>
        <a href="https://techo.org/">Visitar pagina de TECHO</a> <br>
        
    </section>

</template>

<script>

export default {

  beforeRouteEnter(to, from, next) {
    document.title = 'Nuestras Fundaciones'; // Set your desired title
    next();
  },
}

</script>


<style>
template {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
    color: #333;
}

header {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}

header h1 {
    margin: 0;
}


nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #fff;
}

section {
    padding: 20px;
    background-color: #fff;
    margin: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}


footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

</style>