<template>

    <div class="books">

        <div class="post" v-for="post in bookStore.posts" :key="post.id">

            <img class="images" :src="`${post.path_to_photo}`" :alt="`${post.title}`">

            <div class="book_title">

                <h1><RouterLink class="props_book" @click="bookStore.test(post.id)" to='/books/about'>{{ post.title }}</RouterLink></h1>
                <!-- <h1><RouterLink class="props-book" @click="bookStore.prop(post.index)" to='/books/about'>{{ post.title }}</RouterLink></h1> -->
                <p v-if="bookStore.visibility" class="book_content">{{ post.content }}</p>
                <p class="author">Автор: {{ post.author }}</p>
                <p class="date">Дата создания поста: {{ post.time_create }}</p>

                <div class="div-btn">
                    <button class="btn" @click="bookStore.seen(post.id)">Показать</button>
                    <button class="btn" @click="bookStore.noSeen(post.id)">Скрыть</button>
                    <!-- <RouterLink  to='/addBook' @click="bookStore.test(post.id)">Изменить</RouterLink> -->
                </div>

            </div>

        </div>
        
    </div>

</template>

<script>
import AboutComponent from '../components/AboutComponent.vue';
import { RouterLink, RouterView } from 'vue-router'
import { useBookStore } from '../stores/bookStore'
    export default {
    data() {
        return {
            posts: [],
            bookStore: useBookStore()
        };
    },
    async mounted() {
        this.bookStore.book_data_api();
    },
    components: { RouterView, AboutComponent }
}
</script>

<style scoped>
/* Стили общего контейнера */
.books{
padding: 10px;
}


/* Стили для контента */
.post{
  width: auto;
  padding: 10px 15px 10px 15px;
  text-align: justify;
  height: max-content;
  margin-top: 10px;
  background-color: rgba(150, 136, 102, 0.9);
  color: rgb(0, 0, 0);
  display: grid;
  grid-template-columns:200px 1fr;
  column-gap: 50px;
  border-radius: 20px;
  white-space: normal;
}

.images{
    width: 250px;
    height: 300px;
    object-fit: contain;
    border-radius: 22%;
}

.book_title{
    display: flexbox;
    align-items: center;
    margin-bottom: 10px;
    font-weight: 500;
    width: 100%;
    height: auto;
}
.props_book{
    text-decoration: none;
    color: #e2dc88;
}

.props_book:hover{
    opacity: 0.8;
    color: #c9c6a4;
    transition: 0.5s;
}
.book_content{
    font-size: 20px;
    text-align: justify;
    font-family: sans-serif;
}

.author{
    font-size: 18 px;
    font-weight: bold;
}

.date{
    font-size: 18 px;
    font-weight: bold; 
}


/* Стили для кнопок */
.div-btn{
    display: flex;
    align-items: center;
    justify-content: center;
}

.btn{
    border: none;
    width: 100px;
    height: 40px;
    font-size: 20px;
    border-radius: 10px;
    cursor: pointer;
    margin: 0 10px;
}
.btn:hover {
    opacity: 0.8;
    background-color: rgb(243, 236, 132);
    transition: 0.5s;
}

</style>