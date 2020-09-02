<template>
  <div class="popular-templates container">
    <div class="section-title">
      <h2>热门模板</h2>
      <a href="/">查看全部模板&gt;&gt;</a>
    </div>
    <div class="template-button-wrapper">
      <template-button
        v-for="[idx, template] in popularTemplates.entries()"
        :key="idx"
        :thumbnail="template.src"
        :template-title="template.title"
      ></template-button>
    </div>
  </div>
</template>

<script>
import TemplateButton from '@/components/TemplateButton.vue';

export default {
  components: {
    TemplateButton,
  },
  data() {
    return {
      popularTemplates: [
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/medical.png',
          title: '身体健康状况调查',
        },
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/chat.png',
          title: '社交网站满意度',
        },
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/tv.png',
          title: '数码家电类产品满意度',
        },
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/talent.png',
          title: '国际标准智商测试',
        },
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/coffee.png',
          title: '团购网站用户满意度',
        },
        {
          src:
            'https://wj.qq.com/data_temp/template_source/img/game.png',
          title: 'PC端游、页游满意度',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.section-title {
  display: flex;
  justify-content: space-between;
  align-items: baseline;

  width: 100%;
  margin: 38px 0 14px;

  h2 {
    font-size: 20px;
    font-weight: normal;
  }
  a {
    font-size: 13px;
    color: #58a6e7;
    text-decoration: none;
  }
}

.popular-templates {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  // justify-content: space-between;

  width: 100%;
  padding-bottom: 30px;
  margin: 0 auto;
}

.template-button-wrapper {
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  width: 100%;

  & >>> .template-button {
    flex-shrink: 0;
    margin-left: calc(20% - 168px);
  }

  // ::v-deep .template-button :not(:first-child) {
  // }
}

.template-button-wrapper > .template-button:not(:first-child) {
  margin-left: 32px;
  flex-shrink: 0;
}
// .template-button:nth-child(1) {
//   margin-left: 0;
// }
</style>
