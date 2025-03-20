import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue"; // Vérifiez que ce fichier existe

const routes = [
  { path: "/", component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;