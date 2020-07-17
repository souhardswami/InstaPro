<template>
    <div class="auth">
      <div v-if="active">
      
        <Login/>
        <SignIn/>
      </div>
      <div v-else>
        <logout/>
      </div>

    </div>
</template>


<script>

import Login from '@/components/Login.vue';
import SignIn from '@/components/SignIn.vue';
import Logout from '@/components/Logout.vue';

export default {

    components:{
      Login,
      SignIn,
      Logout
    },
    computed:{
      active(){
        return  this.$store.state.auth==-1 ? true :false
      }
    }
}
</script>


<style scoped>
    .auth div{

      display: flex;
      justify-content:center;
      

    }
</style>