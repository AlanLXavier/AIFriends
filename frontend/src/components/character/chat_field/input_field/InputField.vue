<script setup>

</script>

<template>
  <div class="absolute bottom-4 left-2 h-12 w-86 flex items-center">
    <input
      type="text"
      class="input bg-black/30 text-white text-base backdrop-blur-sm w-full h-full rounded-2xl mr-20"
      placeholder="文本输入"
    />
    <div class="absolute right-2 w-8 h-8 flex justify-center items-center cursor-pointer rounded-full hover:bg-white/10">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           class="w-4 h-4 text-white">
        <path d="M22 2L11 13" />
        <path d="M22 2l-7 20-4-9-9-4 20-7z" />
      </svg>
    </div>
    <div class="absolute right-8 w-8 h-8 flex justify-center items-center cursor-pointer rounded-full hover:bg-white/10">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           class="w-4 h-4 text-white">
        <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
        <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
        <path d="M12 19v3" />
      </svg>
    </div>
  </div>
</template>

<style scoped>

</style>
