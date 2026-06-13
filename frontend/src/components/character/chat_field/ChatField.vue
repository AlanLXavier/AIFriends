<script setup>

import {computed, ref} from "vue";
import InputField from "@/components/character/chat_field/input_field/InputField.vue";
import CharacterPhotoField from "@/components/character/chat_field/character_photo_field/CharacterPhotoField.vue";

const props = defineProps(['friend'])
const modalRef = ref(null)

const modalStyle = computed(() => {
  if (!props.friend) return {}
  return {
    backgroundImage: `url(${props.friend.character.background})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  }
})

function showModal() {
  modalRef.value.showModal()
}

defineExpose({ showModal })

</script>

<template>
  <dialog ref="modalRef" class="modal">
    <div class="modal-box w-90 h-150" :style="modalStyle">
      <button class="btn btn-sm btn-circle btn-ghost bg-transparent absolute right-2 top-2"
              @click="modalRef.close()">✕</button>
      <div v-if="friend" class="flex flex-col h-full">
        <CharacterPhotoField :character="friend.character" />
        <div class="flex-1"></div>
        <InputField />
      </div>
    </div>
  </dialog>
</template>

<style scoped>

</style>
