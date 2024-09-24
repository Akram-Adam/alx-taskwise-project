<template>
  <div>
    <h2>Add Task</h2>
    
    <!-- Task Name -->
    <input v-model="taskName" placeholder="Task Name" />

    <!-- Task Description -->
    <textarea v-model="taskDescription" placeholder="Task Description"></textarea>

    <!-- Task Category (New Section) -->
    <select v-model="taskCategory">
      <option value="">Select Category</option>
      <option value="Work">Work</option>
      <option value="Personal">Personal</option>
      <option value="Urgent">Urgent</option>
    </select>

    <!-- Task Type Selector -->
    <select v-model="taskType">
      <option value="">Select Task Type</option>
      <option value="daily">Daily Task</option>
      <option value="timed">Timed Task</option>
    </select>

    <!-- Fields for Daily Task -->
    <div v-if="taskType === 'daily'">
      <h3>Daily Task</h3>
      <input v-model="taskHours" type="number" placeholder="Time (hours)" />
    </div>

    <!-- Fields for Timed Task -->
    <div v-if="taskType === 'timed'">
      <h3>Timed Task</h3>
      <label>Start Date</label>
      <input v-model="startDate" type="date" />
      
      <label>End Date</label>
      <input v-model="endDate" type="date" />
    </div>

    <button @click="addTask">Add Task</button>
  </div>
</template>

  
<script>
import { useToast } from 'vue-toastification';

export default {
  data() {
    return {
      taskName: '',
      taskDescription: '',
      taskType: '',
      taskCategory: '',  
      taskHours: '',
      startDate: new Date().toISOString().split('T')[0],
      endDate: '',
    };
  },
  setup() {
    const toast = useToast(); // استخدام useToast من vue-toastification
    return { toast };
  },
  methods: {
    addTask() {
      if (this.taskName && this.taskType && this.taskCategory) {  
        let newTask = {
          id: Date.now(),
          name: this.taskName,
          description: this.taskDescription,
          type: this.taskType,
          category: this.taskCategory,  
          completed: false,
        };

        if (this.taskType === 'daily') {
          newTask.hours = this.taskHours;
        } else if (this.taskType === 'timed') {
          newTask.startDate = this.startDate;
          newTask.endDate = this.endDate;
        }

        this.$emit('task-added', newTask);
        this.resetFields();

        // عرض رسالة تنبيه عند إضافة المهمة بنجاح
        this.toast.success('Task added successfully!');
      } else {
        this.toast.error('Please fill in all required fields.'); // تنبيه عند عدم تعبئة الحقول
      }
   
    },
    resetFields() {
      this.taskName = '';
      this.taskDescription = '';
      this.taskType = '';
      this.taskCategory = '';  
      this.taskHours = '';
      this.startDate = new Date().toISOString().split('T')[0];
      this.endDate = '';
    }
  }
};
</script>


<style scoped>
/* Add any additional styles here as needed */
div {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

h2 {
  text-align: center;
  font-size: 24px;
  color: #003366;
  margin-bottom: 20px;
}

textarea {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s ease-in-out;
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
</style>

