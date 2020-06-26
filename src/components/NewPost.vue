<template>
    <div class="newpost">


      <h1>------NEWPOST------</h1>

        
          
              
              
        
        
        <div class="first" :class="face1">

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


                
        </div>




      <div   class="second" :class="face2">

           
        <h3 id="headline">  Tag's </h3>
        <div id="chips">

            <div v-for="tagg in tags" :key="tagg" class="chip">
              
              {{tagg}}
              <span class="closebtn" onclick="this.parentElement.style.display='none'">&times;</span>
            </div>
        </div>

        <br>

        <input v-model="tag" id="tag">
        <button @click="enter" id="enter">ADD</button>



      </div>
            <button @click="next" id="prevnext"> {{buttonswap}}</button>
            <button id="submit" @click="onUpload">submit</button>
            

        </div>
    
</template>




<script>
import axios from 'axios';

export default {
      data() {
          return {
            selectedFile: null,
            face1:'front',
            face2:'back',
            tag:'',
            tags:[],
            item:{
              image : null,
              image_url: null,
              user:this.$store.state.user[0],
              tag:'put you post here'
                  },
          }
        },

      computed:{
        


        buttonswap() {

          if(this.face1=='front'){
              return 'next >>'
          }
          else{
            return '<< prev'
          }

        }

      },

        
      methods: {
        enter(){
          this.tags.push(this.tag),
          this.tag=''
        },

        next(){
          // simple swapping
          var temp;
          temp=this.face1,
          this.face1=this.face2,
          this.face2=temp

        },
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
                        "tag":this.item.tag,
                        "tags":this.tags
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
  height: 70vh;
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

.second{
  font-size: 30px;
  position: relative;
  top:-250px;
  /* left:120px; */

  height: 40vh;

  border-top: thick double black;
  border-bottom: thick double black;

  
}

.front{
  
  transform: rotateY(0);
}


.back{
  transform: rotateY(90deg);
}

#headline{
  margin-top:10px;
  margin-left:130px;
}


#prevnext{
  border: none;
  outline: none;
  font-size: 14px;
  padding:8px 14px;
  position: absolute;
  top:660px;
  left:650px;
  
}
#enter{
  border: none;
  outline: none;
  font-size: 12px;
  padding:5px 10px;
  position: absolute;
  top:268px;
  left:240px;
  
}

#tag{

  position: absolute;
  top:270px;
  /* left:650px; */
  left:60px;

}

.chip {
  display: inline-block;
  
  padding: 0 25px;
  height: 20px;
  font-size: 14px;
  line-height: 20px;
  border-radius: 15px;
  margin-left:20px;
  background-color: #f1f1f1;
  
  
}

#chips{
  height: 100px;
  border:double #aaaaaa thick;
  overflow:scroll;
}



.closebtn {
  padding-left: 10px;
  color: #888;
  font-weight: bold;
  float: right;
  font-size: 20px;
  cursor: pointer;
}

.closebtn:hover {
  color: #000;
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


