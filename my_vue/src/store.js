import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      tasks: [],
    };
  },
  mutations: {
    addTask(state, task) {
      state.tasks.push(task);
    },
    completeTask(state, taskId) {
      const task = state.tasks.find(t => t.id === taskId);
      if (task) {
        task.completed = true;
      }
    },
    deleteTask(state, taskId) {
      state.tasks = state.tasks.filter(t => t.id !== taskId);
    },
  },
  actions: {
    addTask({ commit }, task) {
      commit('addTask', task);
    },
    completeTask({ commit }, taskId) {
      commit('completeTask', taskId);
    },
    deleteTask({ commit }, taskId) {
      commit('deleteTask', taskId);
    },
  },
  getters: {
    allTasks(state) {
      return state.tasks;
    },
    completedTasks(state) {
      return state.tasks.filter(t => t.completed);
    },
    incompleteTasks(state) {
      return state.tasks.filter(t => !t.completed);
    },
  },
});

export default store;
