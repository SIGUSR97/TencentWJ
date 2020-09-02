<template>
  <div class="home">
    <tencent-navbar></tencent-navbar>
    <index-swiper></index-swiper>
    <live-stat></live-stat>
    <popular-templates></popular-templates>
    <user-comments></user-comments>
    <join-tencent></join-tencent>
    <tencent-info></tencent-info>
    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import IndexSwiper from '@/components/IndexSwiper.vue';
import LiveStat from '@/components/LiveStat.vue';
import PopularTemplates from '@/components/PopularTemplates.vue';
import UserComments from '@/components/UserComments.vue';
import JoinTencent from '@/components/JoinTencent.vue';
import TencentInfo from '@/components/TencentInfo.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';

export default {
  name: 'Home',
  components: {
    TencentNavbar,
    IndexSwiper,
    LiveStat,
    PopularTemplates,
    UserComments,
    JoinTencent,
    TencentInfo,
    CopyrightFooter,
  },
  data() {
    return {};
  },
};
</script>
