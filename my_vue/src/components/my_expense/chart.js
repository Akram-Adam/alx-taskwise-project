import { Chart, registerables } from 'chart.js';

// تسجيل جميع الإضافات
Chart.register(...registerables);

// دالة لإنشاء مخطط عام
export function createChart(ctx, type, data, options) {
  return new Chart(ctx, {
    type: type,
    data: data,
    options: options || {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
