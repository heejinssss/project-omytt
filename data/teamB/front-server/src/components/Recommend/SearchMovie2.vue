<template>
  <div>

    <input class="m-3" type="text" v-model="searchQuery"
    @input="performSearch" placeholder="그 영화 뭐였지?" />

    <div v-if="selects.length === 0">텅</div>

  </div>
</template>

<script>
export default {
  name: 'SearchMovie2',

  data() {
    return {
      searchQuery: '',
      is_search: false,
    }
  },
  computed: {
    selects() {
      return this.$store.state.selects
    },
  },
  methods: {
    performSearch() {
      this.$store.dispatch('performSearch', this.searchQuery)
      // this.searchQuery = ''
    },
    searchToggle() {
      const container = this.$el.querySelector('.search-wrapper')
      if (!container.classList.contains('active')) {
        container.classList.add('active')
      } else {
        container.classList.remove('active')
        container.querySelector('.search-input').value = ''
      }
    }
  }
}
</script>

<style scoped>

body {
   background: #262433;
}

input {
  font-family: 'NanumSquareNeo-Variable';
}

</style>