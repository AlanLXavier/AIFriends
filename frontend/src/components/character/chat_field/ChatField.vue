<script setup>

import {computed, nextTick, ref} from "vue";
import InputField from "@/components/character/chat_field/input_field/InputField.vue";
import CharacterPhotoField from "@/components/character/chat_field/character_photo_field/CharacterPhotoField.vue";
import ChatHistory from "@/components/character/chat_field/chat_history/ChatHistory.vue";

const props = defineProps(['friend'])
const modalRef = ref(null)
const inputRef = ref(null)
const chatHistoryRef = ref(null)
const history = ref([])

const modalStyle = computed(() => {
  if (!props.friend) return {}
  return {
    backgroundImage: `url(${props.friend.character.background})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  }
})

function handlePushBackMessage(msg) {
  history.value.push(msg)
  chatHistoryRef.value.scrollToBottom()
}

function handleAddToLastMessage(delta) {
  history.value.at(-1).content += delta
  chatHistoryRef.value.scrollToBottom()
}

function handlePushFrontMessage(msg) {
  history.value.unshift(msg)
}

async function showModal() {
  modalRef.value.showModal()
  await nextTick()
  inputRef.value.focus()
}

function handleClose() {
  inputRef.value.close()
}

defineExpose({ showModal })

</script>

<template>
  <dialog ref="modalRef" class="modal" @close="handleClose">
    <div class="modal-box w-90 h-150" :style="modalStyle">
      <button class="btn btn-sm btn-circle btn-ghost bg-transparent absolute left-2 top-2"
              @click="modalRef.close()">✕</button>
      <div v-if="friend" class="flex flex-col h-full">
        <CharacterPhotoField :character="friend.character" />
        <ChatHistory
          ref="chatHistoryRef"
          :history="history"
          :friendId="friend.id"
          :character="friend.character"
          @pushFrontMessage="handlePushFrontMessage"
        />
        <InputField
          ref="inputRef"
          :friendId="friend.id"
          @pushBackMessage="handlePushBackMessage"
          @addToLastMessage="handleAddToLastMessage"
        />
      </div>
    </div>
  </dialog>
</template>

<style scoped>

</style>
