<script setup>

import {ref} from "vue";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import {base64ToFile} from "@/js/utils/base64ToFile.js";
import Photo from "@/views/user/profile/components/Photo.vue";
import Username from "@/views/user/profile/components/Username.vue";
import Profile from "@/views/user/profile/components/Profile.vue";

const user = useUserStore()

const photoRef = ref(null)
const usernameRef = ref(null)
const profileRef = ref(null)
const errorMessage = ref('')

async function handleUpdate() {
  errorMessage.value = ''

  const photo = photoRef.value.myPhoto
  const username = usernameRef.value.myUserName.trim()
  const profile = profileRef.value.myProfile.trim()

  if (!photo) {
    errorMessage.value = '头像不能为空'
    return
  }
  if (!username) {
    errorMessage.value = '用户名不能为空'
    return
  }
  if (!profile) {
    errorMessage.value = '简介不能为空'
    return
  }

  try {
    const formData = new FormData()
    formData.append('username', username)
    formData.append('profile', profile)

    if (photo !== user.photo) {
      const photoFile = base64ToFile(photo, 'avatar.png')
      formData.append('photo', photoFile)
    }

    const res = await api.post('/api/user/profile/update/', formData)
    const data = res.data
    if (data.result === 'success') {
      user.setUserInfo(data)
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
        <h3 class="text-lg font-bold my-4">编辑资料</h3>
        <Photo ref="photoRef" :photo="user.photo" />
        <Username ref="usernameRef" :user-name="user.username" />
        <Profile ref="profileRef" :profile="user.profile" />
        <p v-if="errorMessage" class="text-sm text-red-500 mt-1">{{ errorMessage }}</p>
        <div class="flex justify-center">
          <button class="btn btn-neutral w-60 mt-2" @click="handleUpdate">更新</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
