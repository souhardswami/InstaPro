<template>


<div class="imagegallery">

  




    
      <div  v-for="pic in images" :key="pic.id"  class="grid">
              <figure>
                <div class="img-container">
                    <img :src="'http://localhost:8000'+pic.image_url" >
                    
                </div>
                
                <div class="img-info">
                    <h2 class="tag">TAGLINE</h2>
                    <h3 class="title">{{pic.tag}}</h3>
                    <span class="by">by <a href="#" class="author" >{{pic.username}}</a></span>
                </div>
                <div class="img-button">
                 
                    <img  src="https://cdn3.iconfinder.com/data/icons/pyconic-icons-1-2/512/heart-outline-512.png" @click="like(pic.image_url,pic.id)">
                    
                 
                    
                    <img src="http://icons.iconarchive.com/icons/custom-icon-design/flatastic-1/256/comment-icon.png" @click="comment(pic.image_url,pic.id)"/>
                    
                    <img src="https://cdn0.iconfinder.com/data/icons/social-media-outline-4/64/Facebook_Social_Media_User_Interface-15-512.png" alt="">
                </div>
              </figure>
              
                
        
      </div>

   

      
      
      
      


</div>



</template>

<script>
export default {
  data(){
    return{
      

      image:[]
      
    }
  },
  computed:{
    loguser(){
      return this.$store.state.auth
    },
    
    users(){
      
     

      return this.$store.state.users

    },
    images(){
      return this.$store.state.myphotos
    }
    
    
    
    
  },
  methods:{
    
    comment(picUrl,picId){
      this.$store.commit('set_img',picUrl)
      this.$store.commit('set_picId',picId)
      this.$router.push('/PostContent')
    },
    like(picUrl,picId){
      this.$store.commit('set_img',picUrl)
      this.$store.commit('set_picId',picId)
      this.$router.push('/likecontent')
    },
    
    
  },
  
  
}

</script>


<style scoped>



.imagegallery{
  
    display: flex;
    flex-wrap: wrap;
    justify-content: center;

}

.grid{
  
    width:350px;
}

figure{
  position: relative;
  height: 450px;
  
}

.img-info {
  position: absolute;
  top :235px;
  z-index:2;
  padding: 16px 32px 24px 24px;
  
  width: 214px;
  
  cursor: pointer;
  border-radius: 0px 0px 20px 20px;
  
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  
}

img {
  border-radius: 20px 20px 0 0;
	width: 100%;
  height: 235px;
  
  transform: scale(1);
  transition: all 0.4s ease-in-out;
  
  
}
figure:hover .img-container img {
  
	
  height: 400px;
  opacity: 0.3;
  border-radius:20px 20px 20px 20px; 
  transform: scale(1.1);
  
  
}

figure:hover .img-info{
  background-color: transparent;
  box-shadow: 0 0 0 0 ;
  
}





.tag{
    font-family: 'Raleway', sans-serif;
    text-transform: uppercase;
    font-size: 13px;
    letter-spacing: 2px;
    font-weight: 500;
  color: #868686;
}


.title {
    margin-top: 5px;
    margin-bottom: 10px;
    font-family: 'Roboto Slab', serif;
}


.by {
    font-size: 12px;
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
}

.author {
    font-weight: 600;
    text-decoration: none;
    color: #AD7D52;
}


.img-button {

 
  
     
  opacity: 0;
  display: flex;
  justify-content: space-around;
  position: absolute;
  top :365px;
  z-index:2;
  padding-top: 16px;
  
  width: 214px;
  
  cursor: pointer;
  
}
.img-button img{
    width: 32px;
    height: 32px;
}
figure:hover .img-button{
  opacity: 1;
}
.img-button img:hover{
      transform: scale(1.2);
}








</style>