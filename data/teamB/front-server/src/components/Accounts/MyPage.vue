<template>
  <div>
    <MyOtt />
    <MyMovies />
    <MyOffer />
  </div>
</template>

<script>
import MyMovies from '@/components/Accounts/MyMovies'
import MyOffer from '@/components/Accounts/MyOffer'
import MyOtt from '@/components/Accounts/MyOtt'

export default {
  name: 'MyPage',
  components: {
    MyMovies,
    MyOffer,
    MyOtt
  }
}
</script>

<style>

</style>