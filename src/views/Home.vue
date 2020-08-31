<template>
  <div class="home">
    <index-swiper></index-swiper>
    <live-stat></live-stat>
    <popular-templates></popular-templates>
    <user-comments></user-comments>
    <join-tencent></join-tencent>
    <tencent-info></tencent-info>
  </div>
</template>

<script>
import IndexSwiper from '@/components/IndexSwiper.vue';
import LiveStat from '@/components/LiveStat.vue';
import PopularTemplates from '@/components/PopularTemplates.vue';
import UserComments from '@/components/UserComments.vue';
import JoinTencent from '@/components/JoinTencent.vue';
import TencentInfo from '@/components/TencentInfo.vue';

export default {
  name: 'Home',
  components: {
    IndexSwiper,
    LiveStat,
    PopularTemplates,
    UserComments,
    JoinTencent,
    TencentInfo,
  },
  data() {
    return {};
  },
};
</script>
