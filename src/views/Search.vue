<template>
    <div class="search">

      
        <div id="wrap">
          
            <input   v-model="search" type="text" placeholder="what's  ?">
            <input    @click="res" type="submit">
        </div >
        <div id="result">
            <div  v-show="notHash" v-for="user in result" :key="user.id">
            

                <div class="card">
                    <div class="picture">
                        <img  :src="'https://myinstapro.herokuapp.com'+user.profile_img">
                    </div>
                    <div class="team-content">
                        <h3 class="name">{{user.username}}</h3>
                        <h4 class="title">{{user.name}}</h4>
                    </div>
                    <div class="future">
                       <button id="profile-btn" @click="showprofile(user.id)"> profile</button>
               
                    </div>
                </div>


            </div>
            <div  v-show="Hash" v-for="tag in result" :key="'tag-'+tag.id">
            

                <div class="card">
                    <div class="picture">
                          <img  src="https://static.vecteezy.com/system/resources/previews/000/337/614/non_2x/vector-hash-icon.jpg">
                    </div>
                    <div class="team-content">
                        <h3 class="name">{{tag.tagword}}</h3>
                        
                    </div>
                    <div class="future">
                       <button id="profile-btn"  @click="showtag(tag.id)">explore</button>
                    </div>
                </div>


            </div>




        </div>


        <div id="myModal" class="modal" v-if="show">
                                    <div class="modal-content">
                                      
                                      
                                       
                                        
                                        <span class="close" @click="close" >&times;</span>
                                      
                                       
                                        <ProfileCopy/>
                                        
                                        
                                    </div>
                        </div>
        <div id="myModal" class="modal" v-if="show2">
                                    <div class="modal-content">
                                      
                                      
                                       
                                        <h1>{{search}}</h1>
                                        <div class="close" @click="close2" >&times;</div>
                                      
                                       
                                        


                                        <ShowTag :tagword="sendidd"/>
                                        
                                        
                                    </div>
                        </div>
    </div>
</template>

<script>
import ProfileCopy from './Profile.vue'
import ShowTag from '@/components/ShowTag.vue'
export default {
  components:{
    ProfileCopy,
    ShowTag
  },

    data(){
        return{
            search:'',
            result:[],
            show:false,
            show2:false,
            sendidd:''
        }
    },
    computed:{
      notHash(){
        if(this.search[0]=='#'){
          return false
        }
        else{
          return true
        }

      },
      Hash(){
        if(this.search[0]=='#'){
          return true
        }
        else{
          return false
        }

      }
      
    },
    methods:{

      
        

        res(){
        
            
            fetch('http://localhost:8000/api/search/',{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({"item":this.search}),
              })
            .then(res=> res.json())
            .then((data)=>{
                
                
                this.result=data
                
                
                    })
        },
        showprofile(idd){

          

          for (let i of this.result){
            if(i.id==idd){
              this.$store.commit('set_ondemand',i)
              console.log("hhhh")
              this.show=true
            }
          }

        },
        showtag(idd){
          this.sendidd=idd,
          this.show2=true
        },
        close(){
          this.show=false
        },
        close2(){
          this.show2=false
        }

    }
    
}
</script>



<style scoped>

#wrap {
  
  display: inline-block;
  position: relative;
  height: 60px;
  margin-left:97%;
  margin-top: 50px;
  
  padding: 0;
  position: relative;
}

input[type="text"] {
  height: 60px;
  font-size: 45px;
  display: inline-block;
  font-family: cursive;
  font-weight: 100;
  border: none;
  border-left: solid red 4px;
  outline: none;
  color: #555;
  padding: 3px;
  padding-right: 60px;
  width: 0px;
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  width: 400px;
  cursor: pointer;
  caret-color: black;
  
}


#profile-btn{
  
	border:none;
	padding: 10px 20px;
	margin:6px;
	font-size:18px; 
	
	text-transform: uppercase;
	

  
}

