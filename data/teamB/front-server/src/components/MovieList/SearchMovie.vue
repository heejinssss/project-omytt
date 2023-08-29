<template>
  <div>

    <input class="m-3" type="text" v-model="searchQuery"
    @input="performSearch1" placeholder="검색어를 입력하세요" />
    <div v-if="movies.length === 0 && searchQuery !== ''">
      검색결과가 없습니다
    </div>

  </div>
</template>

<script>
export default {
  name: 'SearchMovie',
  data() {
    return {
      searchQuery: '',
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  methods: {
    performSearch1() {
      this.$store.dispatch('performSearch1', this.searchQuery)
    }
  },
}
</script>

<style scoped>
input {
  font-family: 'NanumSquareNeo-Variable';
}

</style>
