<template>
  <div class="recommended-templates-wrapper">
    <div class="recommended-templates container wide">
      <div class="title">为您推荐</div>
      <ul class="templates-list">
        <li class="template">
          身体健康状况调查<span class="ext">20个问题/3页</span>
        </li>
        <li class="template">
          学生身体健康状况调查<span class="ext">26个问题/3页</span>
        </li>
        <li class="template">
          教师身体健康状况调查<span class="ext">24个问题/3页</span>
        </li>
        <li class="template">
          中小学师生健康调查表<span class="ext">22个问题/3页</span>
        </li>
        <li class="template">
          xx市中小学师生健康调查表<span class="ext">5个问题/1页</span>
        </li>
        <li class="template">
          社交网站用户满意度调查<span class="ext">34个问题/4页</span>
        </li>
        <li class="template">
          购物网用户满意度调查<span class="ext">21个问题/1页</span>
        </li>
        <li class="template">
          数码家电类产品满意度模板<span class="ext"
            >32个问题/4页</span
          >
        </li>
        <li class="template">
          网购消费者行为习惯调查<span class="ext">28个问题/4页</span>
        </li>
        <li class="template">
          餐饮类团购用户满意度问卷模板<span class="ext"
            >31个问题/3页</span
          >
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>

.recommended-templates-wrapper {
  padding: {
    left: 20px;
    right: 20px;
  }
}

.recommended-templates {
  position: relative;

  margin-top: 40px;

  $template-item-height: 35px;

  .templates-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;

    height: calc(35px * 5);
    margin-top: 20px;
  }

  .title {
    font-size: 20px;
    font-weight: normal;
    line-height: 1;
    color: #333333;

    padding-bottom: 13px;

    border-bottom: 1px solid #d9d9d9;
    margin: 0;
  }

  ul,
  li {
    list-style: none outside none;
  }

  .template {
    $template-margin: 140px;

    display: flex;

    height: 35px;
    width: 50%;
    counter-increment: --template-counter;

    font-size: 16px;

    cursor: pointer;

    &::before {
      content: counter(--template-counter);
      display: inline;

      margin-right: 10px;
      font-size: 14px;
      font-style: italic;
      vertical-align: top;
    }

    &:hover,
    &:hover::before,
    &:nth-child(-n + 3)::before {
      color: #3da6ff;
    }

    &:nth-child(-n + 5) {
      width: calc(50% - #{$template-margin});
      margin-right: $template-margin;
    }

    .ext {
      margin-left: auto;

      font-size: 14px;
      color: #999999;
    }
  }
}
</style>
