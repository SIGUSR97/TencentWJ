<template>
  <div
    class="swiper-wrapper"
    :style="{backgroundImage: `url(${this.background})`}"
    @mousedown="handleMouseDown"
    @mousemove="handleMouseMove"
    @mouseup="handleMouseUp"
    @touchstart="handleMouseDown"
    @touchmove="handleMouseMove"
    @touchend="handleMouseUp"
    @touchcancel="handleMouseUp"
  >
    <div class="slides">
      <slot></slot>
    </div>
    <div class="slide-controls">
      <div class="slide-controls-direction">
        <div class="prev"></div>
        <div class="next"></div>
      </div>
      <div
        class="slide-controls-pager"
        @click="handleStopPropagation"
      >
        <div
          v-for="idx in slides.keys()"
          :key="idx"
          :class="{
            'slide-pager-item': true,
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
// import $ from 'jquery';

function clip(num, lower, upper) {
  return Math.min(Math.max(num, lower), upper);
}

export default {
  props: {
    background: {
      type: String,
    },
    delay: {
      type: Number,
      default: 5000,
    },
    pagerPosition: {
      type: String,
      default: 'bottom',
    },
  },
  data() {
    return {
      selectedIdx: 0,
      autoNextSlideId: null,
      slides: [],
    };
  },
  methods: {
    handleMouseDown(e) {
      if (e.changedTouches) e.clientX = e.changedTouches[0].pageX;
      this.startX = e.clientX;
      const el = this.firstSlide;
      const style = el.currentStyle || window.getComputedStyle(el);
      this.startMarginLeft = Number.parseInt(style.marginLeft, 10);
      this.startIdx = this.selectedIdx;
      this.mouseMoveStarted = true;

      this.stopAutoNextSlide();
    },
    handleMouseMove(e) {
      if (this.mouseMoveStarted) {
        if (e.changedTouches) e.clientX = e.changedTouches[0].pageX;
        const deltaX = e.clientX - this.startX;
        const el = this.firstSlide;
        el.style.transition = 'none';
        el.style.marginLeft = `${Number.parseInt(
          this.startMarginLeft,
          10,
        ) + deltaX}px`;
      }
    },

    handleMouseUp() {
      const el = this.firstSlide;
      el.style.transition = null;
      this.mouseMoveStarted = false;
      const style = el.currentStyle || window.getComputedStyle(el);
      const marginLeft = Number.parseInt(style.marginLeft, 10);
      const deltaMargin = this.startMarginLeft - marginLeft;
      if (
        Math.abs(deltaMargin) > 50
        && this.startIdx === this.selectedIdx
      ) {
        this.selectedIdx += deltaMargin / Math.abs(deltaMargin);
        this.selectedIdx = clip(
          this.selectedIdx,
          0,
          this.slides.length - 1,
        );
      }
      if (this.autoNextSlideIntervalId === null) this.autoNextSlide();
      this.updateSlide(this.selectedIdx);
    },
    updateSlide(idx) {
      let newMargin = 0;

      // eslint-disable-next-line no-restricted-syntax
      for (const [i, child] of this.slides.entries()) {
        if (i === idx) break;
        newMargin -= child.getBoundingClientRect().width;
      }
      newMargin = `${newMargin}px`;
      const el = this.firstSlide;
      const style = el.currentStyle || window.getComputedStyle(el);
      if (style.marginLeft !== newMargin) el.style.marginLeft = newMargin;
    },
    nextSlide() {
      this.selectedIdx += 1;
      if (this.selectedIdx >= this.slides.length) this.selectedIdx = 0;
    },
    autoNextSlide() {
      this.autoNextSlideIntervalId = setInterval(
        this.nextSlide,
        this.delay,
      );
    },
    stopAutoNextSlide() {
      if (this.autoNextSlideIntervalId) {
        clearInterval(this.autoNextSlideIntervalId);
        this.autoNextSlideIntervalId = null;
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
    this.slides = Array.from(
      this.$el.querySelector('.slides').childNodes,
    );
    // eslint-disable-next-line
    this.firstSlide = this.slides[0];
    console.log('slides: ', this.slides);
    console.log(
      'slide rects: ',
      this.slides.map((el) => el.getBoundingClientRect()),
    );
    this.autoNextSlide();
    document.addEventListener('mouseup', this.handleMouseUp);
  },
};
</script>

<style lang="scss" scoped>
@mixin sizes($w, $h: -1) {
  @if $h < 0 {
    $h: $w;
  }

  width: $w;
  height: $h;
}

.swiper-wrapper {
  display: flex;
  position: relative;

  width: 100%;
  height: 100%;
  user-select: none;
  overflow: hidden;
  background: {
    repeat: no-repeat;
    size: cover;
    position: 50% 0;
  }
}

.slides {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;

  width: 100%;
  height: 100%;
}

.slide-controls-pager {
  display: flex;
  position: absolute;
  align-items: center;
  justify-content: center;

  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.slide-pager-item {
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
