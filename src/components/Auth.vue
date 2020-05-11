<template>
    <div class="auth">
      
        <Login/>
        <SignIn/>

    </div>
</template>


<script>

import Login from '@/components/Login.vue';
import SignIn from '@/components/SignIn.vue';

export default {
    components:{
      Login,
      SignIn
    }
}
</script>


<style scoped>
    .auth{

      display: flex;
      justify-content:center;
      

    }
</style>