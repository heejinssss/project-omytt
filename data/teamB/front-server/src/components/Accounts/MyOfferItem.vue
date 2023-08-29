<template>
  <div>
    {{ offer.title }}
    <router-link :to="{
      name: 'MovieDetail',
      params: { id: offer.id }}">
      <img :src="getMoviePoster(offer)" alt="Movie Poster">
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MyOfferItem',
  props: {
    offer: Object
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