<template>
    <div>
      <h2>Task List</h2>
      <select v-model="filterCategory">
        <option value="">All Categories</option>
        <option v-for="category in categories" :key="category">{{ category }}</option>
      </select>
      <ul>
        <TaskItem
          v-for="task in filteredTasks"
          :key="task.id"
          :task="task"
          @remove-task="removeTask"
          @edit-task="editTask"
          @toggle-status="toggleStatus"
        />
      </ul>
    </div>
  </template>
  
  <script>
  import TaskItem from './TaskItem.vue';

  
  export default {
    components: {
   TaskItem
  },
    data() {
      return {
        tasks: [],
        filterCategory: '',
        categories: ['Work', 'Personal', 'Urgent'],
      };
    },
    computed: {
      filteredTasks() {
        if (this.filterCategory) {
          return this.tasks.filter(task => task.category === this.filterCategory);
        }
        return this.tasks;
      },
    },
    methods: {
      addTask(task) {
        this.tasks.push(task);
      },
      removeTask(taskId) {
        this.tasks = this.tasks.filter(task => task.id !== taskId);
      },
      editTask(updatedTask) {
        const index = this.tasks.findIndex(task => task.id === updatedTask.id);
        if (index !== -1) {
          this.$set(this.tasks, index, updatedTask);
        }
      },
      toggleStatus(taskId) {
        const task = this.tasks.find(task => task.id === taskId);
        if (task) {
          task.completed = !task.completed;
        }
      },
      checkDeadlines() {
      this.tasks.forEach(task => {
        if (!task.completed && task.time <= 5) {
          alert(`Task "${task.name}" is due in ${task.time} minutes!`);
        }
      });
    },
    },
    mounted() {
    setInterval(this.checkDeadlines, 60000); // التحقق من المواعيد النهائية كل دقيقة
  },
  };
  </script>
  
  <style scoped lang="scss">
div {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f6f9;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #003366;
  font-size: 24px;
  margin-bottom: 20px;
}

select {
  display: block;
  width: 100%;
  padding: 10px;
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

ul {
  padding: 0;
  list-style-type: none;
}

li {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s;

  &:hover {
    background-color: #f0f4f8;
  }

  &.completed {
    background-color: #e0f7e0;
    text-decoration: line-through;
    color: gray;
  }

  button {
    background-color: #003366;
    color: white;
    border: none;
    padding: 8px 12px;
    margin-left: 10px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.2s;

    &:hover {
      background-color: #002244;
    }

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
}
</style>
