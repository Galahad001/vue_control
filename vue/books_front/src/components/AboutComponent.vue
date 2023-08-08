<template>

        <div class="image">
            <img  :src="`${post.path_to_photo}`" :alt="`${post.title}`">
        </div>

        <div class="content">
            <p id="title">{{ post.title }}</p>
            <p>{{ post.content }}</p>
        </div>
        
</template>

<script>
    export default {
        props:{
            post:{
                type:Object,
                required:true,
                default:true
            }
        }
    }
</script>

<style scoped>
.image{
    padding: 20px;
    width: 100%;
    text-align: center;
}

    
.content{
    color: rgb(255, 255, 255);
    background-color: rgba(126, 123, 85, 0.9);
    border-radius: 10px;
    padding: 10px;
    margin: 0 20px 0 20px;
}

.content>p{
    font-size: 20px;
    text-align: center;
    font-family: sans-serif;
}

#title{
    font-size: 30px;
    font-weight: bold;
}
</style>