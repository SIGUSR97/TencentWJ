<template>
  <div class="create-survey">
    <tencent-navbar container-width="wide"></tencent-navbar>
    <guide-banner></guide-banner>
    <upload-survey></upload-survey>
    <recommended-templates></recommended-templates>
    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import GuideBanner from '@/components/CreateSurvey/GuideBanner.vue';
import UploadSurvey from '@/components/CreateSurvey/UploadSurvey.vue';
import RecommendedTemplates from '@/components/CreateSurvey/RecommendedTemplates.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';

export default {
  components: {
    TencentNavbar,
    GuideBanner,
    UploadSurvey,
    CopyrightFooter,
    RecommendedTemplates,
  },
};
</script>

<style lang="scss" scoped>
.container.wide {
  max-width: 1360px;
}
</style>
