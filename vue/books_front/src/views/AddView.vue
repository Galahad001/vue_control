<template>

        <form class="f_inp" @submit.prevent >

            <label>
                <p>Назавние: </p>
                <input type="text" v-model="title">
            </label>
            
            <label>
                <p>Описание: </p>
                <textarea v-model="content" cols="100" rows="10"></textarea>
                <!-- <input type="text" v-model="add.content"> -->
            </label>

            <label>
                <p>Автор: </p>
                <input type="text" v-model="author">
            </label>

            <label>
                <p>Ссылка на фото: </p>
                <input type="text" v-model="path_to_photo">
            </label>

            <label>
                <p>Жанр книги: </p>
                <input type="text" v-model="cat">
            </label> 
       
            <div class='div_btn'><button class="btn" @click="addPost()">Добавить</button></div>

        </form>


</template>

<script>
import { useBookStore } from '../stores/bookStore'
    export default {
        data(){
            return{
                bookStore: useBookStore(),
                title: '',
                content:'',
                author:'',
                path_to_photo:'',
                time_create:'1',
                cat: '1',
                id:'1',
                
            }
        },
        methods:{
             async addPost(){
                await fetch('http://127.0.0.1:8000/api/book/v1/', {
                method: "POST",
                headers: {'Content-Type': 'application/json;charset=utf-8'},
                body: JSON.stringify({title: this.title, content: this.content, author: this.author, path_to_photo: this.path_to_photo, time_create: this.time_create, cat: this.cat, id: this.id})
            })
        },
    }
}
</script>

<style scoped>
/* Стили для формы */
.f_inp{
    display: grid;
    text-align: center;
}

/* Стили для тега label */
label{
    padding-top: 20px;
}

/* Стили для тега input */
input{
    background-color: rgba(189, 142, 142, 0.9);
    border-radius: 10px;
    width: 100%;
    min-width: 200px;
    max-width: 500px;
    height: 20px;
    font-size: 18px;
    text-align: center;
    padding: 10px;
    border: 2px solid grey;
}

/* Стили для тега textarea */
textarea{
    background-color: rgba(189, 142, 142, 0.9);
    border-radius: 10px;
    width: 100%;
    min-width: 200px;
    max-width: 500px;
    height: auto;
    font-size: 18px;
    text-align: justify;
    padding: 10px;
    border: 2px solid grey;
}

/* Стили для всех тегов p в включенных в тег label включеный в элемент с классам  f_inp */
.f_inp>label>p{
    color: white;
    font-family: sans-serif;
    font-size: 30px;
}

/* Стили для кнопок */
.div_btn{
    justify-content: center;
    margin-top: 20px;
}
.btn{
    border: none;
    width: 130px;
    height: 50px;
    font-size: 20px;
    border-radius: 10px;
    padding: 10px;
}

.btn:hover{
    opacity: 0.7;
    color: whitesmoke;
    background-color: rgba(189, 142, 142, 0.9);
    transition: 0.8s;
    cursor: pointer;
}

</style>