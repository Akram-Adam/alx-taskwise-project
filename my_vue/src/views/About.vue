<template>
  <div class="about-us-container">
    <!-- About Header with animated background and text effect -->
    <div class="about-header">
      <h1>{{ aboutTitle }}</h1>
      <p>{{ aboutIntro }}</p>
    </div>

    <!-- Our Goals Section -->
    <div class="about-section">
      <div class="about-content" v-for="goal in goals" :key="goal.title">
        <h2>{{ goal.title }}</h2>
        <p>{{ goal.description }}</p>
      </div>
    </div>

    <!-- Vision Section with interactive hover effect -->
    <div class="about-vision">
      <h2>{{ visionTitle }}</h2>
      <p>{{ visionText }}</p>
    </div>

    <!-- Design Philosophy Section with creative hover effect -->
    <div class="design-section">
      <h2>{{ designTitle }}</h2>
      <div class="design-philosophy" v-for="point in designPoints" :key="point.title">
        <h3>{{ point.title }}</h3>
        <p>{{ point.description }}</p>
      </div>
    </div>

    <!-- Interactive Features Section -->
    <div class="features-section">
      <h2>{{ featuresTitle }}</h2>
      <div class="features-grid">
        <div class="feature-card" v-for="feature in features" :key="feature.title">
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </div>

    <!-- Future Plans Section with animated background -->
    <div class="future-section">
      <h2>{{ futureTitle }}</h2>
      <p>{{ futureText }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutUs",
  data() {
    return {
      aboutTitle: "About TaskWise",
      aboutIntro:
        "At TaskWise, our goal is to help individuals and teams manage their tasks and finances with ease and efficiency. Let us take you through what we stand for and how we work towards innovation every day.",
      goals: [
        {
          title: "Simplifying Task Management",
          description:
            "We aim to break down complex task management into simple, digestible actions, ensuring that users of all skill levels can navigate the platform effortlessly.",
        },
        {
          title: "Financial Control",
          description:
            "Our vision extends beyond task tracking—TaskWise enables you to control your finances with tools that offer insightful analysis and goal-setting.",
        },
      ],
      visionTitle: "Our Vision",
      visionText:
        "We envision a world where managing time and finances is second nature. TaskWise strives to be the one-stop solution for handling both personal and professional tasks with innovative tools that make organization a breeze.",
      designTitle: "Design Philosophy",
      designPoints: [
        {
          title: "User-Centered Design",
          description:
            "Our platform is built with the end-user in mind, ensuring a fluid and intuitive experience across devices.",
        },
        {
          title: "Minimalism and Functionality",
          description:
            "TaskWise embraces minimalism while ensuring that the core features are powerful, practical, and always accessible.",
        },
      ],
      featuresTitle: "Key Features",
      features: [
        {
          title: "Task Manager",
          description:
            "Track, categorize, and prioritize tasks with ease. Manage deadlines and stay ahead of your schedule.",
        },
        {
          title: "Expense Manager",
          description:
            "Monitor your expenses with powerful charts that display spending habits on a weekly, monthly, and yearly basis.",
        },
        {
          title: "Customizable Panels",
          description:
            "Tailor your dashboard and share it with others for collaborative projects, ensuring everyone stays on the same page.",
        },
      ],
      futureTitle: "Looking Ahead",
      futureText:
        "We’re continuously developing new features and improving our platform based on feedback. Our future plans include expanding cross-platform accessibility, introducing AI-powered insights, and enhancing team collaboration tools.",
    };
  },
};
</script>

<style scoped lang="scss">
.about-us-container {
  padding: 2rem;
  background-color: #f9f9f9;
  color: #2c3e50;
  font-family: 'Arial', sans-serif;

  .about-header {
    text-align: center;
    margin-bottom: 3rem;
    background: linear-gradient(135deg, #3498db, #2c3e50);
    padding: 2rem;
    border-radius: 10px;
    color: #fff;
    animation: fadeInDown 1.5s ease-out;

    h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
      text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
      animation: slideInFromLeft 1s ease;
    }

    p {
      font-size: 1.3rem;
      max-width: 700px;
      margin: 0 auto;
    }
  }

  .about-vision, .future-section {
    text-align: center;
    margin-bottom: 3rem;
    background-color: #eaf2f8;
    padding: 2rem;
    border-radius: 10px;

    h2 {
      font-size: 2.2rem;
      color: #3498db;
      text-transform: uppercase;
    }

    p {
      font-size: 1.2rem;
      max-width: 800px;
      margin: 0 auto;
    }

    &:hover {
      background-color: #d4e6f1;
      transition: background-color 0.5s ease-in-out;
    }
  }
  .about-section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 2rem;

    .about-content {
      background-color: #ffffff;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease-in-out;
      
      h2, h3 {
        color: #3498db;
      }

      &:hover {
        transform: translateY(-5px);
      }
    }
  }

  .design-section {
    background-color: #f4f6f7;
    padding: 3rem 2rem;
    border-radius: 10px;

    h2 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 1.5rem;
      color: #2c3e50;
    }

    .design-philosophy {
      background-color: #ffffff;
      padding: 2rem;
      border-radius: 8px;
      margin-bottom: 2rem;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease-in-out;

      &:hover {
        transform: translateY(-10px);
      }

      h3 {
        color: #3498db;
      }
    }
  }

  .features-section {
  background-color: #f8f9fa;
  padding: 4rem 2rem;
  border-radius: 12px;
  text-align: center;

  h2 {
    font-size: 2.5rem;
    margin-bottom: 2rem;
    color: #2c3e50;
    text-transform: uppercase;
    letter-spacing: 2px;
    position: relative;
    display: inline-block;
    padding-bottom: 0.5rem;
    &:before {
      content: '';
      position: absolute;
      left: 50%;
      bottom: 0;
      transform: translateX(-50%);
      width: 50px;
      height: 3px;
      background-color: #3498db;
    }
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }

  .feature-card {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;

    &:hover {
      transform: translateY(-10px);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    h3 {
      font-size: 1.8rem;
      color: #3498db;
      margin-bottom: 1rem;
    }

    p {
      font-size: 1.1rem;
      color: #7f8c8d;
      line-height: 1.6;
    }
  }
}
}

@keyframes slideInFromLeft {
  0% {
    opacity: 0;
    transform: translateX(-100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInDown {
  0% {
    opacity: 0;
    transform: translateY(-50%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(50%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
