import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Test from '../views/Test.vue';
import CreateSurvey from '../views/CreateSurvey.vue';
import MySurvey from '../views/MySurvey.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/test',
    name: 'test',
    component: Test,
  },
  {
    path: '/guide',
    name: 'guide',
    component: CreateSurvey,
  },
  {
    path: '/mine',
    name: 'mine',
    component: MySurvey,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
