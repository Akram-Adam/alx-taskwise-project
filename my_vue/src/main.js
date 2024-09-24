import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // call router
import store from './store'; // call Vuex store

import Toast, { POSITION } from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const app = createApp(App);

const options = {
    position: POSITION.TOP_RIGHT, // يمكنك تغيير الوضع حسب رغبتك
  };
  
app.use(Toast, options);
app.use(router); // using router
app.use(store);  // use Vuex store
app.mount('#app');