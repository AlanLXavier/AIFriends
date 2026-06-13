<script setup>

defineProps(['character'])

</script>

<template>
  <div class="absolute left-2 top-6 bg-black/50 flex items-center gap-2 px-2 h-10 w-fit rounded-full max-w-[calc(100%-22px)]">
    <div class="avatar">
      <div class="w-8 rounded-full">
        <img :src="character.photo" alt="">
      </div>
    </div>
    <div class="text-white text-sm line-clamp-1 break-all">{{ character.name }}</div>
  </div>
</template>

<style scoped>

</style>
