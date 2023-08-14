<template>

        <div class="image">
            <img  :src="`${post.path_to_photo}`" :alt="`${post.title}`">
        </div>

        <div class="content">
            <p id="title">{{ post.title }}</p>
            <p>{{ post.content }}</p>
        </div>


        <div v-if="seen">

            <form class="f_inp" @submit.prevent >

                <label>
                    <p>Назавние: </p>
                    <input type="text" v-model="post.title">
                </label>

                <label>
                    <p>Описание: </p>
                    <textarea v-model="post.content" cols="auto" rows="auto"></textarea>
                </label>

                <label>
                    <p>Автор: </p>
                    <input type="text" v-model="post.author">
                </label>

                <label>
                    <p>Ссылка на фото: </p>
                    <input type="text" v-model="post.path_to_photo">
                </label>

                <label>
                    <p>Жанр книги:</p>
                    <select v-model="post.cat" class="sele">
                        <option disabled value="">Please select one</option>
                        <option value="1">Фэнтези</option>
                        <option value="2">Детектив</option>
                    </select>
                </label>
                <!-- <label>
                    <p>Жанр книги: </p>
                    <input type="" v-model="post.cat">
                </label>  -->
       
                
                <div class='div_btn'><button class="btn" @click="tes(post.id)">Добавить</button></div>
            
            </form>

        </div>

        <div class="s">
            <label>Внести изменения: </label>
            <input type="checkbox" v-model="seen">
            <label>{{ seen }}</label>
        </div>

</template>

<script>
import { useBookStore } from '../stores/bookStore';
    export default {
        data(){
            return{
                bookStore: useBookStore(),
                seen: false,
            }
        },
        props:{
            post:{
                type:Object,
            },
        },
        methods:{
            async tes(id){
                await fetch(`http://127.0.0.1:8000/api/book/${id}/`, {
                method: "PUT",
                headers: {'Content-Type': 'application/json;charset=utf-8'},
                body: JSON.stringify(this.post)
            })
        }
    }  
}
</script>

<style scoped>
/* Стили для фото */
.image{
    padding: 20px;
    width: 100%;
    text-align: center;
}

/* Стили для контента */
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

/* Стили для формы*/

 .f_inp{
    display: grid;
    text-align: center;
}

label{
    padding-top: 20px;
}

label>input{
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

textarea{
    background-color: rgba(189, 142, 142, 0.9);
    border-radius: 10px;
    width: 100%;
    min-width: 200px;
    max-width: 500px;
    font-size: 18px;
    text-align: justify;
    padding: 10px;
    border: 2px solid grey;
    margin: auto;
    overflow: auto;
}

.f_inp>label>p{
    color: white;
    font-family: sans-serif;
    font-size: 30px;
}

/* Стили для выпадающего списка */
.sele{
    background-color: rgba(189, 142, 142, 0.9);
    border-radius: 10px;
    width: 100%;
    min-width: 200px;
    max-width: 500px;
    height: auto;
    text-align: center;
    font-size: 18px;
    padding: 10px;
}

/* Стили для кнопки */
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

/* Стили для Вывода формы для PUT запроса*/
.s{
    width: 100;
    text-align: center;
    margin-top: 30px;
    font-size: 25px;
}

.s>input{
    width: 15px;
    height: 15px;
}
</style>