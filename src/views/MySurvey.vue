<template>
  <div class="my-survey">
    <tencent-navbar container-width="wider"></tencent-navbar>
    <sub-header></sub-header>
    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';
import SubHeader from '@/components/MySurvey/SubHeader.vue';

export default {
  components: {
    TencentNavbar,
    CopyrightFooter,
    SubHeader,
  },
};
</script>

<style lang="scss" scoped></style>
