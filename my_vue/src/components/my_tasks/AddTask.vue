<template>
    <div>
      <h2>Add Task</h2>
      <input v-model="taskName" placeholder="Task Name" />
      <input v-model="taskTime" type="number" placeholder="Time (minutes)" />
      <select v-model="taskCategory">
        <option value="">Select Category</option>
        <option value="Work">Work</option>
        <option value="Personal">Personal</option>
        <option value="Urgent">Urgent</option>
      </select>
      <button @click="addTask">Add Task</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        taskName: '',
        taskTime: '',
        taskCategory: '',
      };
    },
    methods: {
      addTask() {
        if (this.taskName && this.taskTime && this.taskCategory) {
          const newTask = {
            id: Date.now(),
            name: this.taskName,
            time: this.taskTime,
            category: this.taskCategory,
            completed: false,
          };
          this.$emit('task-added', newTask);
          this.taskName = '';
          this.taskTime = '';
          this.taskCategory = '';
        }
      },
    },
  };
  </script>
  
  <style scoped>

body {
  font-family: 'Montserrat', sans-serif;
  background-color: #f5f5f5;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

h2 {
  text-align: center;
  font-size: 24px;
  color: #003366;
  margin-bottom: 20px;
}
div {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}


input,
select {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s ease-in-out;
}

input:focus,
select:focus {
  border-color: #003366;
  outline: none;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  text-transform: uppercase;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

button:hover {
  background-color: #002244;
}

/* تلميح لإضافة مهام */
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
