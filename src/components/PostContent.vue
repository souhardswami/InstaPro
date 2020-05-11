<template>
    <div class="postview">

        
        

        
            <div class="left">
   
                
                
                <img :src="'http://localhost:8000'+currentImg" >
                
            </div>
            <div class="right">
                    <h1> -----COMMENT----- </h1>
                    <CommentList/>
                
                                        
                    <div class="form-group">
                        <input class="form-field" v-model="send.comment_text" placeholder="put your reply">
                        <span><img id="img" src="https://image.flaticon.com/icons/svg/786/786407.svg"  @click="comment"></span>
                    </div>
                                    
            </div>
            
            


    </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
export default {

    data(){
        return{
            
            send:{
            comment_text:'',
            user:'',
            photo:''
            }

        }
    },
    components:{
        CommentList
    },
    computed:{
        currentImg(){
            

            return this.$store.state.currentImg

        }
    },
    methods:{
        comment(){
            console.log("c");
            this.send.user=this.$store.state.user[0].id
            this.send.photo=this.$store.state.picId
            console.log(this.send)
            

            fetch('http://127.0.0.1:8000/api/newcomment/',{
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
          this.send.comment_text=''
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
            margin-left: auto;
            margin-right: auto;
            display: flex;
            
            width: 100%;
        }
        .form-field {
            margin-left:180px;
            border: none;
            border-bottom: solid 4px #AD7D52;
            flex-basis: 40%;
            outline: none;
            font-size: 24px;
            }
        span img{
            margin-left: 30px;
        }
        #img{
            width:40px;
            height:40px;
        }

       
        
        

        
  





</style>