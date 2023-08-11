<template>

    <div class="test">
        <AboutComponent
            :post="bookStore.post_pk"
        />
    </div>
    
</template>

<script>
import { useBookStore } from '../stores/bookStore';
import AboutComponent from '../components/AboutComponent.vue';
    export default {
        data(){
            return{
                bookStore: useBookStore()
            }
        },
        components:{
            AboutComponent
        }
    }
</script>

<style scoped>
.test{
    color:  wheat;
}
</style>