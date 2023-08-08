import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBookStore = defineStore('book', {
  state: () => ({
    posts:[],
    posts_filter:[]
  }),
  actions:{
    async book_data_api(){
        const data = await fetch('http://127.0.0.1:8000/api/book/v1')
        const data2 = await data.json()
        this.posts = data2.reverse()
        console.log(data2)
    },
    seen(el){
      this.posts[el].visibility = true
      // console.log(this.posts[el].title)
      // console.log(this.posts)
    },
    noSeen(el){
      this.posts[el].visibility = false
      // console.log(this.posts[el].title)
      // console.log(this.posts)
    },
    prop(index){
      this.posts_filter = this.posts.filter(el => el.index == index)
    }
  }
})