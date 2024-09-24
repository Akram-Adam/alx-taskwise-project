<template>
  <div class="home-container">
    <div class="header">
        <div class="overlay"></div>
        <h1>Welcome to TaskWise</h1>
        <p>TaskWise helps you organize your tasks, track expenses, and manage your time efficiently.Use our dynamic charts to visualize your daily, weekly, and monthly expenses, and set savings goals to stay on top of your finances.</p>
        <a class="btn"><router-link to="/Auth">Go to Sign in Now!</router-link></a>
        <router-view />
    </div>

    <section class="info-section">
        <h2>Why Choose Taskwise?</h2>
        <p>Taskwise provides an innovative approach to managing both tasks and expenses. By simplifying complex processes, Taskwise ensures you stay on track with your goals while managing your finances effectively.</p>
        
        <div class="info-boxes">
            <div class="info-box">
                <h3>Easy to Use</h3>
                <p>Taskwise's intuitive interface makes it easy to manage your daily tasks and track your expenses, all in one place.</p>
            </div>
            <div class="info-box">
                <h3>Smart Analytics</h3>
                <p>Gain insights into your spending habits and receive recommendations on how to better manage your resources.</p>
            </div>
            <div class="info-box">
                <h3>Customizable</h3>
                <p>Tailor Taskwise to suit your needs, from personal task management to collaborating with coworkers on shared projects.</p>
            </div>
        </div>
    </section>
    

    <section class="features-section">
        <h2>Key Features</h2>
        <ul>
            <li>
                <strong>Domain Access Control</strong>
                <p>Customize your panels to suit your specific needs. Share panels with multiple users while ensuring the right access levels.</p>
            </li>
            <li>
                <strong>Task and Expense Manager</strong>
                <p>Track your tasks, manage expenses, and budget effectively.</p>
            </li>
            <li>
                <strong>Smart Performance Analysis</strong>
                <p>Receive insightful recommendations for better financial management based on spending patterns.</p>
            </li>
        </ul>
    </section>
    
<!-- Beta Version Section -->
<section class="beta-version-section">
    <h2>Beta Version</h2>
    <ul>
        <li>
            <strong>Core Functionality</strong>
            <p>Taskwise will start with a Beta version focusing on core features, ensuring stability with continuous updates.</p>
        </li>
        <li>
            <strong>Web App Launch</strong>
            <p>Initially launching as a web app, with plans to scale across different platforms for broader accessibility.</p>
        </li>
    </ul>
</section>

<!-- Our Vision Section -->
<section class="vision-section">
    <h2>Our Vision</h2>
    <ul>
        <li>
            <strong>Empowerment & Growth</strong>
            <p>Our goal is to help you become the best version of yourself—whether individually or in teams.</p>
        </li>
        <li>
            <strong>Customization & Flexibility</strong>
            <p>Taskwise provides customizable and shareable panels, making it easier to manage both personal and professional goals.</p>
        </li>
    </ul>
</section>


<div class="expense-charts">
  <!-- عنوان واضح يعبر عن الغرض العام من القسم -->
  <h2>Your Expense Overview</h2>
  
  <!-- قسم عرض المصاريف الأسبوعية مع شرح موجز -->
  <div class="chart-section">
    <h3>Weekly Expenses</h3>
    <p>This chart shows your total expenses for the past week. You can track how your spending habits change over the days.</p>
    <BarChart :data="weeklyExpenseData" />
  </div>

  <!-- قسم عرض المصاريف الشهرية مع شرح موجز -->
  <div class="chart-section">
    <h3>Monthly Expenses</h3>
    <p>Here, you can see an overview of your monthly expenses. Use this to identify trends and adjust your budget accordingly.</p>
    <LineChart :data="monthlyExpenseData" />
  </div>

  <!-- قسم عرض المصاريف السنوية مع شرح موجز -->
  <div class="chart-section">
    <h3>Yearly Expenses</h3>
    <p>This pie chart represents your yearly expenses across different categories. It helps you visualize where most of your spending goes over the year.</p>
    <PieChart :data="yearlyExpenseData" />
  </div>
</div>
<FooTer></FooTer>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

  import BarChart from '../components/my_expense/BarChart.vue';
  import LineChart from '../components/my_expense/LineChart.vue';
  import PieChart from '../components/my_expense/PieChart.vue';
  import FooTer from './FooTer.vue';

export default {
  name: 'HomePage',

  data() {
    return {
      weeklyExpenseData: {
        labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        datasets: [{
          label: 'Expenses',
          data: [120, 90, 150, 80, 110, 130, 140],
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        }],
      },
      monthlyExpenseData: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [{
          label: 'Expenses',
          data: [400, 300, 500, 600],
          backgroundColor: 'rgba(153, 102, 255, 0.2)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1,
        }],
      },
      yearlyExpenseData: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
        datasets: [{
          label: 'Expenses',
          data: [1500, 1300, 1700, 1200, 1400, 1600, 1500 ,2000 ,3000 ,1770 ,500 , 1222],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 99, 132, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(255, 99, 132, 1)',
          ],
          borderWidth: 1,
        }],
      },
    };
  },
  components: {
    BarChart,
    LineChart,
    PieChart,
    FooTer
  },
};


// إضافة تأثير تمرير للظهور للأقسام
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionPosition = section.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        if (sectionPosition < screenPosition) {
            section.classList.add('section-visible');
        }
    });
});
</script>

<style scoped>
 @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

  .header {
    position: relative;
    height: 100vh;
    color: white;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: #000;
    overflow: hidden;
}

.header .overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

.header h1 {
    z-index: 2;
    font-size: 3rem;
}

