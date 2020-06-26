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
    btn:1
    
  },
  mutations: {
    set_img(state,imgId){
      state.currentImg=imgId
    },
    set_myphotos(state,photos){
      state.myphotos=photos
    },
    set_user(state,user){
      state.user=user,
      state.auth=user.id
    },
    set_btn(state,val){
      state.btn=val
    },
    
    set_picId(state,val){
      state.picId=val
    }
    
  },
  actions: {},
  modules: {}
});
