<template>
  <div class="auth-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="input-group">
        <label for="email">Email</label>
        <input type="email" v-model="email" required placeholder="Enter your email" />
      </div>
      <div class="input-group">
        <label for="password">Password</label>
        <input type="password" v-model="password" required placeholder="Enter your password" />
      </div>
      <button type="submit" class="btn">Login</button>
      <p>
        Don't have an account? 
        <router-link to="/sign-up">Create an account</router-link>
      </p>
      <p>
        <router-link to="/forgot-password">Did you forget your password?</router-link>
      </p>
    </form>
    <router-view />
  </div>
</template>

<script>

export default {
  name : 'AuthPage',

  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      // Logic for login
      console.log('Login:', this.email, this.password);
    },
  },
};
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
h2 {
  text-align: center;
}
.input-group {
  margin-bottom: 15px;
}
.input-group label {
  display: block;
  margin-bottom: 5px;
}
.input-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.btn {
  width: 100%;
  padding: 10px;
  background-color:  #2c3e50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.btn:hover {
  background-color:  #0b7dda;
}
</style>
