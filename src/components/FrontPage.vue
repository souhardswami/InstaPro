<template>
  <div class="frontpage" id="test">
    
    

   
      
        <div class="left-box">


          <span>New Today's Trend</span>
    

           <h6>All my pictures are built around the idea of
             getting in trouble and so giving me the chance
              to be desperately serious in my attempt to appear
               as a normal little gentleman.</h6>
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



