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
import IndexSwiper from '@/components/Home/IndexSwiper.vue';
import LiveStat from '@/components/Home/LiveStat.vue';
import PopularTemplates from '@/components/Home/PopularTemplates.vue';
import UserComments from '@/components/Home/UserComments.vue';
import JoinTencent from '@/components/Home/JoinTencent.vue';
import TencentInfo from '@/components/Home/TencentInfo.vue';
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
