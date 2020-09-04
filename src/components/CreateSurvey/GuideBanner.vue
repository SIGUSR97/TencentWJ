<template>
  <div class="guide-banner">
    <div class="type create-by-empty">
      <div class="type-avatar"></div>
      <h2 class="title">创建空白问卷</h2>
      <h3 class="subtitle">从一份空白问卷开始创建</h3>
      <base-button
        color="transparent"
        color-active="#fff"
        text-color="#fff"
        text-color-active="#3992dd"
        border
        border-color="#fff"
        size="105 45"
      >
        开始
      </base-button>
      <!-- <a class="btn btn_default" href="/edit.html">开始</a> -->
    </div>
    <div class="type create-by-template">
      <div class="type-avatar"></div>
      <h2 class="title">选择问卷模板</h2>
      <h3 class="subtitle">使用腾讯问卷提供的专业模板</h3>
      <base-button
        color="transparent"
        color-active="#fff"
        text-color="#fff"
        text-color-active="#52a3e7"
        border
        border-color="#fff"
        size="105 45"
      >
        开始
      </base-button>
    </div>
    <div class="type create-by-import">
      <div class="type-avatar"></div>
      <h2 class="title">文本编辑问卷</h2>
      <h3 class="subtitle">自由编辑文本自动生成问卷</h3>
      <base-button
        color="transparent"
        color-active="#fff"
        text-color="#fff"
        text-color-active="#97d886"
        border
        border-color="#fff"
        size="105 45"
      >
        开始
      </base-button>
    </div>
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
$transition-fast: 100ms all ease-in;

.guide-banner {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;

  width: 100%;
  min-width: 980px;
  height: 510px;

  .type {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    height: 100%;

    text-align: center;
    line-height: 1.5;
    background-repeat: no-repeat;

    flex-grow: 1;

    transition: $transition-fast;

    $avatar-sprite-url: url('https://wj.qq.com/image/pc/sprites_bg.png?v=1.9.80');
    &.create-by-empty {
      background-color: #3992dd;
      &:hover {
        background-color: #328edc;
      }

      .type-avatar {
        background-image: $avatar-sprite-url;
        background-position: -232px 0px;
        width: 154px;
        height: 152px;
        transform: scale(0.72);
      }
    }
    &.create-by-template {
      background-color: #52a3e7;
      &:hover {
        background-color: #4da0e7;
      }
      .type-avatar {
        background-image: $avatar-sprite-url;
        background-position: 0px 0px;
        width: 231px;
        height: 157px;
        transform: scale(0.7);
      }
    }
    &.create-by-import {
      background-color: #97d886;
      &:hover {
        background-color: #93d782;
      }
      .type-avatar {
        background-image: $avatar-sprite-url;
        background-position: 0px -158px;
        width: 189px;
        height: 162px;
        transform: scale(0.68);
      }
    }

    .title {
      color: #ffffff;
      margin-bottom: 0;
      font-size: 24px;
      font-weight: normal;
      -webkit-font-smoothing: antialiased;
      margin-top: 10px;
    }

    .subtitle {
      color: #ffffff;
      margin-top: 0;
      font-size: 18px;
      font-weight: normal;
      -webkit-font-smoothing: antialiased;
      margin-bottom: 38px;
    }
  }
}
</style>
