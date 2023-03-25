<script setup>
import { useUserStore } from '@/stores/user'

const userStore =  useUserStore()
const router = useRouter()

function logout(){
  userStore.removeToken()

  router.push({path:'/login'})


}

</script>

<template>
    <div class="min-h-screen flex flex-col">
      <!-- Header -->
      <nav class="bg-teal-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="flex items-center justify-between h-16">
            <div class="flex-shrink-0">
              <NuxtLink to="/" class="text-white font-bold text-xl">Djob</NuxtLink>
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <NuxtLink to="/" class="text-white hover:text-teal-300">Home</NuxtLink>
                <NuxtLink to="/" class="text-white hover:text-teal-300">Browse</NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </nav>
      
      <!-- Main content -->
      <div class="flex-1 bg-white py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <slot />
        </div>
      </div>
      
      <!-- Footer -->
      <footer class="bg-gray-800">
        <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center">
          <p class="text-gray-300 text-sm md:text-base">&copy; 2023 - Pravin Kamble</p>
          <div class="flex mt-6 md:mt-0 items-center space-x-4">
            <template v-if="userStore.user.isAuthenticated">
              <NuxtLink to="/myjobs" class="py-2 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-md text-sm md:text-base">My jobs</NuxtLink>
              <NuxtLink to="/createjob" class="py-2 px-4 bg-teal-600 hover:bg-teal-700 text-white rounded-md text-sm md:text-base">Create a job</NuxtLink>
              <a v-on:click="logout"  class="py-2 px-4 bg-rose-600 hover:bg-rose-700 text-white rounded-md text-sm md:text-base">Log out</a>
            </template>
            <template v-else>
              <NuxtLink to="/login" class="py-2 px-4 bg-teal-900 hover:bg-teal-700 text-white rounded-md text-sm md:text-base">Log in</NuxtLink>
              <NuxtLink to="/signup" class="py-2 px-4 bg-teal-600 hover:bg-teal-700 text-white rounded-md text-sm md:text-base">Sign up</NuxtLink>
            </template>
          </div>
        </div>
      </footer>
    </div>
  </template>
  