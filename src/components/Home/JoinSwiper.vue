<template>
  <div>
    <base-swiper class="swiper">
      <base-slide
        v-for="[idx, slide] in joinSlides.entries()"
        :key="idx"
        :background="slide.background"
      >
        <!-- <img :src="slide.background" class="background" /> -->
        <div class="content">
          <div class="from">
            {{ slide.from }}
          </div>
          <div v-html="slide.desc" class="desc"></div>
        </div>
      </base-slide>
    </base-swiper>
  </div>
</template>

<script>
import BaseSwiper from '@/components/BaseSwiper.vue';
import BaseSlide from '@/components/BaseSlide.vue';

export default {
  components: {
    BaseSwiper,
    BaseSlide,
  },
  data() {
    return {
      joinSlides: [
        {
          background: 'https://wj.qq.com/image/pc/act/join_1@2x.jpg',
          desc: '轻松赚取<br/>奖励红包和惊喜礼物',
          from: '在校学生',
        },
        {
          background: 'https://wj.qq.com/image/pc/act/join_2@2x.jpg',
          desc: '优先获得<br/>腾讯问卷行业报告',
          from: '企业管理者',
        },
        {
          background: 'https://wj.qq.com/image/pc/act/join_3@2x.jpg',
          desc: '亲自参与<br/>产品优化与迭代',
          from: '自由职业者',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.swiper {
  width: 745px;
  .content {
    position: relative;
    display: flex;
    flex-direction: column;
    margin-top: 70px;
    margin-left: 40px;

    color: #fff;
    .from {
      font-size: 18px;
      line-height: 1;
      margin-bottom: 30px;
    }
    .desc {
      font-size: 38px;
      text-shadow: 0px 2.5px 2.5px rgba(0, 0, 0, 0.1);
    }
  }
}
</style>
