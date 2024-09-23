<template>
    <div>
      <canvas id="line-chart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from 'chart.js';
  
  export default {
    name: 'LineChart',
    props: ['data'],
    mounted() {
      new Chart(document.getElementById('line-chart'), {
        type: 'line',
        data: this.data,
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
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
  