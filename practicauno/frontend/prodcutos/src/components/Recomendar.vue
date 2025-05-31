<template>
  <div class="container mt-5">
    <div class="card shadow">
      <div class="card-body">
        <h3 class="card-title text-center mb-4">Recomendación de Productos</h3>
        <form @submit.prevent="obtenerRecomendacion">
          <div class="mb-3">
            <label for="interes" class="form-label">Interés</label>
            <select v-model="interes" class="form-select" id="interes">
              <option value="tecnología">Tecnología</option>
              <option value="hogar">Hogar</option>
              <option value="deporte">Deporte</option>
            </select>
          </div>

          <div class="mb-3">
            <label for="presupuesto" class="form-label">Presupuesto</label>
            <select v-model="presupuesto" class="form-select" id="presupuesto">
              <option value="bajo">Bajo</option>
              <option value="medio">Medio</option>
              <option value="alto">Alto</option>
            </select>
          </div>

          <button type="submit" class="btn btn-primary w-100">Obtener recomendación</button>
        </form>

        <div v-if="recomendacion" class="mt-4">
          <label for="resultado" class="form-label">Producto recomendado:</label>
          <input type="text" class="form-control" id="resultado" :value="recomendacion" readonly />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      interes: 'tecnología',
      presupuesto: 'medio',
      recomendacion: ''
    };
  },
  methods: {
    async obtenerRecomendacion() {
      try {
        const res = await fetch('http://localhost:5000/recomendar', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            interes: this.interes,
            presupuesto: this.presupuesto
          })
        });

        const data = await res.json();
        this.recomendacion = data.recomendacion;
      } catch (error) {
        console.error('Error al obtener recomendación:', error);
        this.recomendacion = 'No se pudo obtener recomendación.';
      }
    }
  }
};
</script>

<style scoped>
.card {
  max-width: 500px;
  margin: 0 auto;
  border-radius: 1rem;
}
</style>


  