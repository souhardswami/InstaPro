<template>
	<div class="profile">
		
		<div class="left">
			<ProfileCard/>
		</div>
		<div class="right">
			        
			<h1> ------------ {{method}} ------------</h1>
			<ProfileContent/>
		</div>
		
	</div>
</template>

<script>

import ProfileCard from "@/components/ProfileCard.vue"
import ProfileContent from "@/components/ProfileContent.vue"
export default {
	components:{
		ProfileCard,
		ProfileContent
	},
	computed:{
		method(){
			if(this.$store.state.btn==1){
				return 'POST'
			}
			else if(this.$store.state.btn==2){
				return 'FOLLOWER'
			}
			else{
				return 'FOLLOWING'
			}
		}
	},
	mounted(){
		if(this.$route.params.id==1){
		this.$store.commit('set_ondemand',{})
		}
	}
}
</script>

<style scoped>

.profile{
	display: flex;
}

.right{
	
	width: 62%;
	height: 100%;
}

h1{
	text-align: center;
	font-family:cursive;
	font-weight: 100;
}
    

</style>
