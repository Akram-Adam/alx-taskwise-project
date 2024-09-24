<template>
    <div class="edit-profile-container">
      <h2>Edit Profile</h2>
      <form @submit.prevent="saveProfile" class="edit-profile-form">
        
        <!-- Full Name Input -->
        <div class="form-group">
          <label for="fullName">Full Name</label>
          <input
            type="text"
            id="fullName"
            v-model="user.fullName"
            placeholder="Enter your full name"
            required
          />
        </div>
  
        <!-- Gender Selection -->
        <div class="form-group">
          <label for="gender">Gender</label>
          <select id="gender" v-model="user.gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
        </div>
  
        <!-- Birthdate Input -->
        <div class="form-group">
          <label for="birthdate">Birthdate</label>
          <input
            type="date"
            id="birthdate"
            v-model="user.birthdate"
            required
          />
        </div>
  
        <!-- Profile Picture Upload -->
        <div class="form-group">
          <label for="profilePicture">Profile Picture</label>
          <input
            type="file"
            id="profilePicture"
            @change="previewProfilePicture"
            accept="image/*"
          />
          <div v-if="user.profilePicture" class="profile-picture-preview">
            <img :src="user.profilePicture" alt="Profile Picture Preview" />
          </div>
        </div>
  
        <!-- Save Button -->
        <button type="submit" class="save-button">Save Changes</button>
      </form>
    </div>
  </template>
  
  <script>
  import Swal from 'sweetalert2'
  export default {
    name: "EditProfile",
    data() {
      return {
        user: {
          fullName: "John Doe",
          gender: "male",
          birthdate: "2004-04-20",
          profilePicture: "https://via.placeholder.com/150",
        },
      };
    },
    methods: {
      
      previewProfilePicture(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = (e) => {
            this.user.profilePicture = e.target.result;
          };
          reader.readAsDataURL(file);
        }
      },
      // data update
      saveProfile() {
        console.log("Profile updated", this.user);
        this.successful("Profile updated");

        this.$router.push("/profile"); //
      },
      successful(message) {
// Use SweetAlert to show the success message
      Swal.fire({
        icon: 'success',
        title: 'Success',
        text: message,
        timer: 2000,  // The message is closed after 2 seconds
        showConfirmButton: false
      });
    },
    },
  };
  </script>
  
  <style scoped lang="scss">
  .edit-profile-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
  
    h2 {
      font-size: 2rem;
      margin-bottom: 1.5rem;
      color: #2c3e50;
    }
  
    .edit-profile-form {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
  
      .form-group {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
  
        label {
          font-size: 1rem;
          margin-bottom: 0.5rem;
          color: #2c3e50;
        }
  
        input,
        select {
          width: 100%;
          padding: 0.5rem;
          border: 1px solid #ccc;
          border-radius: 5px;
          font-size: 1rem;
        }
  
        input[type="file"] {
          padding: 0;
        }
  
        .profile-picture-preview {
          margin-top: 1rem;
          img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
          }
        }
      }
  
      .save-button {
        padding: 0.75rem 1.5rem;
        background-color: #3498db;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2rem;
      }
  
      .save-button:hover {
        background-color: #2980b9;
      }
    }
  }
  </style>
  