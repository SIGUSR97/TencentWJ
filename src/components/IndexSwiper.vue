<template>
  <div>
    <base-swiper
      background="https://wj.qq.com/image/index_sliders_bg.jpg"
    >
      <base-slide
        v-for="[idx, slide] in indexSlides.entries()"
        :key="idx"
        class="slide"
      >
        <h2>
          {{ slide.title }}
        </h2>
        <h3>
          {{ slide.subtitle }}
        </h3>
        <img :src="slide.image" draggable="false" />
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
      indexSlides: [
        {
          title: '多方式创建编辑问卷',
          subtitle: '所有功能全部免费，简约好用，轻松开启在线调试',
          image:
            'https://wj.qq.com/image/index_slider_p0.png?v=@version',
        },
        {
          title: '免费简约的问卷系统',
          subtitle: '自由创建、导入问卷、使用模板三种方式随意选择',
          image:
            'https://wj.qq.com/image/index_slider_p1.png?v=@version',
        },
        {
          title: '数据实时在线统计分析',
          subtitle: '回收数据实时在线统计，图表化展示，清晰直观',
          image:
            'https://wj.qq.com/image/index_slider_p2.png?v=@version',
        },
        {
          title: '跨终端跨平台自适应',
          subtitle: 'PC、手机、平板不同终端自适应，调研随时随地',
          image:
            'https://wj.qq.com/image/index_slider_p3.png?v=@version',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.slide {
  display: flex;
  position: relative;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;

  height: 100%;
  width: 100%;

  color: #fff;
  line-height: 1.5;

  transition: 500ms all ease-in-out;

  h2 {
    padding-top: 110px;

    font-size: 50px;
    font-weight: normal;
  }

  h3 {
    margin: {
      top: -3px;
      bottom: 20px;
    }
    font-size: 20px;
    font-weight: normal;
  }

  img {
    display: inline-block;
    margin-top: 13px;
  }
}
</style>
