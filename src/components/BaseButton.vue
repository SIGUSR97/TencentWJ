<template>
  <button class="btn" :style="cssProps" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    color: { type: String, default: '#80c200' },
    colorActive: { type: String, default: '#5aae00' },
    textColor: { type: String, default: '#fff' },
    textColorActive: { type: String, default: '#fff' },
    border: { type: Boolean, default: false },
    borderColor: { type: String, default: '#000' },
    borderWidth: { type: Number, default: 1 },
    borderRadius: { type: Number, default: 3 },
    size: { type: String },
  },
  computed: {
    cssProps() {
      let width = 'auto';
      let height = '34px';
      if (this.size) [width, height] = this.size.split(' ').map((i) => `${i}px`);
      return {
        '--color-btn': this.color,
        '--color-btn-active': this.colorActive,
        '--text-color': this.textColor,
        '--text-color-active': this.textColorActive,
        '--border': `${this.borderWidth * this.border}px ${
          this.borderColor
        } solid`,
        '--border-radius': `${this.borderRadius}px`,
        '--width': width,
        '--height': height,
      };
    },
  },
};
</script>

<style lang="scss" scoped>
$transition-fast: 100ms all ease-in;

$btn-color: var(--color-btn);
$btn-color-active: var(--color-btn-active);
$text-color: var(--text-color);
$text-color-active: var(--text-color-active);
$border: var(--border);
$border-radius: var(--border-radius);

@mixin btn-size {
  width: var(--width);
  height: var(--height);
}

.btn {
  outline: none;
  border: none;

  background-color: $btn-color;
  @include btn-size;
  // padding: 0px 20px;
  border-radius: $border-radius;
  border: $border;
  color: $text-color;
  cursor: pointer;

  transition: $transition-fast;

  font-size: 14px;

  &:active,
  &:hover {
    background-color: $btn-color-active;
    color: $text-color-active;
  }
}
</style>
