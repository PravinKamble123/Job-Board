<script setup>
//query

let queryRef = ref('')
let query = ''

function performSearch() {
  queryRef.value =query
}

//categories

let { data: jobCategories } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/categories/')
let selectedCategoriesRef = ref('')
let selectedCategories = []

function toggleCategory(id){
  const index = selectedCategories.indexOf(id)
  if( index === -1){
    selectedCategories.push(id)
  }else{
    selectedCategories.splice(index, 1)
    
  }

  console.log('toggleCategory',selectedCategories.join(','))

  selectedCategoriesRef.value = selectedCategories.join(',')
  
}

let {data: jobs } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/',{
  query:{query: queryRef, categories: selectedCategoriesRef }
})
</script>
<template>
    <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
      <div class="md:col-span-1 px-6 py-6 bg-teal-700 rounded-xl">
        <div class="flex items-center justify-between">
          <input
            type="search"
            v-model="query"
            placeholder="Find a job..."
            class="w-full px-6 py-4 rounded-xl bg-white text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-teal-700 focus:border-transparent"
          />
          <button 
           class="px-4 py-2 bg-teal-900 text-white rounded-xl hover:bg-teal-800 focus:outline-none focus:ring-2 focus:ring-teal-700 focus:ring-opacity-50"
           v-on:click="performSearch"
           >
           
            
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21 21l-5.2-5.2a7.5 7.5 0 1 0-2.3 2.3L21 21zM10 15a5 5 0 1 1 0-10 5 5 0 0 1 0 10z"
              />
            </svg>
          </button>
        </div>
        <hr class="my-6 opacity-30">
        <h3 class="mt-6 text-xl text-white">Categories</h3>
        <div class="mt-4 space-y-6">
          <p v-for="category in jobCategories"
             v-bind:key="category.id"
             v-on:click="toggleCategory(category.id)"
             class="py-4 px-4 text-white rounded-xl"
             v-bind:class="{'bg-teal-900': selectedCategoriesRef.includes(category.id)}"
          > {{ category.title }}
        </p>
        </div>
      </div>
      
    </div>
    <div class="grid gap-3 py-4 px-4">
      <Job
      v-for="job in jobs"
      v-bind:key="job.id"
      v-bind:job="job"
      />
    </div>
    
  </template>
  