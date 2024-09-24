import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/Home.vue';
import Profile from './views/Profile.vue';
import Tasks from './views/Tasks.vue';
import ExpenseReport from './views/ExpenseReport.vue';
import Auth from './views/Auth.vue';
import SignUp from './components/Authentication/SignUp.vue';
import ForgetPassword from './components/Authentication/ForgetPassword.vue';
import About from './views/About.vue';
import editProfile from './components/my_profile/edit-profile.vue';
const routes = [
  { path: '/', component: HomePage },
  { path: '/profile', component: Profile },
  { path: '/auth', component: Auth },
  { path: '/tasks', component: Tasks },
  { path: '/expense-report', component: ExpenseReport },
  { path: '/sign-up', component: SignUp },
  { path: '/forgot-password', component: ForgetPassword },
  { path: '/about', component: About},
  { path: '/edit-profile', component: editProfile},
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
