<template>
  <div>
    <tencent-navbar container-width="wide"></tencent-navbar>
    <guide-banner></guide-banner>
    <upload-survey></upload-survey>
    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import GuideBanner from '@/components/CreateSurvey/GuideBanner.vue';
import UploadSurvey from '@/components/CreateSurvey/UploadSurvey.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';

export default {
  components: {
    TencentNavbar,
    GuideBanner,
    UploadSurvey,
    CopyrightFooter,
  },
};
</script>

<style lang="scss" scoped></style>
