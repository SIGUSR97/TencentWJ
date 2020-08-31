<template>
  <div class="join-wrapper">
    <div class="join-tencent">
      <join-swiper></join-swiper>
      <div class="content">
        <h3 class="ttq-title">欢迎关注卷叔填填圈</h3>
        <img
          src="https://wj.qq.com/image/ttq-qrcode@2x.png"
          class="qr-code"
        />
        <div class="ttq-search">公众号搜索“卷叔填填圈”</div>
      </div>
    </div>
  </div>
</template>

<script>
import JoinSwiper from '@/components/JoinSwiper.vue';

export default {
  components: {
    JoinSwiper,
  },
};
</script>

<style lang="scss" scoped>
@font-face {
  font-family: tencentFont;
  src: url('../assets/txFontTtq.ttf');
}

.join-wrapper {
  position: relative;

  margin: 0 auto;
  padding-bottom: 75px;

  background-color: #fafafa;
}

.join-tencent {
  position: relative;
  display: flex;
  flex-direction: row;
  // align-items: center;
  justify-content: space-evenly;

  // width: 100%;
  height: 310px;
  max-width: 1040px;
  min-width: 980px;
  margin: 0 auto;
  border: 1px solid #dddddd;
  border-radius: 3px;

  * {
    flex-shrink: 0;
  }
}

.content {
  width: 180px;

  margin: 0 auto;

  font-size: 16px;
  color: #f63a59;

  .ttq-title {
    border-radius: 4px;
    line-height: 34px;
    height: 34px;
    background-color: #f63a59;
    color: #fff;
    text-align: center;
    font-weight: normal;
    margin-top: 30px;
    margin-bottom: 15px;

    font-size: 1.17em;
    font-family: tencentFont, 'PingFang SC', tahoma, arial,
      'helvetica neue', 'hiragino sans gb', 'microsoft yahei ui',
      'microsoft yahei', simsun, sans-serif;
  }

  img {
    width: 100%;
    margin: 0 auto;
  }

  .ttq-search {
    font-size: 15px;
  }
}
</style>
