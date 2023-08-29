<template>
  <div>
    <router-link :to="{
      name: 'MovieDetail',
      params: { id: movie.id }}">
      <img :src="getMoviePoster(movie)" alt="Movie Poster">
    </router-link>


  </div>
</template>

<script>
export default {
  name: 'MyMoviesItem',
  props: {
    movie: Object
  },
  methods: {
    getMoviePoster(movie) {
      if (movie.poster_path) {
        return 'https://image.tmdb.org/t/p/w300' + movie.poster_path
      }
    }
  }
}
</script>

<style>

</style>