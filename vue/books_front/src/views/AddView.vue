<template>
    <div>
        <form @submit.prevent>
            <!-- <input type="text" v-model="title">
            <input type="text" v-model="content">
            <input type="text" v-model="author">
            <input type="text" v-model="path_to_photo">
            <input type="text" v-model="the_year_of_publishing">
            <input type="text" v-model="cat"> -->
            <button @click="addPost(add)">Добавить</button>
        </form>

    </div>
</template>

<script>
    export default {
        data(){
            return{
                add:{
                    title: "Игра престолов",
                    content: "Перед вами — величественное шестикнижие «Песнь льда и огня». Эпическая, чеканная сага о мире Семи Королевств. О мире суровых земель вечного холода и радостных земель вечного лета. Мире лордов и героев, воинов и магов, чернокнижников и убийц — всех, кого свела воедино Судьба во исполнение древнего пророчества. О мире опасных приключений, великих деяний и тончайших политических интриг.",
                    author: "Джордж Р. Р. Мартин",
                    path_to_photo: "https://cdn.img-gorod.ru/310x500/nomenclature/21/111/2111187.jpg",
                    the_year_of_publishing: "06.08.1996",
                    time_create: "2023-08-05T07:59:37.139993Z",
                    time_update: "2023-09-11",
                    visibility: true,
                    index: 3,
                    pk: 4,
                    id: 4,
                    cat: 1
                }
            }
        },
        methods:{
             async addPost(){
                await fetch('http://127.0.0.1:8000/api/book/v1/', {
                method: "POST",
                headers: {'Content-Type': 'application/json;charset=utf-8'},
                body: JSON.stringify(this.add)
            }).then(response => {
                console.log(response.json())
            })
        }
    }
}
</script>

<style scoped>

</style>