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
