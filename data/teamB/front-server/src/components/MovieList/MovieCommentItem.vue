<template>
  <div class="commentBox">

    <hr style="color: white;"> <!-- 구분선 -->
    <div class="comment_user">
      <span class="comment_user">{{ comment.username }}</span>
    </div>

    <div class="comment">
      <span>{{ comment.content }}</span>
    </div>

    <hr style="color: white;"> <!-- 구분선 -->


  </div>
</template>

<script>
export default {
  name: 'MovieCommentItem',
  props: {
    comment: Object,
  }
}
</script>

<style scoped>
@font-face {
  font-family: 'SUITE-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}
/* .commentBox {
    background-color: #F9F5EB;
    box-sizing: border-box;
    padding: 0px 12px;
    border-radius: 6px;
    overflow: hidden;
    margin: 0px 0px 20px;
    color: black;
    font-family: 'SUITE-Regular';
} */
.comment_user {
  display: inline;
  float: left;
  margin-left: 10px;
  color:  rgb(255, 255, 255);
  font-weight: 700;
}
.comment {
  display: inline;
  color: white;
}
</style>