input[type="submit"] {
  height: 67px;
  width: 63px;
  display: inline-block;
  
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADNQTFRFU1NT9fX1lJSUXl5e1dXVfn5+c3Nz6urqv7+/tLS0iYmJqampn5+fysrK39/faWlp////Vi4ZywAAABF0Uk5T/////////////////////wAlrZliAAABLklEQVR42rSWWRbDIAhFHeOUtN3/ags1zaA4cHrKZ8JFRHwoXkwTvwGP1Qo0bYObAPwiLmbNAHBWFBZlD9j0JxflDViIObNHG/Do8PRHTJk0TezAhv7qloK0JJEBh+F8+U/hopIELOWfiZUCDOZD1RADOQKA75oq4cvVkcT+OdHnqqpQCITWAjnWVgGQUWz12lJuGwGoaWgBKzRVBcCypgUkOAoWgBX/L0CmxN40u6xwcIJ1cOzWYDffp3axsQOyvdkXiH9FKRFwPRHYZUaXMgPLeiW7QhbDRciyLXJaKheCuLbiVoqx1DVRyH26yb0hsuoOFEPsoz+BVE0MRlZNjGZcRQyHYkmMp2hBTIzdkzCTc/pLqOnBrk7/yZdAOq/q5NPBH1f7x7fGP4C3AAMAQrhzX9zhcGsAAAAASUVORK5CYII=) center center no-repeat;
  text-indent: -10000px;
  border: none;
  position: absolute;
  top: 0;
  right: 0;
  cursor: pointer;
  opacity: 0.4;
  cursor: pointer;
  transition: opacity .4s ease;
}

input[type="submit"]:hover {
  opacity: 1;
}


#result{
    margin-top:100px;
    height:60vh;
    
    overflow-y: scroll;
    overflow-x: hidden;
}







.card {
width: 250px;
height: 250px;
  margin-left: auto;
  margin-right: auto;
  padding: 30px 0 40px;
  margin-bottom: 30px;
  background-color: #f7f5ec;
  text-align: center;
  overflow: hidden;
  position: relative;
}

.card .picture {
  display: inline-block;
  height: 130px;
  width: 130px;
  margin-bottom: 50px;
  z-index: 1;
  position: relative;
}

.card .picture::before {
  content: "";
  width: 100%;
  height: 0;
  border-radius: 50%;
  background-color: #AD7D52;
  position: absolute;
  bottom: 135%;
  right: 0;
  left: 0;
  opacity: 0.9;
  transform: scale(3);
  transition: all 0.3s linear 0s;
}

.card:hover .picture::before {
  height: 100%;
}

.card .picture::after {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #AD7D52;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

.card .picture img {
  width: 100%;
  height: auto;
  border-radius: 50%;
  transform: scale(1);
  transition: all 0.9s ease 0s;
}


.card:hover .picture img {
  box-shadow: 0 0 0 14px #f7f5ec;
  transform: scale(0.7);
}


.card .title {
  display: block;
  font-size: 15px;
  color: #4e5052;
  text-transform: capitalize;
}

.card .future {
  width: 100%;
  padding: 0;
  margin: 0;
  background-color: #AD7D52;
  position: absolute;
  bottom: -100px;
  left: 0;
  transition: all 0.5s ease 0s;
}

.card:hover .future {
  bottom: 0;
}





.modal {
  display: block; 
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%;
  height: 100%; 
  overflow-x: scroll; 
  
  background-color: rgba(0,0,0,0.4); 
}
.modal-content {
  background-color: #fefefe;
  margin: 2% auto; 
  padding: 20px;
  border: 1px solid #888;
  width: 80%; 
}


form input[type="text"],
form input[type="password"] {
  max-width:300px;
  width: 80%;
  line-height:3em;
  font-family: 'Ubuntu', sans-serif;
  margin:1em 2em;
  border-radius:5px;
  border:2px solid #f2f2f2;
  outline:none;
  padding-left:10px;
}

.close {
  position: fixed;
  right: 10%;
  top:60px;
  color: #aaa;
  float: right;
  font-size: 28px;
  padding-left:10px;
  padding-right:10px;
  font-weight: bold;
  border: solid #AD7D52 2px;
  border-radius:50%; 
  transition: transform .25s;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
  transform: rotate(360deg);
}

</style>
