<script setup>

import {ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import {base64ToFile} from "@/js/utils/base64ToFile.js";
import Photo from "@/views/create/character/components/Photo.vue";
import Name from "@/views/create/character/components/Name.vue";
import Profile from "@/views/create/character/components/Profile.vue";
import BackgroundImage from "@/views/create/character/components/BackgroundImage.vue";

const router = useRouter()
const user = useUserStore()

const photoRef = ref(null)
const nameRef = ref(null)
const profileRef = ref(null)
const backgroundImageRef = ref(null)
const errorMessage = ref('')

async function handleCreate() {
  errorMessage.value = ''

  const photo = photoRef.value.myPhoto
  const name = nameRef.value.myName?.trim()
  const profile = profileRef.value.myProfile?.trim()
  const backgroundImage = backgroundImageRef.value.myBackgroundImage

  if (!photo) {
    errorMessage.value = '头像不能为空'
    return
  }
  if (!name) {
    errorMessage.value = '名字不能为空'
    return
  }
  if (!profile) {
    errorMessage.value = '角色介绍不能为空'
    return
  }
  if (!backgroundImage) {
    errorMessage.value = '聊天背景不能为空'
    return
  }

  try {
    const formData = new FormData()
    formData.append('name', name)
    formData.append('profile', profile)
    formData.append('photo', base64ToFile(photo, 'avatar.png'))
    formData.append('background', base64ToFile(backgroundImage, 'bg.png'))

    const res = await api.post('/api/character/create/', formData)
    const data = res.data
    if (data.result === 'success') {
      await router.push({
        name: 'user-space-index',
        params: {user_id: user.id}
      })
    } else {
      errorMessage.value = data.result
    }
  } catch (err) {
    console.log(err)
  }
}

</script>

<template>
  <div class="flex justify-center">
    <div class="card w-120 bg-base-200 shadow-sm mt-16">
      <div class="card-body">
        <h3 class="text-lg font-bold my-4">创建角色</h3>
        <Photo ref="photoRef" />
        <Name ref="nameRef" />
        <Profile ref="profileRef" />
        <BackgroundImage ref="backgroundImageRef" />
        <p v-if="errorMessage" class="text-sm text-red-500 mt-1">{{ errorMessage }}</p>
        <div class="flex justify-center">
          <button class="btn btn-neutral w-60 mt-2" @click="handleCreate">创建</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
