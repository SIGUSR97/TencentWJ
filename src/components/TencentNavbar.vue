<template>
  <div class="head">
    <nav-bar :links="links" :container-width="containerWidth">
      <template v-slot:start>
        <router-link to="/" tag="div" class="nav-icon">
          <img
            src="https://wj.qq.com/image/logo.png?v=@version"
            alt="腾讯问卷"
            class="icon-img"
          />
          <div class="tx-font">腾讯问卷</div>
        </router-link>
      </template>
      <template v-slot:end>
        <div class="logged-in" v-if="user.loggedIn">
          <div class="bell"></div>
          <img class="profile-pic" :src="user.profilePic" />
          <span class="splitter">|</span>
          <span class="quit">退出</span>
        </div>
        <base-button v-else>登录</base-button>
      </template>
    </nav-bar>
  </div>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';
import NavBar from '@/components/NavBar.vue';

export default {
  components: {
    NavBar,
    BaseButton,
  },
  data() {
    return {
      links: [
        { name: '创建问卷', path: '/guide' },
        { name: '我的问卷', path: '/test' },
        { name: '回答小组', path: '/test' },
        { name: '调查资讯', path: '/test' },
        { name: '帮助中心', path: '/test' },
      ],
      user: {
        loggedIn: true,
        profilePic: 'http://localhost:8000/img/profile',
      },
    };
  },
  props: {
    containerWidth: {
      type: String,
    },
  },
};
</script>

<style lang="scss" scoped>
$transition-fast: 100ms all ease-in;
$head-height: 60px;

@font-face {
  font-family: tencentFont;
  src: url('../assets/txFont.ttf');
}

@mixin sizes($w, $h: -1) {
  @if $h < 0 {
    $h: $w;
  }

  width: $w;
  height: $h;
}

.tx-font {
  font-family: tencentFont, 'PingFang SC', tahoma, arial,
    'helvetica neue', 'hiragino sans gb', 'microsoft yahei ui',
    'microsoft yahei', simsun, sans-serif;
}

.main {
  padding-top: $head-height;
}

.head {
  position: fixed;
  align-items: center;
  z-index: 1000;

  height: $head-height;
  width: 100%;
  margin: 0 auto;
  background-color: #fff;
  //   margin-left: auto;
  //   margin-right: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.nav-icon {
  display: flex;
  flex-direction: row;
  align-items: center;

  font-size: 21px;
  img {
    @include sizes(32px);
    margin-right: 5px;
  }
}

.bell {
  @include sizes(20px);
  background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAoBAMAAABgGZXtAAAAJ1BMVEUAAACpqampqampqampqampqampqampqampqampqampqampqampqanUNn22AAAADHRSTlMAk+rugFdMEK3FxInT9Pv5AAAAf0lEQVQoz2OAgTNnzsCY+MQSgWJiKCLsTmdAQKUASSzoDASoIoQYz8CAAFysBy52AlMZQmEMkthRqKU6SGKHIFaznEEGDmAxJhQxBbBYDorYMbCYDIrYQbDYGhSxk5AQQQWjYkAx4sEZTEBtMbzp2ebMYQwxmTOnMcQYjeFpFAC+EXAf3y47xwAAAABJRU5ErkJggg==');
  background-repeat: no-repeat;
  background-size: 100%;
}

.profile-pic {
  @include sizes(25px);
  border-radius: 50%;
  margin-left: 20px;
}

.quit {
  font-size: 14px;
  color: #333;
}

.logged-in {
  display: flex;
  flex-flow: row;
  align-items: center;
  justify-content: space;
}
.splitter {
  display: inline-block;
  color: #999;
  margin: 0 8px;
  font-size: 14px;
  font-family: 'PingFang SC', tahoma, arial, 'helvetica neue',
    'hiragino sans gb', 'microsoft yahei ui', 'microsoft yahei',
    simsun, sans-serif;
}
</style>
