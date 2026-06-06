<script setup>

import {ref, watch, nextTick, onBeforeUnmount} from "vue";
import Croppie from "croppie";
import "croppie/croppie.css";

const props = defineProps(['photo'])
const myPhoto = ref(props.photo)
const fileInputRef = ref(null)
const modalRef = ref(null)
const croppieRef = ref(null)

watch(() => props.photo, (newValue) => {
  myPhoto.value = newValue
})

defineExpose({ myPhoto })

function selectImage() {
  fileInputRef.value.click()
}

let croppie = null

function onFileChange(e) {
  const file = e.target.files[0]
  e.target.value = ''

  if (!file) return

  const reader = new FileReader()
  reader.onload = () => {
    openModal(reader.result)
  }
  reader.readAsDataURL(file)
}

async function openModal(photoUrl) {
  modalRef.value.showModal()
  await nextTick()

  if (!croppie) {
    croppie = new Croppie(croppieRef.value, {
      viewport: {width: 200, height: 200, type: 'square'},
      boundary: {width: 300, height: 300},
      enableOrientation: true,
      enforceBoundary: true,
    })
  }

  croppie.bind({url: photoUrl})
}

async function crop() {
  if (!croppie) return

  myPhoto.value = await croppie.result({
    type: 'base64',
    size: 'viewport',
  })
  modalRef.value.close()
}

onBeforeUnmount(() => {
  croppie?.destroy()
})

</script>

<template>
  <div class="flex justify-center my-6">
    <div class="avatar relative">
      <div v-if="myPhoto" class="w-28 rounded-full">
        <img :src="myPhoto" alt="" />
      </div>
      <div v-else class="w-28 h-28 rounded-full bg-base-300"></div>

      <div
        class="absolute left-0 top-0 w-28 h-28
               flex justify-center items-center
               bg-black/20 rounded-full cursor-pointer"
        @click="selectImage"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="1.5">
          <path d="M4 6m0 2a2 2 0 0 1 2 -2h1.172a2 2 0 0 0 1.414 -.586l.828 -.828a2 2 0 0 1 1.414 -.586h2.344a2 2 0 0 1 1.414 .586l.828 .828a2 2 0 0 0 1.414 .586h1.172a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2z"></path>
          <circle cx="12" cy="13" r="3"></circle>
        </svg>
      </div>
    </div>

    <input type="file" ref="fileInputRef"
           class="hidden" accept="image/*"
           @change="onFileChange" />
  </div>

  <dialog ref="modalRef" class="modal">
    <div class="modal-box" style="transition: none">
      <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2"
              @click="modalRef.close()">✕</button>

      <div ref="croppieRef" class="flex flex-col justify-center my-4"></div>

      <div class="modal-action">
        <button class="btn" @click="modalRef.close()">取消</button>
        <button class="btn btn-neutral" @click="crop">确定</button>
      </div>
    </div>
  </dialog>
</template>

<style scoped>

</style>
