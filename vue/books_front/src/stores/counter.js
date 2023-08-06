import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBookStore = defineStore('book', {
  state: () => ({
    test:0
  }),
  actions:{
    d(){
      this.test++
    }
  }
})