<template>
  <div
    class="wrapper"
    :style="{backgroundImage: `url(${this.background})`}"
    @mousedown="handleMouseDown"
    @mousemove="handleMouseMove"
    @mouseup="handleMouseUp"
    @touchstart="handleMouseDown"
    @touchmove="handleMouseMove"
    @touchend="handleMouseUp"
    @touchcancel="handleMouseUp"
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
      <img :src="slide.image" draggable="false" />
    </div>
    <div class="slider-controls">
      <div class="slider-controls-direction">
        <div class="prev"></div>
        <div class="next"></div>
      </div>
      <div
        class="slider-controls-pager"
        @click="handleStopPropagation"
      >
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
    delay: {
      type: Number,
      default: 10000,
    },
  },
  data() {
    return {
      selectedIdx: 0,
      autoNextSlideId: null,
    };
  },
  methods: {
    handleMouseDown(e) {
      if (e.changedTouches) e.clientX = e.changedTouches[0].pageX;
      this.startX = e.clientX;
      const el = $(this.$el).children()[0];
      const style = el.currentStyle || window.getComputedStyle(el);
      this.startMarginLeft = style.marginLeft;
      this.mouseMoveStarted = true;
    },
    handleMouseMove(e) {
      if (this.mouseMoveStarted) {
        if (e.changedTouches) e.clientX = e.changedTouches[0].pageX;
        const deltaX = e.clientX - this.startX;
        const el = $(this.$el).children()[0];
        el.style.transition = 'none';
        el.style.marginLeft = `${Number.parseInt(
          this.startMarginLeft,
          10,
        ) + deltaX}px`;
      }
    },

    handleMouseUp() {
      $(this.$el).children()[0].style.transition = null;
      this.mouseMoveStarted = false;
      const el = $(this.$el).children()[0];
      const style = el.currentStyle || window.getComputedStyle(el);
      const marginLeft = Number.parseInt(style.marginLeft, 10);
      const width = $(this.$el).width();
      const margins = [...this.slides.keys()].map((i) => i * -width);
      // console.log(margins.map((m) => m - marginLeft));
      const [, index] = margins
        .map((m) => m - marginLeft)
        .reduce(
          (prev, cur, idx) => {
            // eslint-disable-next-line comma-spacing
            const [pval, ,] = prev;
            if (Math.abs(cur) < Math.abs(pval)) return [cur, idx];
            return prev;
          },
          [2e32, -1],
        );
      // console.log('idx: ', index);
      this.selectedIdx = index;
      this.updateSlide(index);
    },
    updateSlide(idx) {
      const width = $(this.$el).width();
      const newMargin = `${-idx * width}px`;
      const el = $(this.$el).children()[0];
      if (el.style.marginLeft !== newMargin) el.style.marginLeft = newMargin;
    },
    resetSlidePosition() {},
    nextSlide() {
      this.selectedIdx += 1;
      if (this.selectedIdx >= this.slides.length) this.selectedIdx = 0;
    },
    autoNextSlide() {
      return setInterval(this.nextSlide, this.delay);
    },
    resetAutoNextSlide() {
      if (this.autoNextSlideId) {
        this.autoNextSlideId = clearInterval(this.autoNextSlideId);
        // clearTimeout(this.autoNextSlideId);
      }
      if (this.resetAutoSlideId) {
        clearTimeout(this.autoNextSlideId);
        const that = this;
        this.resetAutoSlideId = setTimeout(() => {
          that.autoNextSlideId = that.autoNextSlide();
        }, this.delay * 2);
      }
    },
    handleStopPropagation() {
      return false;
    },
  },
  watch: {
    selectedIdx(idx) {
      this.updateSlide(idx);
    },
  },
  mounted() {
    this.autoNextSlide();
    // console.log('watchers: ', this.$watch);
    document.addEventListener('mouseup', this.handleMouseUp);
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
  user-select: none;
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
  justify-content: center;

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

  @include sizes(11px);
  image-rendering: crisp-edges;
}

.pager {
  background: {
    image: url("data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-circle-fill' fill='%23fff' xmlns='http://www.w3.org/2000/svg'%3E %3Ccircle cx='8' cy='8' r='8'/%3E %3C/svg%3E");
    repeat: no-repeat;
    size: 100%;
  }
  image-rendering: crisp-edges;
}
</style>
