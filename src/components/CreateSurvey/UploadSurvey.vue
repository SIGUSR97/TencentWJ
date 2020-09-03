<template>
  <div class="upload-survey container wide">
    从Excel导入数据，并自动生成问卷
    <base-button
      color="#008fff"
      colorActive="#2196f3"
      size="100 36"
      :border-radius="4"
    >
      开始
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
.upload-survey {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;

  height: 70px;
  margin-top: 30px;
  background-color: #f4f6f9;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cpath d='M0 6h24v15a3 3 0 01-3 3H3a3 3 0 01-3-3V6z' fill='%23FFF'%3E%3C/path%3E%3Cpath fill='%23008FFF' d='M2 8h5v3H2z'%3E%3C/path%3E%3Cpath fill='%23008FFF' opacity='.3' d='M9 8h6v3H9zM17 8h5v3h-5zM2 13h5v3H2zM9 13h6v3H9zM17 13h5v3h-5zM2 18h5v3H2zM9 18h6v3H9zM17 18h5v3h-5z'%3E%3C/path%3E%3Cpath d='M3 0h18a3 3 0 013 3v3H0V3a3 3 0 013-3z' fill='%23008FFF'%3E%3C/path%3E%3C/g%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-size: 24px;
  background-position: 20px 50%;

  font-size: 20px;

  padding: {
    left: 54px;
    right: 20px;
  }
}
</style>
