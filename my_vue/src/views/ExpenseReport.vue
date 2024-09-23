<template>
    <div class="expense-report-container">
      <h1 class="title">Expense Report</h1>
      
      <!-- Expense Input Section -->
      <div class="expense-input">
        <h2>Add Expense</h2>
        <input v-model="newExpense" placeholder="Enter amount" type="number" />
        <input v-model="expenseDate" placeholder="Select date" type="date" />
        <button @click="addExpense">Add Expense</button>
      </div>
  
      <!-- Chart Section -->
      <div class="charts-section">
        <h2>Weekly Overview</h2>
        <BarChart :data="weeklyData" />
        
        <h2>Monthly Overview</h2>
        <LineChart :data="monthlyData" />
  
        <h2>Yearly Overview</h2>
        <PieChart :data="yearlyData" />
      </div>
  
      <!-- Statistics Section -->
      <div class="statistics-section">
        <h2>Expense Statistics</h2>
        <p>Total this week: {{ totalWeekly }}</p>
        <p>Total this month: {{ totalMonthly }}</p>
        <p>Total this year: {{ totalYearly }}</p>
        <p>Largest Expense: {{ largestExpense }}</p>
      </div>
  
      <!-- Savings Goals -->
      <div class="savings-goals-section">
        <h2>Set Savings Goals</h2>
        <input v-model="savingsGoal" placeholder="Monthly savings goal" type="number" />
        <button @click="setSavingsGoal">Set Goal</button>
        <p>Your current savings goal: {{ currentSavingsGoal }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import BarChart from '../components/my_expense/BarChart.vue';
  import LineChart from '../components/my_expense/LineChart.vue';
  import PieChart from '../components/my_expense/PieChart.vue';
  import { Chart, registerables } from 'chart.js';
  
  Chart.register(...registerables);
  
  export default {
    name: 'ExpenseReport',
    components: {
      BarChart,
      LineChart,
      PieChart,
    },
    data() {
      return {
        newExpense: 0,
        expenseDate: '',
        expenses: [],
        weeklyData: [],
        monthlyData: [],
        yearlyData: [],
        savingsGoal: 0,
        currentSavingsGoal: 0,
      };
    },
    methods: {
      addExpense() {
        if (this.newExpense > 0 && this.expenseDate) {
          this.expenses.push({ amount: this.newExpense, date: this.expenseDate });
          this.updateCharts();
          this.newExpense = 0;  // إعادة تعيين بعد الإدخال
          this.expenseDate = '';
        }
      },
      calculateTotal(period) {
        let total = 0;
        const now = new Date();
        this.expenses.forEach(expense => {
          const expenseDate = new Date(expense.date);
          if (period === 'weekly') {
            const oneWeekAgo = new Date(now.setDate(now.getDate() - 7));
            if (expenseDate >= oneWeekAgo) {
              total += expense.amount;
            }
          } else if (period === 'monthly') {
            const oneMonthAgo = new Date(now.setMonth(now.getMonth() - 1));
            if (expenseDate >= oneMonthAgo) {
              total += expense.amount;
            }
          } else if (period === 'yearly') {
            const oneYearAgo = new Date(now.setFullYear(now.getFullYear() - 1));
            if (expenseDate >= oneYearAgo) {
              total += expense.amount;
            }
          }
        });
        return total;
      },
      getWeekNumber(date) {
        const firstDayOfYear = new Date(date.getFullYear(), 0, 1);
        const pastDaysOfYear = (date - firstDayOfYear) / 86400000;
        return Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7);
      },
      updateCharts() {
        this.weeklyData = this.calculateTotal('weekly');
        this.monthlyData = this.calculateTotal('monthly');
        this.yearlyData = this.calculateTotal('yearly');
      },
      setSavingsGoal() {
        this.currentSavingsGoal = this.savingsGoal;
      },
    },
    computed: {
      totalWeekly() {
        return this.calculateTotal('weekly');
      },
      totalMonthly() {
        return this.calculateTotal('monthly');
      },
      totalYearly() {
        return this.calculateTotal('yearly');
      },
      largestExpense() {
        return Math.max(...this.expenses.map(exp => exp.amount));
      },
    },
  };
  </script>
  
  
  <style lang="scss" scoped>
 .expense-report-container {
  padding: 2rem;
  text-align: center;
  background-color: #f5f7fa;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-width: 900px;
  margin: 0 auto;

  .title {
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 2rem;
    font-weight: bold;
  }

  .expense-input {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    
    h2 {
      font-size: 1.8rem;
      color: #34495e;
      margin-bottom: 1rem;
    }

    input {
      width: calc(50% - 1rem);
      margin: 0.5rem;
      padding: 0.75rem;
      font-size: 1.1rem;
      border: 1px solid #dce1e7;
      border-radius: 5px;
      outline: none;
      transition: border-color 0.3s ease;
      &:focus {
        border-color: #0b7dda;
      }
    }

    button {
      padding: 0.75rem 1.5rem;
      background-color: #3498db;
      color: white;
      border-radius: 8px;
      font-size: 1.1rem;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;
      &:hover {
        background-color: #2c3e50;
      }
    }
  }

  .charts-section {
    margin-bottom: 2rem;

    h2 {
      font-size: 1.8rem;
      color: #34495e;
      margin-bottom: 1rem;
    }

    canvas {
      max-width: 100%;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
  }

  .statistics-section, .savings-goals-section {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    margin-top: 2rem;

    h2 {
      font-size: 1.75rem;
      color: #34495e;
      margin-bottom: 1rem;
    }

    p {
      font-size: 1.2rem;
      color: #7f8c8d;
      margin-bottom: 0.5rem;
      line-height: 1.6;
    }
  }

  .savings-goals-section {
    input {
      width: calc(50% - 1rem);
      margin: 0.5rem;
      padding: 0.75rem;
      font-size: 1.1rem;
      border: 1px solid #dce1e7;
      border-radius: 5px;
      outline: none;
      transition: border-color 0.3s ease;
      &:focus {
        border-color: #0b7dda;
      }
    }

    button {
      padding: 0.75rem 1.5rem;
      background-color: #27ae60;
      color: white;
      border-radius: 8px;
      font-size: 1.1rem;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;
      &:hover {
        background-color: #2c3e50;
      }
    }

    p {
      font-size: 1.2rem;
      color: #2c3e50;
      margin-top: 1rem;
      font-weight: bold;
    }
  }
}

  </style>
  