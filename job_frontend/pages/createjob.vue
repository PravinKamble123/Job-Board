<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()

async function submitForm() {
    console.log('Submit form')
    errors.value = []

    if(category.value == ''){ errors.value.push('You must select a category')}
    if(title.value == ''){ errors.value.push('The title field is missing')}
    if(description.value == ''){ errors.value.push('The description  field is missing')}
    if(position_salary.value == ''){ errors.value.push('The position salary field is missing')}
    if(position_location.value == ''){ errors.value.push('The position location field is missing')}
    if(company_name.value == ''){ errors.value.push('The Company name field is missing')}
    if(company_location.value == ''){ errors.value.push('The Company location field is missing')}
    if(company_email.value == ''){ errors.value.push('The Company email field is missing')}

    if (errors.value.length == 0){
        await $fetch('http://localhost:8000/api/v1/jobs/create/',{
            headers:{
                    'Authorization':'token ' + userStore.user.token,
                    'content-type':'application/json' 
                },
            method: 'POST',
            body: {
                category: category.value,
                title: title.value,
                description: description.value,
                position_salary: position_salary.value,
                position_location:position_location.value,
                company_name: company_name.value,
                company_location: company_location.value,
                company_email: company_email.value
            }
        }).then(response => {
            console.log('response',response)
            
            router.push({path:'/myjobs'})
        })
        .catch(error => {
            if(error.response){
                for(const property in error.response_data){
                    errors.value.push(`${property}: ${error.response_data[property]}`)
                }
            }else if( error.message){
                errors.value.push('Something went wrong , Please try again')

                console.log(JSON.stringify(error))
            }
        })
    }
}

onMounted( () => {

    if(!userStore.user.isAuthenticated) {
        router.push('/login')
    }

})

let { data: jobCategories } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/categories/')

let category = ref('')
let title = ref('')
let description = ref('')
let position_salary = ref('')
let position_location = ref('')
let company_name = ref('')
let company_location = ref('')
let company_email = ref('')
let errors = ref([])
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-xl">
            Create job
        </h1>
        <form v-on:submit.prevent="submitForm" class="space-y-4">
            <div>
                <label>Category</label>
                <select v-model="category" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
                    <option
                    v-for="category in jobCategories"
                    :key="category.id"
                    
                     :value="category.id">{{ category.title }}</option>
                   
                </select>
            </div>
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
            <button class="py-4 px-6  bg-teal-700 text-white rounded-xl">Submit</button>
        </form>
    </div>
</template>