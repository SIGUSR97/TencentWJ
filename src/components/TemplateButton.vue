<template>
  <div class="template-button">
    <div class="thumbnail-wrapper">
      <img :src="thumbnail" class="thumbnail" />
    </div>
    <div class="template-title">
      {{ templateTitle }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    thumbnail: {
      type: String,
    },
    templateTitle: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.template-button {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  margin-top: 20px;

  cursor: pointer;
  &:hover {
    & > .template-title {
      color: #7da6e9;
    }
  }
}

.thumbnail-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 138px;
  height: 138px;
  background: #fafafa;
  border: 1px solid #ddd;
  border-radius: 5px;
  line-height: 138px;
  text-align: center;
}

.template-title {
  margin-top: 13px;
  text-align: center;
  font-size: 14px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
</style>
