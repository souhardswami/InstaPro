
<template>
    <div class="navbar">
              <nav>
                        
                        <img src="https://www.shareicon.net/data/512x512/2017/05/09/885911_logo_512x512.png">
                        
                        <div id="sign">insta-Pro</div>
                        <div class="circle"></div>
                        <div class="A"><router-link class="rl" to="/" >Home</router-link></div>
                        <div class="A"><router-link class="rl notActive" to="/about"  :disabled="notActive"  >About</router-link></div>
                        <div class="A">
                          <router-link  to="/search" class="notActive" :disabled="notActive" >
                          <img src="https://img.icons8.com/pastel-glyph/64/000000/search--v1.png"/>
                          
                          </router-link>
                        </div>
                        <div class="A">
                          <router-link class="notActive" to="/new" :disabled="notActive" >
                          <img src="https://img.icons8.com/wired/64/000000/plus-2-math.png"/>
                          </router-link>
                        </div>
                        <div class="A" id="proimg">

                          <router-link   class="notActive"  to="/profile/1" :disabled="notActive" >
                          
                          <img v-if="this.$store.state.auth==-1" src="https://cdn.onlinewebfonts.com/svg/img_518099.png">
                          <img v-else :src="'http://127.0.0.1:8000'+this.$store.state.user[0].profile_img">
                          
                          </router-link>
                        </div>
                         
              </nav>
             <router-view id="rw"/> 
        </div>



    

  
</template>

<script>
export default {
  
  computed: {
        notActive(){
          return  Object.keys(this.$store.state.user).length==0 ? true :false
        }
    }
}
</script>







<style scoped>


.notActive[disabled] {
  pointer-events: none;
}

  .navbar{
    margin:0 100px;
    
  }

  nav{
    
    
    
    display: flex;
    height: 100px;

    width: 100%;
     align-items: center;
  }
  
  img{
    width:  60px;
    
    margin-right: auto;
    
   
  }
  #sign{
     margin-right: 30%;
     font-size: 30px;
     font-family: cursive;

  }

  
  .A{
    
    margin:40px;
    font-size: 28px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif
    

    

  }


  #proimg{
    width:60px;
    height:60px;
    border:solid 4px black;
    border-radius:50%; 
    
  }

  
   #proimg img{
    
    
    border-radius:50%; 
    
     
  } 
  


  .rl{
	  text-decoration: none;
    color: black;
    position: relative;
  } 
  .rl::before{
          content: "";
        position: absolute;
        width: 100%;
        height: 3px;
        bottom: 10px;
        left: 0;
        background:rgba(0, 0, 0, 0.6);
        /* visibility: hidden; */
        border-radius: 5px;
        transform: scaleX(0);
        transition: .25s linear;
  }
  .rl:hover::before{
    transform: scaleX(1);

  }

  
  

  

  .circle{
          background-color: #414a4c;
          /* background-color: black; */
          
            position: absolute;
            
            width: 10px;
            height: 10px;
            
            
            border-radius: 50%;
            top:53px;
            left:133px;
            animation: increase 2s infinite ease-in;
            

        }
  @keyframes increase{
            50%{
                opacity: 0.3;
                top:25px;
                width:60px;
                height: 60px;
                left:108px;
            }
         }


           

            

  

</style>

