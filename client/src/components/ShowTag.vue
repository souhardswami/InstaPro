<template>
  <div class="showtag">
    
    
    <div v-for="pic in result" :key="pic.id" class="gallery">
    
      <img
        :src="'http://localhost:8000'+pic.image_url"
        
      />
    
    <div class="desc">{{pic.tag}}</div>
  </div>
  
  
  </div>
</template>

<script>
import token from '../../apikey.js';
export default {
  props:['tagword'],

  data(){
    return{
      result:[]
    }
  },

  mounted(){
    fetch('http://localhost:8000/api/tagdetail/',{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': token.HiddenToken
              },
              body: JSON.stringify({"idd":this.tagword}),
              })
            .then(res=> res.json())
            .then((data)=>{
                
                
                console.log(data)
                this.result=data
                
                
                    })
  }
}
</script>

<style scoped>

.showtag{
 
  height:50vh;
  margin-top: 40px;
  display: flex;
  flex-wrap: wrap;
  overflow-x:scroll;
  margin-left:50px;


}

div.gallery {
 margin: 10px;
 border: 2px solid black;

 
 width: 200px;
 height:250px;
 transition: transform .25s;
}
div.gallery:hover {
 transform: scale(1.03);
}
div.gallery img {
 width: 100%;
 height: 200px;
}
div.desc {
 text-align: center;
 height: 50px;
 overflow-x: hidden;
}
</style>
