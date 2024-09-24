<template>
  <div>
    <h2>Task List</h2>
    <!-- Category filter -->
    <select v-model="filterCategory">
      <option value="">All Categories</option>
      <option v-for="category in categories" :key="category">{{ category }}</option>
    </select>
    
    <!-- Type filter -->
    <select v-model="filterType">
      <option value="">All Types</option>
      <option v-for="type in taskTypes" :key="type">{{ type }}</option>
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
    TaskItem,
  },
  data() {
    return {
      tasks: [],
      filterCategory: '', // Filter for category ('Work', 'Personal', etc.)
      filterType: '',     // Filter for type ('daily', 'timed')
      categories: ['Work', 'Personal', 'Urgent'], // Main categories
      taskTypes: ['daily', 'timed'], // Task types within each category
    };
  },
  computed: {
    filteredTasks() {
      return this.tasks.filter(task => {
        const matchesCategory = this.filterCategory ? task.category === this.filterCategory : true;
        const matchesType = this.filterType ? task.type === this.filterType : true;
        return matchesCategory && matchesType;
      });
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
        if (task.type === 'daily') {
          if (!task.completed && task.time <= 1) {
            alert(`Task "${task.name}" is due in ${task.time} hour(s)!`);
          }
        } else if (task.type === 'timed') {
          const now = new Date();
          const endDate = new Date(task.endDate);
          if (!task.completed && endDate <= now) {
            alert(`Task "${task.name}" is due today!`);
          }
        }
      });
    },
  },
  mounted() {
    setInterval(this.checkDeadlines, 60000); // the check on time evray minutes
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
