<script setup>

import {ref, watch} from "vue";

const props = defineProps(['userName'])
const myUserName = ref(props.userName)

watch(() => props.userName, (newVal) => {
  myUserName.value = newVal
})

defineExpose({ myUserName })

</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">用户名</label>
    <input
      v-model="myUserName"
      type="text"
      class="input w-108"
      placeholder="用户名"
    />
  </fieldset>
</template>

<style scoped>

</style>
