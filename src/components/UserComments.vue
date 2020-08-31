<template>
  <div class="user-comments-wrapper">
    <div class="user-comments">
      <h2 class="section-title">他们正在使用</h2>
      <div class="comment">
        {{ comments[currentCommentIdx].comment }}
      </div>
      <div class="users">
        <div
          class="user"
          v-for="[idx, comment] in comments.entries()"
          :key="idx"
          @click="currentCommentIdx = idx"
        >
          <img
            :src="comment.user.avatar"
            :class="{
              avatar: true,
              selected: idx === currentCommentIdx,
            }"
          />
          <div class="detail">
            <div class="name">{{ comment.user.name }}</div>
            <div class="corp">{{ comment.user.corp }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      currentCommentIdx: 0,
      comments: [
        {
          comment:
            '我们的问卷投放量很大，每次问卷调查都是一次品牌形象宣传，因此除了问卷功能，更注重系统环境的稳定性。在评估后，我们决定选择腾讯问卷，事实证明百万的问卷数据承载毫无压力，可靠！',
          user: {
            avatar: 'https://wj.qq.com/image/avatar_thomas.png',
            corp: '小米路由器',
            name: 'Thomas',
          },
        },
        {
          comment:
            '腾讯问卷提供的调查问卷模板可订制化服务，增加了页面趣味性，降低了用户点击成本，问卷的回收率简单轻松翻倍，还收获了不少用户的好评。',
          user: {
            avatar: 'https://wj.qq.com/image/avatar_cctv.png',
            corp: '中央电视台',
            name: '315晚会',
          },
        },
        {
          comment:
            '界面简洁轻量，QQ登录即可免费使用，问卷发布快捷方便，再也不用人工处理问卷数据，大大节省了调研成本，是很赞的自助式在线问卷调查服务的平台！',
          user: {
            avatar: 'https://wj.qq.com/image/avatar_tongcheng.png',
            corp: '同程网',
            name: '火车票调查',
          },
        },
        {
          comment:
            '腾讯问卷在编辑方式上更加灵活高效，不同用户环境下的交互体验更友好，前端稳定性、安全性表现尤为优异，为海量车主调研项目提供了可靠的基础支撑，用起来更踏实！',
          user: {
            avatar: 'https://wj.qq.com/image/avatar_didi.png',
            corp: '滴滴',
            name: '滴滴代驾',
          },
        },
        {
          comment:
            '腾讯问卷的扁平化设计做得很好，交互设计的体验也很棒，在对比多个平台后选择使用腾讯问卷，帮我轻轻松松完成了调研！',
          user: {
            avatar: 'https://wj.qq.com/image/avatar_lianjia.png',
            corp: '链家',
            name: '链家网',
          },
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.user-comments-wrapper {
  background-color: #fafafa;
}

.user-comments {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
  max-width: 1040px;
  min-width: 980px;
  margin: 0 auto;

  background-color: #fafafa;

  font-family: 'PingFang SC', tahoma, arial, 'helvetica neue',
    'hiragino sans gb', 'microsoft yahei ui', 'microsoft yahei',
    simsun, sans-serif;
}

.section-title {
  padding: 35px 0 0;
  color: #999;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
  text-align: center;
  font-size: 20px;
  font-weight: 400;
}

$user-margin-top: 31px;

.users {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;

  width: 100%;
  margin-bottom: 40px;
  padding: 0 20px;
  border-top: 1px solid #ddd;
}

.user {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-self: center;

  margin-top: $user-margin-top;

  cursor: pointer;

  &:hover > .avatar {
    box-shadow: #58a6e7 0 0 0 2px;
  }

  .avatar {
    position: relative;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 7px;
    &.selected {
      box-shadow: #58a6e7 0 0 0 2px;
    }
  }

  .name {
    font-size: 14px;
    margin-left: 5px;
  }

  .corp {
    margin-left: 4px;
    margin-top: 3px;
    font-size: 14px;
    color: #999;
  }
}

.comment {
  margin-top: 20px;
  font-size: 16px;
  height: 80px;
  align-self: flex-start;
}
</style>
