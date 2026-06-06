<script setup>

import {ref, watch, nextTick, onBeforeUnmount} from "vue";
import Croppie from "croppie";
import "croppie/croppie.css";

const props = defineProps(['backgroundImage'])
const myBackgroundImage = ref(props.backgroundImage)
const fileInputRef = ref(null)
const modalRef = ref(null)
const croppieRef = ref(null)

watch(() => props.backgroundImage, (newValue) => {
  myBackgroundImage.value = newValue
})

defineExpose({ myBackgroundImage })

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
      viewport: {width: 300, height: 500},
      boundary: {width: 600, height: 600},
      enableOrientation: true,
      enforceBoundary: true,
    })
  }

  croppie.bind({url: photoUrl})
}

async function crop() {
  if (!croppie) return

  myBackgroundImage.value = await croppie.result({
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
  <fieldset class="fieldset">
    <label class="label text-base">聊天背景</label>

    <div class="avatar relative">
      <div v-if="myBackgroundImage" class="w-15 h-25 rounded-box">
        <img :src="myBackgroundImage" alt="" />
      </div>
      <div v-else class="w-15 h-25 rounded-box bg-base-300"></div>

      <div
        class="absolute left-0 top-0 w-15 h-25
               flex justify-center items-center
               bg-black/20 rounded-box cursor-pointer"
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
  </fieldset>

  <dialog ref="modalRef" class="modal">
    <div class="modal-box max-w-2xl" style="transition: none">
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
