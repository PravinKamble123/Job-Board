<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()
const emit = defineEmits(['deleteJob'])
const props= defineProps({
    my: {
        type: [Boolean]
    },
    job: {
      type: [Object]
    }
})

async function deleteJob(id){
  await $fetch('http://localhost:8000/api/v1/jobs/' + id + '/delete/',{
            headers:{
                    'Authorization':'token ' + userStore.user.token,
                    'content-type':'application/json' 
                },
            method: 'DELETE',
})
.then(response => {
  console.log('response',response)

  emit('deleteJob',id)
  router.push({path:'/myjobs'})
})
.catch(error => {
  console.log(error)
})
}
</script>
<template>
    <section class="container mx-auto px-6 py-12">
        
  
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
          <!-- Job card -->
          <div class="bg-white rounded-lg overflow-hidden shadow-md hover:shadow-lg">
            <div class="p-6">
              <h3 class="text-xl font-semibold mb-2">{{ job.title }}</h3>
              <p class="text-gray-500 text-sm">{{ job.company_name }}</p>
            </div>
  
            <div class="px-6 py-4 border-t border-gray-200 flex items-center justify-between">
              <div>
                <p class="text-xs uppercase font-semibold mb-1">Company Name</p>
                <p class="text-sm">{{ job.position_location }}</p>
              </div>
  
              <div>
                <p class="text-xs uppercase font-semibold mb-1">Salary</p>
                <p class="text-sm">{{ job.position_salary }}</p>
              </div>
  
              <div>
                <p class="text-xs uppercase font-semibold mb-1">Posted</p>
                <p class="text-sm">{{ job.created_at_formatted }}</p>
              </div>
            </div>
  
            <div class="p-6 space-x-4">
              <NuxtLink v-bind:to="'/browse/' + job.id" class="py-2 px-4 bg-teal-700 rounded-lg text-white text-lg font-semibold hover:bg-teal-600">Details</NuxtLink>
              <NuxtLink v-bind:to="'/editjob/' + job.id" class="py-2 px-4 bg-yellow-700 rounded-lg text-white text-lg font-semibold hover:bg-yellow-600" v-if="my">Edit</NuxtLink>
              <a v-on:click="deleteJob(job.id)" class="py-2 px-4 bg-rose-700 rounded-lg text-white text-lg font-semibold hover:bg-rose-600" v-if="my">Delete</a>
            </div>
          </div>
        </div>
      </section>
</template>