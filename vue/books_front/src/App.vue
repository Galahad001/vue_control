<template>
  <div>
    <MainHeader/>
    <div id='test'>
      <RouterView />
    </div>
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
  width: 100%;
}

</style>