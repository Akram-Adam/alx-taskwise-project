<template>
    <div>
      <canvas id="pie-chart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from 'chart.js';
  
  export default {
    name: 'PieChart',
    props: ['data'],
    mounted() {
      new Chart(document.getElementById('pie-chart'), {
        type: 'pie',
        data: this.data,
        options: {
          responsive: true,
        },
      });
    },
  };
  </script>
  
  <style scoped>
  canvas {
    max-width: 100%;
    max-height: 400px;
  }
  </style>
  