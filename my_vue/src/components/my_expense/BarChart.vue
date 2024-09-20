<template>
    <div>
      <canvas id="bar-chart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from 'chart.js';
  
  
  export default {
    name: 'BarChart',
    props: ['data'],
    mounted() {
      new Chart(document.getElementById('bar-chart'), {
        type: 'bar',
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
  