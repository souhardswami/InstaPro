<template>
    <div class="commentlist">

        

        

        <div id="comments" v-for="comment in comments" :key="comment.id">
                    <section>
                    
                    <img :src="'https://myinstapro.herokuapp.com'+comment.profile_img" alt="">
                            <article>
                                <p>
                                  {{comment.comment_text}}
                                </p>
                                 <span class="by">by <a href="#" class="author" >{{comment.username}}</a></span>
                            </article>
                    
                    
                    </section>
        </div>
	
    </div>
</template>

<script>
export default {


  data(){
    return{
      comments:[]
    }
  },
  mounted(){
    
    

     fetch('https://myinstapro.herokuapp.com/api/comments/',{
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({"picId":this.$store.state.picId}),
              })
          .then(res=> res.json())
          .then((data)=>{
              console.log(data)
              this.comments=data
              
              
              
            
                })
      


  }
}
</script>

<style scoped>


.commentlist{
    height:50vh;
    margin-left:  auto;
    margin-right: auto;
    width: 60%;
   overflow-y: scroll;
   overflow-x: hidden;

    
    
}
.commentlist::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.commentlist::-webkit-scrollbar-track {
  background-color: rgba(0, 0, 0, 0.4);
  border-radius: 10px;
}
.commentlist::-webkit-scrollbar-thumb {
  background-color: #AD7D52;
  border-radius: 10px;
}

#comments {
            height: 100%;
            max-height: 126px;
                
            
}

#comments section {
                max-width: 340px;
                margin: 18px 0 0 18px;
}

#comments section img {
                    width: 75px;
                    height: 75px;

                    float: left;

                    border-radius: 50%;

                    margin: 0 18px 0 0;
}

#comments section  article {
                    max-width: 240px;
                    display: inline-block;

                    margin-bottom: 18px;
}

#comments section  article:last-child {
                        margin-bottom: 0;
                    }

#comments section  article                     p {
                        margin-top: 5px;
                        color: #82868f;

                        font-size: 14px;
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

</style>
