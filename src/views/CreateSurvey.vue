<template>
  <div>
    <tencent-navbar container-width="wide"></tencent-navbar>
    <guide-banner></guide-banner>
    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import GuideBanner from '@/components/CreateSurvey/GuideBanner.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';

export default {
  components: {
    TencentNavbar,
    CopyrightFooter,
    GuideBanner,
  },
};
</script>

<style lang="scss" scoped></style>
