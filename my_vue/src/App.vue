<template>
  <div id="app">
    <nav class="navbar">
      <div class="logo">TaskWise</div>        
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/profile">Profile</router-link></li>
        <li><router-link to="/tasks">Tasks</router-link></li>
        <li><router-link to="/expense-report">Expense</router-link></li>
        <li><router-link to="/auth">Registration</router-link></li>
        <li><router-link to="/about">About Us</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>



<script>
export default {
  data() {
  return {
    isMenuOpen: false,
  };
},
methods: {
  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen;
  },
},

};
</script>


<style lang="scss">
body { 
  font-family: "Inria Sans", sans-serif;
  font-weight: 400;
  font-style: normal;
}

$primary-color: #2c3e50;
$secondary-color: #3498db;
$text-color: #ecf0f1;

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem; 
  background-color: $primary-color;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  position: relative;

  .logo {
    font-size: 1.5rem; 
    font-weight: bold;
    color: $text-color;
    transition: color 0.3s ease;

    &:hover {
      color: $secondary-color;
    }
  }

  .nav-links {
    list-style: none;
    display: flex;
    gap: 2rem; 
    li {
      position: relative;

      a {
        color: $text-color;
        text-decoration: none;
        font-size: 1rem;
        padding: 0.5rem 0; 
        transition: color 0.3s ease;

        &:hover {
          color: $secondary-color;
        }

        &::after {
          content: '';
          position: absolute;
          width: 100%;
          height: 2px;
          background: $secondary-color;
          bottom: -4px;
          left: 0;
          transform: scaleX(0);
          transition: transform 0.3s ease;
        }

        &:hover::after {
          transform: scaleX(1);
        }
      }
    }
  }
}

// Media Queries for responsiveness
@media (max-width: 768px) {
  .navbar {
    padding: 0.5rem 1rem; 
    
    .logo {
      font-size: 1.2rem; 
    }

    .nav-links {
      gap: 1rem; 
      
      a {
        font-size: 0.9rem; 
        padding: 0.3rem 0; 
      }
    }
  }
}

@media (max-width: 480px) {
  .navbar {
    padding: 0.3rem 0.5rem; 
    
    .logo {
      font-size: 1rem; 
    }

    .nav-links {
      gap: 0.5rem; 

      a {
        font-size: 0.8rem; 
        padding: 0.2rem 0; 
      }
    }
  }
}
</style>
