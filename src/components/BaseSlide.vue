<template>
  <div
    :style="{backgroundImage: `url(${background})`}"
    class="base-slide"
  >
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    background: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
@mixin unselectable {
  user-drag: none;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}

.base-slide {
  display: flex;
  flex-direction: column;
  position: relative;
  flex-shrink: 0;

  width: 100%;
  height: 100%;

  transition: 500ms all ease-in-out;

  background-repeat: no-repeat;
  background-size: cover;

  @include unselectable();

  & > * {
    @include unselectable();
  }
}
</style>
