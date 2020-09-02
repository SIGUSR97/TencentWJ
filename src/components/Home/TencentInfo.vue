<template>
  <div class="tencent-info-wrapper">
    <div class="tencent-info container">
      <div class="description">
        <div>
          <span class="keyword simple">简约</span>
          <span class="keyword easy">好用</span>
          <span class="keyword free">免费</span>
        </div>
        <p class="slogan">腾讯问卷为您提供专业调研服务</p>
      </div>
      <div class="contact-us">
        <p class="bold">
          任何建议和问题随时
          <a
            target="_blank"
            href="https://support.qq.com/products/1221"
          >
            吐个槽
          </a>
        </p>
        <p class="contacts">
          官方邮箱：<a target="_blank" href="mailto:wj@tencent.com"
            >wj@tencent.com</a
          ><br />
          官方微博：<a target="_blank" href="https://weibo.com/txur"
            >腾讯问卷</a
          ><br />
          官方QQ群：
          <a
            target="_blank"
            href="http://shang.qq.com/wpa/qunwpa?idkey=cb9d044e3808db5db4eea628fe26ec7bbaee96c106959efe44b5ca53e9f18818"
            alt="腾讯问卷反馈群"
            title="腾讯问卷反馈群"
            >365694489</a
          >
          <br />
          客服QQ:&nbsp;
          <span class="contact-button">
            <img
              src="https://bqq.gtimg.com/qidian/src/wpa/dist/4.1.0/images/1_1_1.png"
              class="qq-img"
            />
            <span class="btn-text">在线咨询</span>
          </span>
        </p>
      </div>
      <div class="qr-code">
        <img
          src="https://wj.qq.com/image/wx_public_qr_code.png?v=@version"
          alt="二维码"
          class="qr-img"
        />
        <p class="bold">扫描关注微信公众号</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@mixin flex-column {
  display: flex;
  flex-direction: column;
  align-items: center;
}

@mixin flex-row {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.tencent-info-wrapper {
  position: relative;
  background: #f5f5f5;
  padding: 38px 0 20px;
}

.tencent-info {
  position: relative;
  @include flex-row();
  justify-content: space-around;

  width: 100%;
  // max-width: 1040px;
  // min-width: 980px;
  margin: 0 auto;

  color: #333;

  .description {
    @include flex-column();
    align-items: flex-start;
  }

  .slogan {
    margin-top: 22px;
    color: #999;
    font-size: 22px;
  }

  .keyword {
    line-height: 24px;
    display: inline-block;
    padding: 15px 0 15px 60px;
    margin-right: 20px;

    font-size: 20px;
    color: #58a6e7;

    background-repeat: no-repeat;

    &.simple {
      background-image: url('https://wj.qq.com/image/icon_simple.png?v=1.9.80');
    }
    &.easy {
      background-image: url('https://wj.qq.com/image/icon_easy.png?v=1.9.80');
    }
    &.free {
      background-image: url('https://wj.qq.com/image/icon_free.png?v=1.9.80');
    }
  }

  .bold {
    font-size: 16px;
    margin-bottom: 18px;
    a {
      font-size: 16px;
      color: #58a6e7;
      margin-left: 5px;
    }
  }

  .contacts {
    font-size: 13px;
    line-height: 190%;
    color: #999;
  }

  a {
    text-decoration: none;
    color: #333;
    &:hover {
      color: #58a6e7;
    }
  }

  .contact-button {
    // @include flex-row();
    position: relative;
    display: inline-block;
    vertical-align: bottom;
    background-color: #fff;
    border: #dadee7 1px solid;
    padding: 0px 8px;
    user-select: none;
    margin-left: 10px;
    cursor: pointer;
    .qq-img {
      position: relative;
      transform: translateY(25%);
      margin-right: 5px;
    }
    .btn-text {
      vertical-align: middle;
      font-size: 14px;
      height: 28px;
      line-height: 28px;
      margin-top: -3px;
      word-break: break-all;
      word-wrap: break-word;
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
    }
  }

  .qr-code {
    @include flex-column();
    .bold {
      margin-top: 5px;
      color: #999;
      font-size: 13px;
    }
  }
}
</style>
