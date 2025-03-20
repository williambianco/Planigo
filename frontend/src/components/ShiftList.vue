<template>
  <div>
    <h3>Liste des shifts</h3>
    <ul>
      <li v-for="(shift, index) in shifts" :key="index">
        {{ shift }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ShiftList",
  data() {
    return {
      shifts: ["Matin - Employé 1", "Après-midi - Employé 2", "Soir - Employé 3"]
    };
  }
};
</script>