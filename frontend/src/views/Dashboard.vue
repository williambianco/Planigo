<template>
  <div>
    <h1>Planigo - Gestion des Plannings</h1>
    <button @click="assignShifts">Affecter les employés</button>
    <ShiftList />
  </div>
</template>

<script>
import ShiftList from "../components/ShiftList.vue";
import axios from "axios";

export default {
  components: { ShiftList },
  methods: {
    async assignShifts() {
      await axios.post("http://localhost:5000/assign_shifts");
    }
  }
};
</script>
