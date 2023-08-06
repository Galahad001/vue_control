<template>
        <div class="post" v-for="post in posts" :key="post.id">
            <h1>{{ post.title }}</h1>
            <p v-if="seen">{{ post.content }}</p>
            <p>{{ post.author }}</p>
            <p>{{ post.time_create }}</p>
            <button @click="seenFunc">Скрыть</button>
        </div>
</template>

<script>
    export default {
        data () {    // Переменные
            return {
                posts: [ ],
                seen:true
            }
        },
        async mounted() { // Компонент монтирован
            const data = await fetch('http://127.0.0.1:8000/api/book/v1')
            this.posts = await data.json()
        },
        methods:{
            seenFunc(){
                    this.seen = !this.seen
            }
        }
    }
</script>

<style scoped>
.post{
  width: 100%;
  padding: 5px 15px 5px 10px;
  text-align: justify;
  height: max-content;
  margin-top: 10px;
  background-color: rgb(179, 130, 58);
  color: rgb(0, 0, 0);
}

</style>