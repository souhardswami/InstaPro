<template>
    <div class="postview">

        
        

        
            <div class="left">
   
                
                
                <img :src="'http://localhost:8000'+currentImg" >
                
            </div>
            <div class="right">
                    <h1> -----Liked By----- </h1>
                    <LikeList/>
                    
                
                                        
                    <div class="form-group">
                        
                        <img id="img" src="https://cdn3.iconfinder.com/data/icons/pyconic-icons-1-2/512/heart-outline-512.png" >
                        <img id="img" src="https://cdn3.iconfinder.com/data/icons/cosmo-color-basic-1/40/favorite-512.png"/>
                    </div>
                                    
            </div>
            
            


    </div>
</template>

<script>
import LikeList from '@/components/LikeList.vue'
export default {
    components:{
        LikeList
    },
    computed:{
        currentImg(){

            return this.$store.state.currentImg

        }
    },
    methods:{
        backbutton(){
            this.$router.push('about')
        }
    }
}
</script>



<style scoped>



        .postview{
            
            width: 100%;
            height: 50vh;
            position: relative;
            display: flex;
            
            
        }
        h1{
            text-align: center;
            font-family: cursive;
        }
        .left{
            flex-basis: 50%;
            

        }
        .right{
            flex-basis: 50%;
        }


        
        
       .left img{
           margin-left:20%;
           margin-top:15%;
           width:400px;
           height: 400px;
           border-radius: 12px;
           
        }
        
        

                    
            
        #img{
            width:40px;
            height:40px;
        }

        

        .form-group {
            margin-top: 30px;
            width: 100%;
            text-align: center;
        }
        

       
        
        

        
  





</style>