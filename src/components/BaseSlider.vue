<template>
  <div
    class="wrapper"
    :style="{backgroundImage: `url(${this.background})`}"
  >
    <div
      v-for="[idx, slide] in slides.entries()"
      :key="idx"
      class="slider"
    >
      <h2>
        {{ slide.title }}
      </h2>
      <h3>
        {{ slide.subtitle }}
      </h3>
      <img :src="slide.image" alt="" />
    </div>
    <div class="slider-controls">
      <div class="slider-controls-direction">
        <div class="prev"></div>
        <div class="next"></div>
      </div>
      <div class="slider-controls-pager">
        <div
          v-for="idx in slides.keys()"
          :key="idx"
          :class="{
            'slider-pager-item': true,
            pager: idx !== selectedIdx,
            'pager-selected': idx === selectedIdx,
          }"
          @click="selectedIdx = idx"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  props: {
    background: {
      type: String,
    },
    slides: {
      type: Array,
    },
  },
  data() {
    return {
      selectedIdx: 0,
    };
  },
  methods: {},
  watch: {
    selectedIdx(idx) {
      const width = $(this.$el).width();
      $(this.$el).children()[0].style.marginLeft = `${-idx
        * width}px`;
    },
  },
  mounted() {
    const that = this;
    setInterval(() => {
      that.selectedIdx += 1;
      if (that.selectedIdx >= that.slides.length) that.selectedIdx = 0;
    }, 5000);
  },
};
</script>

<style lang="scss" scoped>
$default-height: 510px;

@mixin sizes($w, $h: -1) {
  @if $h < 0 {
    $h: $w;
  }

  width: $w;
  height: $h;
}

.wrapper {
  display: flex;
  position: relative;

  width: 100%;
  height: $default-height;

  overflow: hidden;
  background: {
    repeat: no-repeat;
    size: cover;
    position: 50% 0;
  }
}

.slider {
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

.slider-controls-pager {
  display: flex;
  position: absolute;
  align-items: center;

  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.slider-pager-item {
  @include sizes(10px);

  margin: 0 4px;
  cursor: pointer;
}

.pager-selected {
  background: {
    image: url("data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-circle' fill='%23fff' xmlns='http://www.w3.org/2000/svg'%3E %3Cpath fill-rule='evenodd' d='M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/%3E %3C/svg%3E");
    repeat: no-repeat;
    size: 100%;
  }

  @include sizes(12px);
}

.pager {
  background: {
    image: url("data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-circle-fill' fill='%23fff' xmlns='http://www.w3.org/2000/svg'%3E %3Ccircle cx='8' cy='8' r='8'/%3E %3C/svg%3E");
    repeat: no-repeat;
    size: 100%;
  }
}
</style>
