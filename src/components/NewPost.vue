<template>
    <div class="newpost">


      <h1>------NEWPOST------</h1>

        
          
              
              
        
        

          <figure>
                  <div class="img-container">
                     <img  id="img" v-if="item.image_url" :src="item.image_url" />
                      <img  v-else src="@/assets/1.jpg"/>
                      <input type="file" @change="onFileChanged" accept="image/*" id="imgupload" />
                      <img id="uploadimg" src="https://img.icons8.com/wired/50/000000/upload.png"/>
                      
                  </div>
                  
                  <div class="img-info">
                      <h2 class="tag">TAGLINE</h2>
                      <h3 class="title"><textarea v-model="item.tag"></textarea></h3>
                      <span class="by">by <a href="#" class="author" >{{item.user.username}}</a></span>
                  </div>
                  
                </figure>
            <button id="submit" @click="onUpload">submit</button>
            

        </div>
    
</template>




<script>
import axios from 'axios';

export default {
      data() {
          return {
            selectedFile: null,
            item:{
              image : null,
              image_url: null,
              user:this.$store.state.user[0],
              tag:'editable'
                  },
          }
        },
        
      methods: {
              onFileChanged (event) {
                  this.selectedFile = event.target.files[0]
                  console.log(this.selectedFile)
                  let reader = new FileReader();
                  reader.readAsDataURL(this.selectedFile);
                  reader.onload= e=>{
                    this.item.image_url=e.target.result
                  }
                  },
              onUpload() {
                      const formData = new FormData()
                      formData.append('image', this.selectedFile, this.selectedFile.name)
                      axios.post('http://127.0.0.1:8000/api/images/', formData)
                      .then(res=>{

                       console.log(res.data.image)
                       this.item.image=res.data.image
                       this.final()

                      })
              },
              final(){



                fetch('http://127.0.0.1:8000/api/newpost/',{
                
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(
                      {
                        "image_url":this.item.image,
                        "user":this.item.user.id,
                        "tag":this.item.tag
                      }

                    ),
              })
              .then(res=> res.json())
              .then(data=>{
                console.log(data)
                this.$router.push('about/')
              })

                
              }

    }
}
</script>


<style scoped>


.newpost{
  width:25%;
  margin:0 auto;
  height: 87vh;
  padding-top:120px;


  
}

    
h1{
  margin-top: -60px;
	text-align: center;
	font-family:cursive;
	font-weight: 100;
}



figure{
  width: 255px;
  position: relative;
  
  
}


#imgupload{
  position: absolute;
  top:215px;
  left:200px;
  z-index:2;
  opacity: 0;
}
  
#uploadimg{
  position: absolute;
  width:64px;
  height:64px;
  top:200px;
  left:200px;
  
  
}
  

.img-info {
  position: absolute;
  top :235px;
  z-index:2;
  padding: 16px 32px 24px 24px;
  
  width: 200px;
  
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

#img{
  opacity: 0.5;
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
.title textarea{
  border:none;
  outline: 0;
  font-size: 18px;
  width: 200px;
  height: 40px;
  resize: none;
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

#submit{
  border: none;
  outline: none;
  font-size: 24px;
  padding:10px 24px;
  position: absolute;
  top:650px;
  left:780px;
}










      
</style>


