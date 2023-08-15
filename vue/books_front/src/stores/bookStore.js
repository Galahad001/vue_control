import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBookStore = defineStore('book', {

  state: () => ({
    posts:[],
    post_pk:[],
    posts_filter:[],
    visibility: true
  }),

  actions:{
    async book_data_api(){
        const data = await fetch('http://127.0.0.1:8000/api/book/v1/')
        const data2 = await data.json()
        this.posts = data2.reverse()
        console.log(data2)
    },
    async test(id){
      const data = await fetch(`http://127.0.0.1:8000/api/book/${id}/`)
      const data2 = await data.json()
      this.post_pk = data2
      console.log(this.post_pk)
    },

    seen(id){
      const i = this.posts.findIndex(n => n.id == id)
    },

    noSeen(id){
      for(i=0; i < this.posts.length; i++){
        if(id == this.posts[i].id){
          this.visibility = false
        }
      }

    },

    delete: async function(id){
        await fetch(`http://127.0.0.1:8000/api/book/${id}/`, {method: "DELETE"})

        const i = this.posts.findIndex(n => n.id == id)
        this.posts.splice(i, 1)
    },

    testos(id){
      // this.posts.filter(el => el.cat == id)
      console.log('OK')
    },

    addBook(id){
      this.test(id)
    }

  }
})