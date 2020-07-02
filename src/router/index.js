import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
// import Post from "../views/Post.vue";

import PostContent from "@/components/PostContent.vue"
import LikeContent from "@/components/LikeContent.vue"
Vue.use(VueRouter);

const routes = [
  
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/postContent/",
    name: "PostContent",
    component: PostContent
  },
  {
    path: "/likeContent/",
    name: "LikeContent",
    component: LikeContent
  },
  
  {
    path: "/about/",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },

  {
    path: "/profile/:id",
    name: "Profile",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Profile.vue")
  },
  {
    path: "/search/",
    name: "Search",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search.vue")
  },
  {
    path: "/new/",
    name: "New",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/New.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
