<template>
<section class="sponsors">
    <h2>Nuestros Sponsors</h2>
    <div class="sponsor">
        <img src="../../public/logo-ucema.png" alt="Sponsor 1">
       <p>Agradecemos a la Universidad del CEMA por el apoyo en este proyecto.</p>
    </div>

    <div class="sponsor">
      <img src="../../public/logo-meli.png" alt="Sponsor 1">
      <p>Y a Mercado Libre por patrocinar nuestra manera de ayudar al mundo.</p>
    </div>
  </section>

  
   
    <p>Si usted esta interesado en ser parte de nuestra organizacion, puede ponerse en contacto con nosotros a través de:</p>
    <ul>
      <li>Correo electrónico: <a href="mailto:info@donacionesenlinea.com">info@donacionesenlinea.com</a></li>
      <li>Teléfono: +1-123-456-7890</li>
    </ul>

</template>

<script>

export default {

  beforeRouteEnter(to, from, next) {
    document.title = 'Sponsors'; // Set your desired title
    next();
  },
}
</script>


<style>
.sponsors {
    background-color: #f4f4f4;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 20px;
  }
  
  .sponsors h2 {
    font-size: 24px;
  }
  
  .sponsor {
    margin-top: 20px;
  }
  
  .sponsor img {
    max-width: 100%;
  }
  
  .sponsor p {
    font-size: 16px;
  }

  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
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
  
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  
</style>