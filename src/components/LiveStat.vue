<template>
  <div class="main-wrapper">
    <div class="stat">
      当前已经为广大用户完成<span class="user-count">{{
        userCount
      }}</span
      >份回收
    </div>
    <base-button class="get-started-btn">立即使用</base-button>
  </div>
</template>

<script>
import $ from 'jquery';
import axios from 'axios';
import BaseButton from '@/components/BaseButton.vue';

export default {
  components: {
    BaseButton,
  },
  data() {
    return {
      userCount: 0,
    };
  },
  methods: {
    animateUserCount(count) {
      $(this.$el)
        .find('.user-count')
        .each(function () {
          $(this)
            .prop('counter', 0)
            .animate(
              {
                counter: count,
              },
              {
                duration: 1000,
                easing: 'swing',
                step(now) {
                  $(this).text(Math.trunc(now).toLocaleString());
                },
              },
            );
        });
    },
  },
  watch: {
    userCount(newVal) {
      this.animateUserCount(newVal);
    },
  },
  mounted() {
    axios.get('http://localhost:8000/usercount').then((res) => {
      this.userCount = res.data.count;
    });
  },
};
</script>

<style lang="scss" scoped>
.main-wrapper {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;

  width: 100%;
  height: 142px;
  min-width: 1000px;
  max-width: 1000px;
  margin: 0 auto;
  border-bottom: 1px solid #ddd;
}

.stat {
  color: #999;
  font-size: 14px;
}

.user-count {
  color: #58a6e7;
  font-size: 30px;
  margin: 0 5px;
}

.get-started-btn {
  height: 48px;
  // line-height: 48px;
  padding: 0 41px;
  border-radius: 7px;
  font-size: 18px;
}
</style>
