import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.use(VueRouter);

import VerArchivos from './views/VerArchivos.vue';
import Home from './views/Home.vue';

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/verarchivos', component: VerArchivos},
    {path: '/', component: Home}
  ]
});

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
