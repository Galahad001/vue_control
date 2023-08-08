<template>

    <div class="test" v-for="post in bookStore.posts_filter">
        <AboutComponent
            :post="post"
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