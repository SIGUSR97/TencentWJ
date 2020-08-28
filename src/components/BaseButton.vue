<template>
  <button class="btn" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
$transition-fast: 100ms all ease-in;

$default-btn-color: #80c200;
$default-btn-color-active: #5aae00;
$default-height: 34px;

.btn {
  outline: none;
  border: none;

  background-color: $default-btn-color;
  height: $default-height;
  padding: 0px 20px;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;

  transition: $transition-fast;

  font-size: 14px;

  &:active,
  &:hover {
    background-color: $default-btn-color-active;
  }
}
</style>
