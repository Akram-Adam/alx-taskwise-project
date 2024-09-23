// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
// بدلاً من استخدام defineConfig، قم بتصدير الإعدادات بشكل مباشر
module.exports = {
  transpileDependencies: [
    // ضع هنا الحزم التي تريد تحويلها
  ]
};
