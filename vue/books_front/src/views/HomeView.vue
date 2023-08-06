<template>
  <div>
    Home
    {{ bookStore.test }}
    <button @click="bookStore.d">+</button>
  </div>
</template>

<script>
import { useBookStore } from '../stores/counter';
  export default {
    data(){
      return{
        bookStore: useBookStore()
      }
    }
    
  }
</script>

<style scoped>

</style>