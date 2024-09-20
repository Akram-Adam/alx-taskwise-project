import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // call router
import store from './store'; // call Vuex store


const app = createApp(App);

app.use(router); // using router
app.use(store);  // use Vuex store
app.mount('#app');