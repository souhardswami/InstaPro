<template>
    <div class="postview">

        
        

        
            <div class="left">
   
                
                
                <img :src="'https://myinstapro.herokuapp.com'+currentImg" >
                    
                
            </div>
            <div class="right">
                    <h1> -----Liked By----- </h1>
                    <LikeList :name="this.$store.state.user[0].username" :triger="trig" @liked="dontshow"/>
                    
                
                                        
                    <div class="form-group" v-if="visible">
                        
                        
                     <button>   <img class="img" id="img1" src="https://cdn3.iconfinder.com/data/icons/pyconic-icons-1-2/512/heart-outline-512.png" @click="like" ></button>
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
    data(){

        return{
            
        visible:true,
        trig:false,

        send:{
            
            userId:'',
            imgId:''
            }
        }
    },

    computed:{
        currentImg(){
            
            return this.$store.state.currentImg

        }
    },
    methods:{
        
        dontshow(){
            this.visible=false
        },

        like(){
            console.log("c");
            this.send.userId=this.$store.state.user[0].id
            this.send.imgId=this.$store.state.picId
            

            fetch('http://127.0.0.1:8000/api/newlike/',{
                method: 'POST',
                headers:
                         {
                             'Content-Type': 'application/json'
                        },
                body: JSON.stringify(
                    this.send

                    ),
                    })
      .then(res=> res.json())
      .then((data)=>{
          console.log(data)
          this.visible=false,
          this.trig=true
          
          })
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
        
        

                    
        .form-group {
            margin-top: 30px;
            width: 100%;
            text-align: center;
            
        }
            
        .img{
            width:40px;
            height:40px;
            
            
            
        }
        
        

        

        
        

       
        
        

        
  





</style>
