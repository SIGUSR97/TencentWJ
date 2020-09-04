<template>
  <div class="sub-header container wider">
    <base-button
      color="#008fff"
      color-active="#2196f3"
      size="105 35"
      icon="data:image/svg+xml,%3Csvg class='icon icon-add' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Cpath fill='%23bfe3ff' d='M40 18H22V0h-4v18H0v4h18v18h4V22h18v-4z'%3E%3C/path%3E%3C/svg%3E"
    >
      创建问卷
    </base-button>
    <div class="tools">
      <div class="icon add-folder"></div>
      <div class="icon trash"></div>
      <div
        :class="['icon', view]"
        @click="view = view === 'list' ? 'grid' : 'list'"
      ></div>
    </div>
  </div>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';

export default {
  components: {
    BaseButton,
  },
  data() {
    return {
      view: 'list',
    };
  },
};
</script>

<style lang="scss" scoped>
$add-folder-icon: "data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-folder-plus' fill='currentColor' xmlns='http://www.w3.org/2000/svg'%3E %3Cpath fill-rule='evenodd' d='M9.828 4H2.19a1 1 0 0 0-.996 1.09l.637 7a1 1 0 0 0 .995.91H9v1H2.826a2 2 0 0 1-1.991-1.819l-.637-7a1.99 1.99 0 0 1 .342-1.31L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3h3.982a2 2 0 0 1 1.992 2.181L15.546 8H14.54l.265-2.91A1 1 0 0 0 13.81 4H9.828zm-2.95-1.707L7.587 3H2.19c-.24 0-.47.042-.684.12L1.5 2.98a1 1 0 0 1 1-.98h3.672a1 1 0 0 1 .707.293z'/%3E %3Cpath fill-rule='evenodd' d='M13.5 10a.5.5 0 0 1 .5.5V12h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V13h-1.5a.5.5 0 0 1 0-1H13v-1.5a.5.5 0 0 1 .5-.5z'/%3E %3C/svg%3E";
$trash-icon: "data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-trash-fill' fill='currentColor' xmlns='http://www.w3.org/2000/svg'%3E %3Cpath fill-rule='evenodd' d='M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5a.5.5 0 0 0-1 0v7a.5.5 0 0 0 1 0v-7z'/%3E %3C/svg%3E";
$list-icon: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M1.77,1.13H3.35A1.14,1.14,0,0,1,4.49,2.27v1A1.14,1.14,0,0,1,3.35,4.37H1.77A1.14,1.14,0,0,1,.63,3.23v-1A1.14,1.14,0,0,1,1.77,1.13Zm13.61,2.1v-1a1.16,1.16,0,0,0-1.15-1.15H6.61A1.16,1.16,0,0,0,5.46,2.27v1A1.15,1.15,0,0,0,6.61,4.37h7.62A1.15,1.15,0,0,0,15.38,3.23ZM1.77,6.37H3.35A1.14,1.14,0,0,1,4.49,7.52v1A1.15,1.15,0,0,1,3.35,9.63H1.77A1.15,1.15,0,0,1,.63,8.48v-1A1.15,1.15,0,0,1,1.77,6.37ZM15.38,8.48v-1a1.15,1.15,0,0,0-1.15-1.14H6.61A1.16,1.16,0,0,0,5.46,7.52v1A1.16,1.16,0,0,0,6.61,9.63h7.62A1.15,1.15,0,0,0,15.38,8.48ZM1.77,11.62H3.35a1.15,1.15,0,0,1,1.14,1.15v1a1.15,1.15,0,0,1-1.14,1.15H1.77A1.15,1.15,0,0,1,.63,13.73v-1A1.15,1.15,0,0,1,1.77,11.62Zm13.61,2.11v-1a1.16,1.16,0,0,0-1.15-1.15H6.61a1.15,1.15,0,0,0-1.15,1.14v1a1.16,1.16,0,0,0,1.15,1.15h7.62A1.15,1.15,0,0,0,15.38,13.73Z' fill='currentColor'/%3E%3C/svg%3E";
$grid-icon: "data:image/svg+xml,%3Csvg width='1em' height='1em' viewBox='0 0 16 16' class='bi bi-grid-3x3-gap-fill' fill='currentColor' xmlns='http://www.w3.org/2000/svg'%3E %3Cpath d='M1 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2zM1 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V7zM1 12a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-2zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-2z'/%3E %3C/svg%3E";

@function svg-color($url, $color) {
  @return str-slice($url, 0, str-index($url, 'currentColor') - 1) +
    '%23' + str-slice('#{$color}', 2, -1) +
    str-slice($url, str-index($url, 'currentColor') + 12);
}

.sub-header {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;

  padding: {
    top: 60px;
    left: 20px;
    right: 20px;
  }
  height: 120px;
  box-shadow: 0px 3px 8px 0px rgba(224, 229, 236, 0.4);

  .tools {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    width: 120px;
    // margin-left: auto;

    .icon {
      height: 20px;
      width: 20px;

      background-repeat: no-repeat;
      background-size: contain;

      cursor: pointer;
      &.add-folder {
        background-image: url(svg-color($add-folder-icon, #a9a9a9));
        &:hover {
          background-image: url(svg-color($add-folder-icon, #008fff));
        }
      }
      &.trash {
        background-image: url(svg-color($trash-icon, #a9a9a9));
        &:hover {
          background-image: url(svg-color($trash-icon, #008fff));
        }
      }
      &.list {
        background-image: url(svg-color($list-icon, #a9a9a9));
        &:hover {
          background-image: url(svg-color($list-icon, #008fff));
        }
      }
      &.grid {
        background-image: url(svg-color($grid-icon, #a9a9a9));
        &:hover {
          background-image: url(svg-color($grid-icon, #008fff));
        }
      }
    }
  }
}
</style>
