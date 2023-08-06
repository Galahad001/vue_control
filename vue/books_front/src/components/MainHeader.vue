<template>
    <header>
        <nav>
            <RouterLink to="/">Home</RouterLink> -
            <RouterLink to="/books">Books</RouterLink>
        </nav>
    </header>
</template>

<script>
import { RouterLink } from 'vue-router';
    export default {
        name:'MainHeader'
        
    }
</script>

<style scoped>
header{
    text-align: center;
    height: 30px;
    padding: 10px;
    /* margin-top: 200px; */
}

</style>