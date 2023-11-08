<template>
  <div>
    <header>
      <h1>Doná, se parte del cambio</h1>
      <p style="font-weight: bold;">Contribui con tu donacion aca!</p>
    </header>

    <section>
      <form @submit.prevent="realizarDonacion">
        <fieldset>
          <legend> Datos personales</legend>
          <label for="nombre">Nombre:</label>
          <input type="text" v-model="nombre" required />

          <br />
          <label for="apellido">Apellido:</label>
          <input type="text" v-model="apellido" required />

          <br />
          <label for="tel">Telefono:</label>
          <input type="tel" v-model="tel" required />

          <br />
          <label for="mail">Mail:</label>
          <input type="email" v-model="mail" required />

          <br /><br />
        </fieldset>
        <div>
          <fieldset>
            <legend>Tipo de donación</legend>
            <input type="radio" id="dinero" value="dinero" v-model="tipoDonacion" />
            <label for="dinero">Dinero</label>

            <input type="radio" id="cryptos" value="cryptos" v-model="tipoDonacion" />
            <label for="cryptos">Cryptos</label>

            <div v-if="tipoDonacion === 'dinero'">
              <p>Selecciona una opción:</p>
              <input type="radio" value="dolares" v-model="opcionDinero" /> Dólares
              <input type="radio" value="pesos" v-model="opcionDinero" /> Pesos Argentinos
            </div>

            <div v-if="tipoDonacion === 'cryptos'">
              <p>Precio de Bitcoin (USD): ${{ bitcoinPrice }}</p>
              <p>Selecciona una criptomoneda:</p>
              <input type="radio" value="bitcoin" v-model="opcionCryptos" /> Bitcoin
              <input type="radio" value="ethereum" v-model="opcionCryptos" /> Ethereum
              <input type="radio" value="cardano" v-model="opcionCryptos" /> Cardano
              <input type="radio" value="tether" v-model="opcionCryptos" /> Tether
              <input type="radio" value="dogecoin" v-model="opcionCryptos" /> Dogecoin
            </div>

            <div>
              <br />
              <label for="tipopago">Tipo Pago:</label>
              <input type="radio" id="debito" value="debito" v-model="tipoPago" /> Debito
              <input type="radio" id="credito" value="credito" v-model="tipoPago" /> Credito
            </div>

            <br />
            <label for="tarjeta">Tarjeta:</label>
            <select v-model="tarjeta">
              <option value="amex">Amex</option>
              <option value="visa">Visa</option>
              <option value="master">Master</option>
            </select>

            <br />
            <label for="comentario">Comentarios:</label>
            <textarea v-model="comentario" cols="15" rows="10" maxlength="255"></textarea>
            <br />
          </fieldset>
        </div>
        <fieldset>
          <legend> Fundación a la que quiere donar: </legend>
          <label for="fundacion">Selecciona una fundación:</label>
          <select v-model="fundacion">
            <option value="Fundacion Unicef">Fundacion Unicef</option>
            <option value="Fundacion Caritas">Fundacion Caritas</option>
            <option value="Fundacion Techo">Fundacion Techo</option>
          </select>
        </fieldset>
        <fieldset>
          <legend> Completa aca la cantidad</legend>
          <label for="cantidad">Cantidad:</label>
          <input type="number" v-model="cantidad" min="0" step="0.01" required />
        </fieldset>
        <input type="submit" value="Realizar donacion" />
      </form>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nombre: '',
      apellido: '',
      tel: '',
      mail: '',
      tipoDonacion: '',
      opcionDinero: '',
      opcionCryptos: '',
      tipoPago: '',
      tarjeta: 'visa',
      comentario: '',
      fundacion: 'Fundacion Unicef',
      cantidad: '',
      bitcoinPrice: '', // To be fetched dynamically
    };
  },
  methods: {
    // Handle form submission
    realizarDonacion() {
      console.log(this.nombre, this.apellido, this.tel, this.mail, this.tipoDonacion, this.opcionDinero, this.opcionCryptos, this.tipoPago, this.tarjeta, this.comentario, this.fundacion, this.cantidad);
    },
  },
  mounted() {
    // Fetch Bitcoin price here and update this.bitcoinPrice
    const apiUrl = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd';
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
        this.bitcoinPrice = data.bitcoin.usd;
      })
      .catch((error) => {
        console.error('Error al obtener datos de la API:', error);
        this.bitcoinPrice = 'Error al cargar datos de criptomonedas';
      });
  },
};
</script>

<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

header {
    background-color: #007BFF;
    color: #fff;
    text-align: center;
    padding: 20px;
}

h1 {
    font-size: 36px;
}

section {
    background-color: #fff;
    padding: 20px;
    margin: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

fieldset {
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
input[type="email"],
textarea,
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
}

input[type="checkbox"] {
    margin-right: 5px;
}

input[type="submit"] {
    background-color: #007BFF;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}
</style>