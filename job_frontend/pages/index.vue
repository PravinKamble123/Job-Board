<script setup>
const { data: jobs } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/newest/')

</script>
<template>
    <div class="bg-gray-100">
      <!-- Header section -->
      <header class="bg-teal-700 text-white py-6">
        <div class="container mx-auto px-6 flex items-center justify-between">
          <h1 class="text-4xl font-bold">Find a Job Anywhere</h1>
          <NuxtLink to="/browse" class="py-2 px-4 bg-teal-900 rounded-lg text-white text-lg font-semibold hover:bg-teal-800">Browse Jobs</NuxtLink>
        </div>
      </header>
  
      <!-- Jobs section -->
      <job v-for="job in jobs"
       v-bind:key="job.id"
       v-bind:job="job"/>
    </div>
  </template>
  