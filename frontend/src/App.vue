<script setup>

import NavBar from "@/components/navbar/NavBar.vue";
import {onMounted} from "vue";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import axios from "axios";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const route = useRoute()
const router = useRouter()

onMounted(async () => {
  try {
    // 第1步：主动刷新 access token（通过 Cookie 中的 refresh_token）
    const refreshRes = await axios.post(
      '/api/user/account/refresh_token/',
      {},
      { withCredentials: true }
    )
    if (refreshRes.data.result === 'success') {
      user.setAccessToken(refreshRes.data.access)

      // 第2步：用新的 access token 拉取用户信息
      const res = await api.get('/api/user/account/get_user_info/')
      const data = res.data
      if (data.result === 'success') {
        user.setUserInfo(data)
      }
    }
  } catch (err) {
    // refresh_token 失败 → 用户确实未登录，不需处理
    console.log('未登录或登录已过期')
  } finally {
    user.setHasPulledUserInfo(true)
    if (route.meta.needLogin && !user.isLogin()) {
      await router.replace({ name: 'user-account-login-index' })
    }
  }
})
</script>

<template>
<NavBar>
  <RouterView/>
</NavBar>
</template>

<style scoped>

</style>
