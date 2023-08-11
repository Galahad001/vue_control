<template>

    <header>
        <nav>
            <RouterLink to="/" class="sr">Home</RouterLink> -
            <RouterLink to="/books" class="sr">Books</RouterLink> -
            <RouterLink to="/addBook" class="sr">addBook</RouterLink>
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
    align-items: center;
    justify-content: center;
    height: 30px;
    padding: 10px;
    margin: auto;
    text-align: center;
    font-size: 30px;
    color: blanchedalmond;
    font-weight: bold;
    /* margin-top: 200px; */
}

nav{
    border: 1px solid black;
    background-color: rgba(73, 68, 62, 0.8);
    border-radius: 10px;
}

.sr{
    text-decoration: none;
    color: blanchedalmond;
}

.sr:hover{
    opacity: 0.8;
    color: rgb(223, 187, 144);
    transition: 0.5s;
}

</style>