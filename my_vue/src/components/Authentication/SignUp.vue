<template>
    <div class="auth-container">
      <h2>Create Account</h2>
      <form @submit.prevent="signUp">
        <div class="input-group">
          <label for="fullName">Full Name</label>
          <input type="text" v-model="fullName" required placeholder="Enter your full name" />
        </div>
        <div class="input-group">
          <label for="username">Username</label>
          <input type="text" v-model="username" required placeholder="Choose a username" />
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <input type="password" v-model="password" required placeholder="Enter your password" />
        </div>
        <div class="input-group">
          <label for="confirmPassword">Confirm Password</label>
          <input type="password" v-model="confirmPassword" required placeholder="Confirm your password" />
        </div>
        <div class="input-group">
          <label for="gender">Gender</label>
          <select v-model="gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="input-group">
          <label for="birthDate">Date of Birth</label>
          <input type="date" v-model="birthDate" required />
        </div>
        <button type="submit" class="btn">Create Account</button>
      </form>
      <p><router-link to="/auth">You already have an account ?!</router-link></p>
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name : 'sign-up',

    data() {
      return {
        fullName: '',
        username: '',
        password: '',
        confirmPassword: '',
        gender: '',
        birthDate: '',
      };
    },
    methods: {
      signUp() {
        if (this.password !== this.confirmPassword) {
          alert("Passwords don't match!");
          return;
        }
        // Logic for signing up
        console.log('Sign Up:', this.fullName, this.username, this.gender, this.birthDate);
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
  .input-group input,
  .input-group select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .btn {
    width: 100%;
    padding: 10px;
    background-color:#2c3e50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  .btn:hover {
    background-color: #0b7dda;
  }
  </style>
  