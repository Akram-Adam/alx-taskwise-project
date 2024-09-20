<template>
    <footer class="footer">
      <div class="footer-content">
        <!-- Developers Names -->
        <div class="developers">
          <p>&copy; 2024 TaskWise. All rights reserved. Developed By  <a href="https://www.linkedin.com/in/akram-adam-16955422b" target="_blank">Akram Adam </a>| <a href="https://www.linkedin.com/in/mahmoud-ahmed-bb3056248/" target="_blank">Mahmoud Ahmed</a></p>
        </div>
      </div>
    </footer>

  </template>
  
  <script>
  export default {
    name: "SiteFooter",
  };
  </script>
  <style lang="scss" scoped>
  .footer {
    background-color: #364250;
    color: white;
    padding: 1.5rem; 
    display: flex;
    justify-content: center; 
    align-items: center;
    font-family: 'Arial', sans-serif;
  
    .footer-content {
      display: flex;
      flex-direction: column; 
      align-items: center;
      width: 100%;
      
      .developers {
        text-align: center; 
        p {
          margin: 0;
          font-size: 0.9rem; 
        }
      }
    }
  
    a {
      color: #00aced; 
      text-decoration: none;
      font-weight: bold;
      transition: color 0.3s ease;
  
      &:hover {
        color: #1DA1F2; 
        text-decoration: underline;
      }
    }
  }
  </style>
  