.header p {
    z-index: 2;
    font-size: 1.5rem;
    margin-top: 10px;
}

.header .btn {
    z-index: 2;
    padding: 15px 30px;
    background-color: #ff6b6b;

    text-decoration: none;
    border-radius: 5px;
    font-size: 1.2rem;
  /*  position: fixed;*/
    bottom: 20px;
   /* right: 20px;*/
}
.header  a {
  color: white;
}

section {
    padding: 50px;
    text-align: center;
}

.info-section {
    padding: 60px 20px;
    background: linear-gradient(to right, #ff6b6b, #f94d6a);
    color: #fff;
    text-align: center;
}

.info-section h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #fff;
    letter-spacing: 1px;
}

.info-section p {
    font-size: 1.2rem;
    margin-bottom: 30px;
    line-height: 1.8;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.9;
}

.info-section .info-boxes {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 40px;
}

.info-section .info-box {
    background-color: #fff;
    color: #333;
    padding: 20px;
    border-radius: 10px;
    width: 250px;
    margin: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.info-section .info-box:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.info-section .info-box h3 {
    font-size: 1.5rem;
    margin-bottom: 15px;
    color: #ff6b6b;
}

.info-section .info-box p {
    font-size: 1rem;
    line-height: 1.6;
    color: #555;
}

/* إضافة تأثير animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.info-section h2, .info-section p, .info-section .info-box {
    animation: fadeInUp 1s ease forwards;
}

.info-section .info-box:nth-child(1) {
    animation-delay: 0.2s;
}
.info-section .info-box:nth-child(2) {
    animation-delay: 0.4s;
}
.info-section .info-box:nth-child(3) {
    animation-delay: 0.6s;
}

/* تنسيق قائمة المميزات */
.features-section ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    list-style: none;
    padding: 0;
}

.features-section ul li {
    background-color: #fff;
    color: #333;
    margin: 15px;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    flex: 1 1 300px;
    max-width: 300px;
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: left;
    position: relative;
}

/* تأثير اللمسة الإبداعية - التحويم */
.features-section ul li:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* إضافة خط تحت عنوان كل ميزة */
.features-section ul li::before {
    content: "";
    position: absolute;
    bottom: 0;
    left: 20px;
    width: 50px;
    height: 3px;
    background-color: #ff6b6b;
}

/* تنسيق النص داخل المميزات */
.features-section ul li strong {
    font-size: 1.2rem;
    color: #ff6b6b;
}

.features-section ul li p {
    font-size: 1rem;
    margin-top: 10px;
}


/* تنسيق عام للأقسام Beta Version و Our Vision */
.beta-version-section, .vision-section {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 50px 0;
    background-color: #f9f9f9;
}

.beta-version-section ul, .vision-section ul {
    list-style: none;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.beta-version-section ul li, .vision-section ul li {
    background-color: #fff;
    color: #333;
    margin: 15px;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    flex: 1 1 300px;
    max-width: 300px;
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: left;
    position: relative;
}

/* تأثير التحويم */
.beta-version-section ul li:hover, .vision-section ul li:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* إضافة خط تحت العنوان في Beta Version و Our Vision */
.beta-version-section ul li::before, .vision-section ul li::before {
    content: "";
    position: absolute;
    bottom: 0;
    left: 20px;
    width: 50px;
    height: 3px;
    background-color: #ff6b6b;
}

/* تنسيق النصوص داخل العناصر */
.beta-version-section ul li strong, .vision-section ul li strong {
    font-size: 1.2rem;
    color: #ff6b6b;
}

.beta-version-section ul li p, .vision-section ul li p {
    font-size: 1rem;
    margin-top: 10px;
}

footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}

/* خلفية متحركة */
@keyframes backgroundMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.header {
    background: url('../assets/images/e3.jpg') no-repeat center center/cover;
    animation: backgroundMove 10s infinite linear;
}
/* تأثير الظهور التدريجي للنص في الـHeader */
.header h1, .header p {
    opacity: 0;
    transform: translateY(-20px);
    animation: fadeIn 1.5s forwards;
}

.header p {
    animation-delay: 0.5s;
}

@keyframes fadeIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* تأثير التمرير على الأقسام */
section {
    opacity: 0;
    transform: translateY(50px);
    transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}

.section-visible {
    opacity: 1;
    transform: translateY(0);
}

/* تحسينات زر hover */
.btn:hover {
    background-color: #333;
    transition: background-color 0.3s ease-in-out;
}



.features-section ul li:hover::before {
    transform: rotate(360deg);
}


  .expense-charts {
    margin-top: 3rem;

    h2 {
      font-size: 2rem;
      margin-bottom: 1.5rem;
    }
  }

  canvas {
    max-width: 100%;
    margin: 1rem 0;
  }


  .expense-charts {
    margin: 40px auto;
    max-width: 1200px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .expense-charts h2 {
    text-align: center;
    font-size: 32px;
    font-weight: 600;
    color: #333;
    margin-bottom: 30px;
  }

  .chart-section {
    margin-bottom: 40px;
  }

  .chart-section h3 {
    font-size: 24px;
    font-weight: 500;
    color: #444;
    margin-bottom: 10px;
  }

  .chart-section p {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
    line-height: 1.5;
  }

  .chart-section canvas {
    max-width: 100%;
    height: auto;
  }

  .chart-section:nth-child(odd) {
    background-color: #f1f1f1;
    padding: 20px;
    border-radius: 8px;
  }

  @media (max-width: 768px) {
    .expense-charts {
      padding: 10px;
    }

    .chart-section h3 {
      font-size: 20px;
    }

    .chart-section p {
      font-size: 14px;
    }
  }
</style>
