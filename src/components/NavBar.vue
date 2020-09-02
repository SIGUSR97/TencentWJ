<template>
  <div :class="`navbar-wrapper container ${containerWidth}`">
    <div class="start" v-if="hasSlot('start')">
      <slot name="start"> </slot>
    </div>
    <router-link
      class="nav-menu-item"
      v-for="[idx, link] in links.entries()"
      :key="idx"
      :to="link.path"
    >
      {{ link.name }}
    </router-link>
    <div class="end" v-if="hasSlot('end')">
      <slot name="end"> </slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    links: {
      type: Array,
      default: () => [{ name: 'home', path: '/' }],
    },
    containerWidth: {
      type: String,
      default: '',
      validator(value) {
        return ['wide', 'wider', ''].indexOf(value) !== -1;
      },
    },
  },
  methods: {
    pathOrName(link) {
      return link.path ? 'path' : 'name';
    },
    hasSlot(name) {
      return Boolean(this.$slots[name]);
    },
  },
  mounted() {
    console.log(this.$el);
  },
};
</script>

<style lang="scss" scoped>
$brand-color: #2f8cdb;
$hover-underline-width: 2px;

$default-height: 60px;
$default-background: #fff;
$default-padding: 20px;
$default-font-size: 17px;
$default-spacing: 50px;
$default-font: 'PingFang SC', tahoma, arial, 'helvetica neue',
  'hiragino sans gb', 'microsoft yahei ui', 'microsoft yahei', simsun,
  sans-serif;

$transition-fast: 100ms all ease-in-out;

@mixin menu-item {
  display: flex;
  flex-direction: column;
  align-items: center;

  line-height: $default-height;
  text-decoration: none;

  margin-left: $default-spacing;
  flex-shrink: 0;

  font-family: $default-font;

  cursor: pointer;
}

@mixin underline-ani($color, $size: 2px) {
  background-image: linear-gradient($color, $brand-color);
  background-repeat: no-repeat;
  background-size: 0 $size;
  background-position: 50% 100%;
  transition: $transition-fast;

  &:hover {
    color: $brand-color;
    background-size: 100% $size;
  }
}

* {
  user-select: none;
  // z-index: 1000;
}

.navbar-wrapper {
  position: relative;
  display: flex;
  flex-direction: row;
  align-content: center;
  // justify-content: center;

  width: 100%;
  height: $default-height;
  margin: 0 auto;
  // max-width: 1040px;
  padding: 0 $default-padding;

  background-color: $default-background;

  font-size: $default-font-size;
}

.nav-menu-item:nth-child(1) {
  margin-left: 0;
}

.nav-menu-item {
  @include menu-item;

  $underline-thickness: 2px;
  @include underline-ani($brand-color, $underline-thickness);
  color: #000;

  &.router-link-active {
    background-size: 100% $underline-thickness;
  }
}

.start {
  @include menu-item;
  margin-left: 0;
  margin-right: 9px;
  transition: $transition-fast;
  &:hover {
    color: $brand-color;
  }
}

.end {
  @include menu-item;

  margin-left: auto;
  align-self: center;
}
</style>
