<template>
  <div class="base-slide">
    <slot></slot>
  </div>
</template>

<script>
export default {};
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
  position: relative;

  width: 100%;

  transition: 500ms all ease-in-out;

  @include unselectable();
}
</style>
