<template>
    		<div class="profilecard">


					<div class="card">
						<div class="avatar">
							<div class="circle"></div>
							<div class="circle"></div>
							<img v-if="item.image_url" :src="item.image_url"/>
					  		<img v-else :src="'http://127.0.0.1:8000'+img"/></div>
							
							<input type="file" @change="onFileChanged" accept="image/*" id="imgupload" />
                      
					  
						<div class="info" >
							<span class="big">{{current.username}} </span> <br/>
							<span class="small">{{current.name}}</span> 
							<br>
						</div>
												
						<div class="about">

							
						
							<button  v-if="show" class="unfollow-follow" @click="followunfollow">{{typeofuser}}</button>
						
							<br>
							<span> Magni corrupti perspiciatis eligendi veniam. Rem enim iusto, rerum voluptatibus eum eius! Eos accusamus laboriosam excepturi soluta vitae. Quod iure cumque odio.</span></div>
							</div>
					<div class="btn">
						
						<button class="post" @click="post" >post</button>
						<button class="followers" @click="followers">followers</button>
						<button class="following" @click="following">following</button></div>

						
			</div>
</template>

<script>
import axios from 'axios';

export default {
	data(){
		return {

			typeofuser:"follower",
			selectedFile: null,
			item:{
              image : null,
              image_url: null,
              
        		},

		}
	},

	computed:{
		img(){
			return this.current.profile_img
		},
		

		current(){
			
			return  Object.keys(this.$store.state.ondemand).length==0 ? this.$store.state.user[0] :this.$store.state.ondemand
		},
		show(){
			if(Object.keys(this.$store.state.ondemand).length!=0){
				return true
				
			}
			else{
				return false
			}
		},
		

	},
	
	methods:{

		onFileChanged (event) {
                  this.selectedFile = event.target.files[0]
                  console.log(this.selectedFile)
                  let reader = new FileReader();
                  reader.readAsDataURL(this.selectedFile);
                  reader.onload= e=>{
					this.item.image_url=e.target.result,
					this.onUpload()
                  }
				  },
		onUpload() {
					  const formData = new FormData()
					  console.log("going")
                      formData.append('image', this.selectedFile, this.selectedFile.name)
                      axios.post('http://127.0.0.1:8000/api/images/', formData)
                      .then(res=>{

                       console.log(res.data.image)
					   this.item.image=res.data.image,
					   this.update()
					   
                       

                      })
		},
		update(){

			fetch('http://127.0.0.1:8000/api/registor/',{
                  method: 'PUT',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({
                    "name": this.$store.state.user[0].name,
                    "username": this.$store.state.user[0].username,
					"password": this.$store.state.user[0].password,
					"profile_img":this.item.image
                    }),
                  })
          .then(res=> res.json())
          .then((data)=>{
			console.log(data),
			this.$store.commit('set_user_img',data)
           
            
            
            })

		},
		post(){
			this.$store.commit('set_btn',1)

		},
		followers(){
			this.$store.commit('set_btn',2)
		},
		following(){
			console.log('clicked')
			this.$store.commit('set_btn',3)
		},
		followunfollow(){

			if(this.typeofuser=='unfollower'){




				fetch('http://127.0.0.1:8000/api/unfollow/',{
						method: 'POST',
						headers: {
							'Content-Type': 'application/json',
						},
						body: JSON.stringify({"user":this.$store.state.user[0].id ,"check":this.$store.state.ondemand.id}),
						})
				.then(res=> res.json())
				.then(()=>{
					
					this.typeofuser='follower'
					this.$store.commit('set_followunfollow','follower')
					
						})
					
			}
			else{

							fetch('http://127.0.0.1:8000/api/follow/',{
						method: 'POST',
						headers: {
							'Content-Type': 'application/json',
						},
						body: JSON.stringify({"user":this.$store.state.user[0].id ,"check":this.$store.state.ondemand.id}),
						})
				.then(res=> res.json())
				.then(()=>{
					
					this.typeofuser='unfollower',
					this.$store.commit('set_followunfollow','unfollower')
					
					
						})
			}

		}

	},
	mounted(){
		fetch('http://127.0.0.1:8000/api/checkfollower/',{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
			  body: JSON.stringify({"user":this.$store.state.user[0].id ,"check":this.$store.state.ondemand.id}),
              })
      .then(res=> res.json())
      .then((data)=>{
          
          if(data){
			  console.log(" njjbhlefkrfgufuy")
			  this.typeofuser='unfollower',
			  this.$store.commit('set_followunfollow','unfollower')
			  
		  }
		  else{
			  this.typeofuser='follower',
			  this.$store.commit('set_followunfollow','follower')

		  }
          
        
            })
	}
}
</script>





<style scoped>

@import url('https://fonts.googleapis.com/css?family=Open+Sans:700,600,300');


.profilecard{
	border-right: 4px solid red;
	width:100%;
}

.card {
	margin-left:10%;
	width: 90%;
	height: 500px;
	position: relative;
}
.card .avatar {
	position: absolute;
	left: 100px;
	top: 90px;
	width: 200px;
	height: 200px;
	border-radius: 50%;
	cursor: pointer;
}
.card .avatar .circle {
	box-sizing: border-box;
	position: absolute;
	border-radius: 50%;
	transition: all 1.5s ease-in-out;
	border: 1px solid;

}
.card  .avatar .circle:first-child {
	left: -7px;
	top: -6px;
	width: 212px;
	height: 212px;
	border-color: transparent   transparent #AD7D52 transparent;
}
.card .avatar .circle:nth-child(2) {
	left: -17px;
	top: -16px;
	width: 232px;
	height: 232px;
	border-color: transparent   transparent #AD7D52 transparent;
}
.card  .avatar:hover .circle:first-child {
	 transform: rotate(360deg);
}
 .card .avatar:hover .circle:nth-child(2) {
	 transform: rotate(-360deg);
}
.card  .avatar img {
	width: inherit;
	height: inherit;
	display: block;
	border-radius: inherit;
}

.card .info{
	
	position:absolute;
	text-align: center;
	top:320px;
	left:150px;
}
span.big {
	 font-size: 32px;
	 font-weight: 600;
}
span.small {

	 font-size: 24px;
	 font-weight: 300;
}


.about{
	width:70%;
	position: absolute;
	top:400px;
	left:30px;
	text-align: center;
	overflow: hidden;
}


.btn{
	margin:30px  0 0 50px ;
	
}


.btn button{
	border:none;
	padding: 10px 20px;
	margin:6px;
	font-size:18px; 
	
	text-transform: uppercase;
	
}
.unfollow-follow{
	border:none;
	padding: 5px 10px;
	margin:3px;
	margin-left:30px;
	font-size:14px; 
	
	text-transform: uppercase;
	color: red;

}




</style>
