<template>
  <div>
    <tencent-navbar></tencent-navbar>
    <div style="padding-top: 100px;">this is a test page</div>

    <copyright-footer></copyright-footer>
  </div>
</template>

<script>
import TencentNavbar from '@/components/TencentNavbar.vue';
import CopyrightFooter from '@/components/CopyrightFooter.vue';

export default {
  components: {
    TencentNavbar,
    CopyrightFooter,
  },
};
</script>

<style lang="scss" scoped></style>
