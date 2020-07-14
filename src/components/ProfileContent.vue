<template>
    <div class="Profilecontent">
      
      <div v-if="show">
      
        <div v-if="ind==1" class="post">
          <MyPost/>
        </div>
        <div v-else-if="ind==2" class="follower">
            <MyFollower/>
        </div>
        <div v-else-if="ind==3" class="following">
            <MyFollowing/>
        </div>
      </div>
      <div v-else>
        <h1> private content</h1>
      </div>
    </div>

</template>

<script>


import MyPost from '@/components/MyPost.vue';
import MyFollower from '@/components/MyFollower.vue';
import MyFollowing from '@/components/MyFollowing.vue';


export default {
  components:{
    
    MyPost,
    MyFollower,
    MyFollowing
  },
  
  computed:{
    ind(){
      return this.$store.state.btn
    },
    show(){

      
      if(Object.keys(this.$store.state.ondemand).length==0 ){
        return true
      }
      else{
        
        if(this.$store.state.followunfollow=="unfollower"){
          return true
        }
        else{
          return false
        }
      }
      }
    
  }
  
  
  
  
}
</script>

<style scoped>


.Profilecontent{
    height:63vh;
    margin-left:  auto;
    margin-right: auto;
    width: 70%;
    overflow-y: scroll;
    overflow-x: hidden;

    
    
}
.Profilecontent::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.Profilecontent::-webkit-scrollbar-track {
  background-color: rgba(0, 0, 0, 0.4);
  border-radius: 10px;
}
.Profilecontent::-webkit-scrollbar-thumb {
  background-color: #AD7D52;
  border-radius: 10px;
}


</style>