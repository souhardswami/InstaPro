<template>
    <div class="logout">
        <button class="button" @click="logout">LogOut</button>
    </div>
</template>

<script>
export default {
    methods:{
        logout(){
            console.log("t")
            this.$store.commit('set_user',[]),
            this.$store.commit('set_auth',-1)
        }
    }
}
</script>


<style scoped>

.button {
  
  border: none;
  color: black;
  padding: 15px 32px;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>