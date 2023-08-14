<template>

    <MainHeader/>
    <div id='test'>
      <RouterView />
    </div>

</template>

<script>
import { RouterView } from 'vue-router';
import MainHeader from './components/MainHeader.vue';
  export default {
    components:{
      MainHeader
    }
    
  }
</script>

<style scoped>
#test{
  width: 90%;
  margin: auto;
}

</style>