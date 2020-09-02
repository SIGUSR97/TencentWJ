<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      links: [
        { name: '创建问卷', path: '/' },
        { name: '我的问卷', path: './test' },
        { name: '回答小组', path: './test' },
        { name: '调查资讯', path: './test' },
        { name: '帮助中心', path: './test' },
      ],
      user: {
        loggedIn: true,
        profilePic: 'http://localhost:8000/img/profile',
      },
    };
  },
};
</script>

<style lang="scss">
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
</style>
