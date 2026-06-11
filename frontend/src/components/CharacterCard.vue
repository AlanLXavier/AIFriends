<script setup>

defineProps(['character'])

</script>

<template>
  <div class="card bg-base-200 shadow-sm">
    <figure>
      <img :src="character.photo" :alt="character.name" class="w-full h-40 object-cover" />
    </figure>
    <div class="card-body p-3">
      <h3 class="card-title text-base">{{ character.name }}</h3>
      <p class="text-sm text-gray-500 line-clamp-2">{{ character.profile }}</p>
    </div>
  </div>
</template>

<style scoped>

</style>
