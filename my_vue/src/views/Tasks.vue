<template>
    <div class="my-tasks">
      <h1>Task Manager</h1>
      <AddTask @add-task="addTask" />
      <TaskList :tasks="tasks" @delete-task="deleteTask" />
    </div>
  </template>
  
  <script>
  import AddTask from '../components/my_tasks/AddTask.vue';
  import TaskList from '../components/my_tasks/TaskList.vue';


  
  export default {
    name: 'UserTasks',
    components: {
      AddTask,
      TaskList
    },
    data() {
      return {
        tasks: []
      };
    },
    methods: {
      addTask(task) {
        this.tasks.push(task);
      },
      deleteTask(index) {
        this.tasks.splice(index, 1);
      }
    }
  };
  </script>
  
  <style scoped lang="scss">
  .my-tasks {
    max-width: 470px;
    margin: 0 auto;
    padding: 40px;
    background-color: #f4f6f9;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    text-align: center;
    color: #003366;
    font-size: 32px;
    margin-bottom: 30px;
  }
  
  input, select {
    width: 100%;
    padding: 12px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
    background-color: #fff;
    transition: border-color 0.3s ease;
  
    &:focus {
      border-color: #003366;
      outline: none;
    }
  }
  
  button {
    width: 100%;
    padding: 12px;
    background-color: #003366;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  
    &:hover {
      background-color: #002244;
    }
  
    &:disabled {
      background-color: #999;
      cursor: not-allowed;
    }
  }
  
  .task-list {
    margin-top: 30px;
  }
  
  .task-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 15px;
    padding: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background-color 0.3s ease;
  
    &:hover {
      background-color: #f0f4f8;
    }
  
    &.completed {
      background-color: #e0f7e0;
      text-decoration: line-through;
      color: gray;
    }
  }
  
  .task-item span {
    flex-grow: 1;
    margin-right: 10px;
  }
  
  .task-item button {
    margin-left: 10px;
    padding: 8px 12px;
    font-size: 14px;
    border-radius: 6px;
  
    &.edit-btn {
      background-color: #f0ad4e;
  
      &:hover {
        background-color: #ec971f;
      }
    }
  
    &.remove-btn {
      background-color: #d9534f;
  
      &:hover {
        background-color: #c9302c;
      }
    }
  }
  
  .add-task-container {
    margin-bottom: 30px;
  }
  </style>
  