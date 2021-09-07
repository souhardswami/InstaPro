<template>
  <div class="frontpage" id="test">
    
    

   
      
        <div class="left-box">


          <span>New Today's Trend</span>
    
           <h6>{{data}}</h6>


               
          <Auth/>

            





          
        </div>
        <div class="right-box">

          <img src="http://www.pngmart.com/files/6/Charlie-Chaplin-PNG-Clipart.png">
          <!-- <img src="@/assets/souhard.png"> -->
        </div>

        





  </div>
</template>


<script>

import Auth from "@/components/Auth.vue";

export default {

  components:{
    Auth

  },
  data(){
    return{
      data:'',
      active:0,
      
      stored:[`All my pictures are built around the idea of getting in trouble and so giving me the chanceto be desperately serious in my attempt to appear as a normal little gentleman.`,
      `I’m a nobody. Nobody’s perfect. So I guess that makes me perfect.I’m not the kind of person who tries to be cool or trendy, I’m definitely an individual.a mirror. If you’re cool with me, I’m cool with you.`,
      `Being popular on Facebook is like sitting at the cool table in a cafeteria at a MENTAL HOSPITAL., I Protect It With A Layer Of Fat.`
      ]
    }
  },

  created(){
    this.data=this.stored[2],

    setInterval(()=>{
      this.data=this.stored[this.active%3],
      this.active=this.active%3+1

    },5000)
  }

  
  
  
}
</script>



<style scoped>

    
 



    .frontpage{
      position: relative;
      text-align: center;
      font-size: 50px;
      height: 87vh;

      display: flex;
      justify-content: space-between;
      align-items: center;
      
      
    }

     img{
       
      width:50%;
      
    }
     
     span{
      z-index: -1;
      opacity: 0.1;
      position:absolute;
      font-size: 120px;
      font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
      font-weight: 990;
      top:100px;
      left:100px;
    }
    h6{
      height: 180px;
      animation: change 5s infinite;
    }
    @keyframes change {
      0%{
        opacity: 0;
      }
      70%{
        opacity: 1;
      }
      100%{
        opacity: 0;
      }
      
    }



            
      

    .left-box{
      flex-basis: 50%;
      font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
      
      /* background-color: #eee3e7 ; */
      

    }
    .right-box{
      flex-basis: 50%;
      /* background-color:#f9caa7 ; */

    }





  
</style>



