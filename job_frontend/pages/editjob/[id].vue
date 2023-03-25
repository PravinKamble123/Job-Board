<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'


const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

onMounted( () => {
  if(!userStore.user.isAuthenticated){
    router.push('/login')
  }
})
const {data: job} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/' + route.params.id + '/')


let title = ref(job.value.title)
let description = ref(job.value.description)
let position_salary = ref(job.value.position_salary)
let position_location = ref(job.value.position_location)
let company_name = ref(job.value.company_name)
let company_location = ref(job.value.company_location)
let company_email = ref(job.value.company_email)
let errors = ref([])

async function submitForm() {
  console.log('Submit form')
  errors.value = []

  if (title.value == '') {
    errors.value.push('The title field is missing')
  }
  if (description.value == '') {
    errors.value.push('The description field is missing')
  }
  if (position_salary.value == '') {
    errors.value.push('The position salary field is missing')
  }
  if (position_location.value == '') {
    errors.value.push('The position location field is missing')
  }
  if (company_name.value == '') {
    errors.value.push('The Company name field is missing')
  }
  if (company_location.value == '') {
    errors.value.push('The Company location field is missing')
  }
  if (company_email.value == '') {
    errors.value.push('The Company email field is missing')
  }

  if (errors.value.length == 0) {
    const data = {
      category: job.category,
      title: title.value,
      description: description.value,
      position_salary: position_salary.value,
      position_location: position_location.value,
      company_name: company_name.value,
      company_location: company_location.value,
      company_email: company_email.value
    }

    await $fetch(`http://localhost:8000/api/v1/jobs/${route.params.id}/edit/`, {
      method: 'PUT',
      headers: {
        'Authorization': 'token ' + userStore.user.token,
        'content-type': 'application/json'
      },
      body: JSON.stringify(data)
    }).then(response => {
      console.log('response', response)

      router.push({path:'/myjobs'})
    })
    .catch(error => {
      if (error.response) {
        for (const property in error.response_data) {
          errors.value.push(`${property}: ${error.response_data[property]}`)
        }
      } else if (error.message) {
        errors.value.push('Something went wrong, please try again')

        console.log(JSON.stringify(error))
      }
    })
  }
}


</script>


<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-xl">
            Edit Job
        </h1>
        <form v-on:submit.prevent="submitForm" class="space-y-4">
            
            <div>
                <label>Title</label>
                <input v-model="title" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div>
                <label>Description</label>
                <textarea v-model="description" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100"></textarea>
            </div>
            <div>
                <label>Salary</label>
                <input v-model="position_salary" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div>
                <label>Job Location</label>
                <input v-model="position_location" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div>
                <label>Company Name</label>
                <input v-model="company_name" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div>
                <label>Company Location</label>
                <input v-model="company_location" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div>
                <label>Company Email</label>
                <input v-model="company_email" type="email" placeholder="Company email address..." class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>
            <div 
                v-if="errors.length"
                class="mb-6 py-4 px-6 bg-rose-400 rounded-xl text-white"
                >
                <p
                v-for="error in errors" v-bind:key="error"
                >{{ error }}
                </p>
            </div>
            <button class="py-4 px-6  bg-teal-700 text-white rounded-xl">Save Changes</button>
        </form>
    </div>
</template>