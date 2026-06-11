<script setup>
import Photo from "@/views/create/character/components/Photo.vue";
import Name from "@/views/create/character/components/Name.vue";
import Profile from "@/views/create/character/components/Profile.vue";
import BackgroundImage from "@/views/create/character/components/BackgroundImage.vue";
import {onMounted, ref} from "vue";
import {base64ToFile} from "@/js/utils/base64ToFile.js";
import api from "@/js/http/api.js";
import {useRoute, useRouter} from "vue-router";
import {useUserStore} from "@/stores/user.js";

const user = useUserStore()
const router = useRouter()
const route = useRoute()
const characterId = route.params.character_id
const character = ref(null)

onMounted(async () => {
  try {
    const res = await api.get('/api/create/character/get_single/', {
      params: {
        character_id: characterId,
      }
    })
    const data = res.data
    if (data.result === 'success') {
      character.value = data
    }
  } catch (err) {
    console.log(err)
    character.value = null
  }
})

const photoRef = ref(null)
const nameRef = ref(null)
const profileRef = ref(null)
const bgRef = ref(null)
const errorMessage = ref('')

async function handleUpdate() {
  const photo = photoRef.value.myPhoto
  const name = nameRef.value.myName?.trim()
  const profile = profileRef.value.myProfile?.trim()
  const backgroundImage = bgRef.value.myBackgroundImage

  errorMessage.value = ''
  if (!photo) {
    errorMessage.value = '头像不能为空'
  } else if (!name) {
    errorMessage.value = '名字不能为空'
  } else if (!profile) {
    errorMessage.value = '角色介绍不能为空'
  } else if (!backgroundImage) {
    errorMessage.value = '聊天背景不能为空'
  } else {
    const formData = new FormData()
    formData.append('character_id', characterId)
    formData.append('name', name)
    formData.append('profile', profile)

    if (photo !== character.value.photo) {
      formData.append('photo', base64ToFile(photo, 'photo.png'))
    }

    if (backgroundImage !== character.value.background) {
      formData.append('background', base64ToFile(backgroundImage, 'background_image.png'))
    }

    try {
      const res = await api.post('/api/create/character/update/', formData)
      const data = res.data
      if (data.result === 'success') {
        await router.push({
          name: 'user-space-index',
          params: {
            user_id: user.id,
          }
        })
      } else {
        errorMessage.value = data.result
      }
    } catch (err) {
      console.log(err)
      errorMessage.value = '网络异常，请稍后重试'
    }
  }
}
</script>

<template>
  <div v-if="character" class="flex justify-center">
    <div class="card w-120 bg-base-200 shadow-sm mt-16">
      <div class="card-body">
        <h3 class="text-lg font-bold my-4">更新角色</h3>
        <Photo ref="photoRef" :photo="character.photo" />
        <Name ref="nameRef" :name="character.name" />
        <Profile ref="profileRef" :profile="character.profile" />
        <BackgroundImage ref="bgRef" :background-image="character.background" />

        <p v-if="errorMessage" class="text-sm text-red-500">{{ errorMessage }}</p>

        <div class="flex justify-center">
          <button @click="handleUpdate" class="btn btn-neutral w-60 mt-2">更新</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>

