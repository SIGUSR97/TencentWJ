<template>
  <div class="sub-header container wider">
    <base-button
      color="#008fff"
      color-active="#2196f3"
      size="105 35"
      icon="data:image/svg+xml,%3Csvg class='icon icon-add' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Cpath fill='%23bfe3ff' d='M40 18H22V0h-4v18H0v4h18v18h4V22h18v-4z'%3E%3C/path%3E%3C/svg%3E"
    >
      创建问卷
    </base-button>
  </div>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';

export default {
  components: {
    BaseButton,
  },
};
</script>

<style lang="scss" scoped>
.sub-header {
  padding-top: 60px;
}
</style>
