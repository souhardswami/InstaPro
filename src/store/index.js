import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    auth:-1,
    currentImg:'',
    picId:'',

    user:[],
    
    myphotos:[],
    btn:1,
    ondemand:{},
    followunfollow:'follower'
    
  },
  mutations: {
    set_img(state,imgId){
      state.currentImg=imgId
    },
    set_myphotos(state,photos){
      state.myphotos=photos
    },
    set_user(state,user){
      state.user=user
      
    },
    set_auth(state,idd){
      state.auth=idd
    },
    set_btn(state,val){
      state.btn=val
    },
    
    set_picId(state,val){
      state.picId=val
    },
    set_ondemand(state,val){
      state.ondemand=val
      console.log(state.ondemand)
    },
    set_followunfollow(state,val){
      state.followunfollow=val
      console.log(val)
      console.log(state.followunfollow)
    }
    
  },
  actions: {},
  modules: {}
});
