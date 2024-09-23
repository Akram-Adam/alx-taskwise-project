<template>
    <div class="auth-container">
      <h2>Forgot Password</h2>
      <form @submit.prevent="submitEmail">
        <div class="input-group">
          <label for="email">Enter your email</label>
          <input type="email" v-model="email" required placeholder="Enter your email" />
        </div>
        <button type="submit" class="btn">Submit</button>
      </form>
      <p><router-link to="/auth">Back</router-link></p>
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name : 'ForgetPassword',
    data() {
      return {
        email: '',
      };
    },
    methods: {
      submitEmail() {
        // Logic for password reset email
        console.log('Password reset request sent to:', this.email);
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
    background-color:   #0b7dda;
  }
  </style>
  