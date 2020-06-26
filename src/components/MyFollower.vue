<template>
    <div class="myfollower">
        
        <div v-for="user in users" :key="user.id">
        
            <div class="card">
                            <div class="avatar">
                                <div class="circle"></div>
                                <div class="circle"></div>
                                <img :src="'https://myinstapro.herokuapp.com'+user.profile_img" alt="">
                                </div>
                            
                            <div class="info" >
                                <span class="big">{{user.username}} </span> <br/>
                                <span class="small">{{user.name}}</span> </div>
                                                    
                            <div class="about">
                                <span>Lorem  dolor sit amet consectetur adipisicing elit.Incidunt, fugiat explicabo quosex error repellendus unde laborum vel numquam</span></div>
            </div>
        </div>

    </div>
</template>

<script>

export default {

    data(){
        return {
            users:[]
        }
    },
    

   
  
  created(){
      


      fetch('https://myinstapro.herokuapp.com/api/follower/',{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({"user":this.$store.state.user[0].id}),
              })
      .then(res=> res.json())
      .then((data)=>{
          
          this.users=data
          
        
            })
      
  }

    
      
        
  
    
}
</script>

<style scoped>
.myfollower{
    
    transform: scale(0.75);
    
}



.card {
    margin-bottom: 30px;
	margin-left:10%;
	width: 90%;
	height: 500px;
	position: relative;
    border-right: solid 4px red;
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
</style>
