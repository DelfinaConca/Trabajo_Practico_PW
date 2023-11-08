<template>
    <section class="como-donar">
    <h2>Cómo Donar</h2>
    <p>Donar es fácil. Siga los siguientes pasos:</p>
    <br><br>

    <ol>
      <li>Presione en el formulario que se encuentra en la pagina principal o entre desde <router-link to="/formulario" target="_blank">aqui</router-link>.</li>
      <br>
      <li>Rellene el formulario con su información personal.</li>
      <br>
      <li>Seleccione el monto que desea donar y elija un método de pago (tarjeta de crédito, PayPal, Cripto, etc).</li>
      <br>
      <li>Haga clic en el botón "Donar" para finalizar la transacción.</li>
    </ol>

    <p>Gracias por su generosidad y apoyo.</p>
   
  </section>

</template>


<script>

export default {

}
</script>


<style>

.como-donar {
    background-color: #f4f4f4;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 20px;
  }
  
  .como-donar h2 {
    font-size: 24px;
  }
  
  .como-donar p {
    font-size: 16px;
  }
  
  .como-donar ol {
    list-style-type: decimal;
    margin-left: 20px;
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

nav ol {
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
  
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

</style>