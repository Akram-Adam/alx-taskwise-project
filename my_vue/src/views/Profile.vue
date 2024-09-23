<template>
    <div class="user-profile">
      <div class="profile-header">
        <img :src="user.profilePicture" alt="Profile Picture" class="profile-picture" />
        <div class="user-info">
          <h2>{{ user.username }}</h2>
          <p>{{ user.email }}</p>
        </div>
        <button @click="editProfile" class="edit-button">Edit Profile</button>
      </div>
      <div class="profile-details">
        <div class="detail-item">
          <h3>full Name</h3>
          <p>{{ user.first_name }} {{ user.last_name }}</p>
        </div>
        <div class="detail-item">
          <h3>Gender</h3>
          <p>{{ user.gender }}</p>
        </div>
        <div class="detail-item">
          <h3>Birthdate</h3>
          <p>{{ user.birthdate }}</p>
        </div>
        <div class="detail-item">
          <h3>Membership</h3>
          <p>{{ user.membership }}</p>
        </div>

      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserProfile',
    data() {
      return {
        user: {
          profilePicture: 'https://via.placeholder.com/150',
          username : 'john_doe',
          first_name : 'John',
          last_name : 'Doe',
          email: 'john.doe@example.com',
          phone: '+1234567890',
          address: '123 Main St, City, Country',
          membership: 'Premium',
          gender : 'male',
          birthdate : '20-04-2004'

          
        },
      };
    },
    methods: {
      editProfile() {
      
        this.$router.push('/edit-profile');
      },
    },
  };
  </script>
  
  <style scoped>
  .user-profile {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .profile-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .profile-picture {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .user-info {
    flex: 1;
    margin-left: 1.5rem;
  }
  
  .user-info h2 {
    margin: 0;
    font-size: 2rem;
    color: #333333;
  }
  
  .user-info p {
    margin: 0.5rem 0 0;
    color: #777777;
  }
  
  .edit-button {
    padding: 0.5rem 1rem;
    background-color: #2c3e50;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }
  
  .edit-button:hover {
    background-color: #2980b9;
  }
  
  .profile-details {
    margin-top: 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }
  
  .detail-item {
    background-color: #f9f9f9;
    padding: 1rem;
    border-radius: 8px;
  }
  
  .detail-item h3 {
    margin-bottom: 0.5rem;
    color: #555555;
  }
  
  .detail-item p {
    margin: 0;
    color: #333333;
  }
  </style>
  