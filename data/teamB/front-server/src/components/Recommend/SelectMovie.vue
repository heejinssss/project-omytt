<template>
  <div class="container select_main" ref="container">

    <div class="modal" v-if="showModal">
    <div class="modal-content">
      <h2>추천하는 OTT는 {{ finalRecommend.name }}</h2>
      <button class="btn-3d red">
        <a v-bind:href="finalRecommend.signup" class="link-no-underline">가입하러 가기</a>
      </button>
      <button class="close-button" @click="closeModal">닫기</button>
    </div>
  </div>


    <div style="margin-bottom:10px">
    <button class="btn-3d yellow" @click="getSelect"><div class="dot"></div>RANDOM</button>
    <button class="btn-3d blue" @click="sendIds"><span>제출하기</span></button>
    </div>
    <SearchMovie2 />
    <SelectMovieItem 
    v-for="select in selects"
    :key="select.id"
    :select="select"
    />

  </div>
</template>

<script>
import SearchMovie2 from '@/components/Recommend/SearchMovie2'
import SelectMovieItem from '@/components/Recommend/SelectMovieItem'

export default {
  name: 'SelectMovie',
  data() {
    return {
      showModal: false
    }
  },
  components: {
    SelectMovieItem,
    SearchMovie2,
  },
  computed: {
    selects() {
      return this.$store.state.selects
    },
    selectedId() {
      return this.$store.state.selectedId
    },
    finalRecommend() {
      return this.$store.state.finalRecommend
    }
  },
  methods: {
    getSelect() {
      this.$store.dispatch('getSelect')
    },
    sendIds() {
      this.$store.dispatch('sendIds', this.selectedId).then(() => {
        this.openModal() // 모달 열기
      })
    },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    }
  }
}
</script>

<style scoped>
button {
  margin: 20px;
}
.modal {
  /* 모달 스타일 설정 */
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  /* 모달 내용 스타일 설정 */
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.link-no-underline {
  text-decoration: none; /* 밑줄 제거 */
  color: inherit; /* 상위 요소에서 상속된 색상 사용 */
}
.select_main {
  font-family: 'NanumSquareNeo-Variable';
  color: white;
}

h2 {
  color: black;
}
.btn-3d {
  width: 150px;
  margin-top: 50px;
  position: relative;
  display: inline-block;
  font-size: 22px;
  color: white;
  border-radius: 6px;
  text-align: center;
  transition: top .01s linear;
  text-shadow: 0 1px 0 rgba(0,0,0,0.15);
  border: none
}
.btn-3d.red:hover    {background-color: #e74c3c;}
.btn-3d.blue:hover   {background-color: #699DD1;}
.btn-3d.green:hover  {background-color: #80C49D;}
.btn-3d.purple:hover {background-color: #D19ECB;}
.btn-3d.yellow:hover {background-color: #dbbc4a;}
.btn-3d.cyan:hover   {background-color: #82D1E3;}

.btn-3d:active {
  top: 9px;
}
/* 3D button colors */
.btn-3d.red {
  background-color: #e74c3c;
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 #C24032,
        0 8px 0 1px rgba(0,0,0,0.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.red:active {
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.blue {
  background-color: #6DA2D9;
  box-shadow: 0 0 0 1px #6698cb inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(110, 164, 219, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.blue:active {
  box-shadow: 0 0 0 1px #6191C2 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.green {
  background-color: #82c8a0;
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(126, 194, 155, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.green:active {
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.purple {
  background-color: #cb99c5;
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(189, 142, 183, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.purple:active {
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.cyan {
  background-color: #7fccde;
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(102, 164, 178, .6),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.cyan:active {
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.yellow {
  background-color: #fdd750;
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(196, 172, 83, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.yellow:active {
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}

.close-button {
  /* 모달 닫기 버튼 스타일 설정 */
  padding: 10px 20px;
  background-color: #ccc;
  border: none;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
}

.close-button:hover {
  background-color: #999;
}

/* @keyframes shiny-btn {
  0% { -webkit-transform: scale(0) rotate(45deg); opacity: 0; }
  80% { -webkit-transform: scale(0) rotate(45deg); opacity: 0.5; }
  81% { -webkit-transform: scale(4) rotate(45deg); opacity: 1; }
  100% { -webkit-transform: scale(50) rotate(45deg); opacity: 0; }
} */
</style>
