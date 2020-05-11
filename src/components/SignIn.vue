<template>
    <div>

        <button class="button"  @click="disSignin">SignIn</button>
        
                        <div id="myModal" class="modal" v-if="show">
                                    <div class="modal-content">
                                        <span class="close" @click="hidSignin" >&times;</span>
                                        <div>
                                            <img src="https://www.shareicon.net/data/512x512/2017/05/09/885911_logo_512x512.png">
                                        </div>
                                        <span>Sign-in</span>
                                        <form >
                                            <input v-model="sign.name" type="text" placeholder="Name">
                                                <br>
                                            <input v-model="sign.username" type="text" placeholder="UserName">
                                                <br>
                                            <input v-model="sign.password" type="password" placeholder="Password">
                                               <br>
                                            <input v-model="sign.Conformpassword" type="password" placeholder="re-Password">
                                            <br>
                                            <button class="button" @click="signSubmit">Signin</button>
                                        </form>
                                    </div>
                        </div>
    </div>
</template>




<script>
export default {
    data(){
      return{
        show:false,
        sign:{
            name:'',
            password:'',
            Conformpassword:'',
            username:''
        }
      }
    },
    methods:{
      disSignin(){
          this.show=true
      },
      hidSignin(){
        this.show=false
      },
      signSubmit(){
            console.log("future task")
            console.log(this.sign)

              
            fetch('http://127.0.0.1:8000/api/registor/',{
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                    "name":this.sign.name,
                    "username":this.sign.username,
                    "password":this.sign.password
                    }),
                  })
          .then(res=> res.json())
          .then((data)=>{
            console.log(data)
            this.show=false
            
            
            })


      
      }
    }
}
</script>


<style scoped>
.button {
  
  border: none;
  color: black;
  padding: 15px 32px;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}



.modal {
  display: block; 
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%;
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0,0,0); 
  background-color: rgba(0,0,0,0.4); 
}


img{
    width:  60px;
    
    margin-right: auto;
    
   
}

.modal-content {
  background-color: #fefefe;
  
  margin: 10% auto; 
  padding: 20px;
  border: 1px solid #888;
  width: 30%; 
}



form input[type="text"],
form input[type="password"],
form input[type="email"]
 {
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
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>