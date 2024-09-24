<template>
  <li :class="{ completed: task.completed }">
    <span>{{ task.name }} ({{ task.time }} min) - {{ task.category }} - {{ task.type }}</span>
    <p>{{ task.description }}</p>
    <button @click="toggleStatus">{{ task.completed ? 'Mark Incomplete' : 'Mark Complete' }}</button>
    <button @click="editTask">Edit</button>
    <button @click="removeTask">Remove</button>
  </li>
</template>

<script>
export default {
  props: ['task'],
  methods: {
    toggleStatus() {
      this.$emit('toggle-status', this.task.id);
    },
    removeTask() {
      this.$emit('remove-task', this.task.id);
    },
    editTask() {
      const newTime = prompt('Enter new time (minutes):', this.task.time);
      const newCategory = prompt('Enter new category:', this.task.category);
      const newDescription = prompt('Enter new description:', this.task.description);
      const newType = prompt('Enter new task type (daily/timed):', this.task.type);
      
      if (newTime !== null && newCategory !== null && newDescription !== null && newType !== null) {
        this.$emit('edit-task', {
          ...this.task,
          time: newTime,
          category: newCategory,
          description: newDescription,
          type: newType
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
li {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 15px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  transition: background-color 0.3s ease-in-out;
  margin-bottom: 10px;
  list-style-type: none;

  &.completed {
    background-color: #e0f7e0;
    text-decoration: line-through;
    color: gray;
  }

  span {
    font-size: 16px;
    font-weight: 500;
  }

  p {
    font-size: 14px;
    color: #666;
    margin: 5px 0 15px;
  }

  button {
    background-color: #003366;
    color: white;
    border: none;
    padding: 8px 12px;
    margin-top: 10px;
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
