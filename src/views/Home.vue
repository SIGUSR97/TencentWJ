<template>
  <div class="home">
    <index-swiper></index-swiper>
    <live-stat></live-stat>
    <popular-templates></popular-templates>
    <user-comments></user-comments>
    <join-tencent></join-tencent>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';
import LiveStat from '@/components/LiveStat.vue';
import PopularTemplates from '@/components/PopularTemplates.vue';
import UserComments from '@/components/UserComments.vue';
import JoinTencent from '@/components/JoinTencent.vue';
import IndexSwiper from '@/components/IndexSwiper.vue';

export default {
  name: 'Home',
  components: {
    LiveStat,
    PopularTemplates,
    UserComments,
    JoinTencent,
    IndexSwiper,
  },
  data() {
    return {
      indexSlides: [
        {
          title: '多方式创建编辑问卷',
          subtitle: '所有功能全部免费，简约好用，轻松开启在线调试',
          image:
            'https://wj.qq.com/image/index_slider_p0.png?v=@version',
        },
        {
          title: '免费简约的问卷系统',
          subtitle: '自由创建、导入问卷、使用模板三种方式随意选择',
          image:
            'https://wj.qq.com/image/index_slider_p1.png?v=@version',
        },
        {
          title: '数据实时在线统计分析',
          subtitle: '回收数据实时在线统计，图表化展示，清晰直观',
          image:
            'https://wj.qq.com/image/index_slider_p2.png?v=@version',
        },
        {
          title: '跨终端跨平台自适应',
          subtitle: 'PC、手机、平板不同终端自适应，调研随时随地',
          image:
            'https://wj.qq.com/image/index_slider_p3.png?v=@version',
        },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.slide {
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
</style>
