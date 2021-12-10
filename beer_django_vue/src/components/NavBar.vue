<template>
    <nav class="navbar is-dark">
       <div class="navbar-brand">
         <router-link to="/" class="navbar-item"><strong>BeerUp</strong></router-link>

         <a  class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
           <span aria-hidden="true"></span>
           <span aria-hidden="true"></span>
           <span aria-hidden="true"></span>
           <span aria-hidden="true"></span>
         </a>
       </div>
         
         <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
           
           <div class="navbar-start">
             <div class="navbar-item">
               <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" class="input" placeholder="¿Qué buscas" name="query">
                    </div>
                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
                </div>
               </form>
             </div>

           </div>
           <div class="navbar-end">
             <router-link to="/premium/" class="navbar-item"> Premiums</router-link>
             <router-link to="/artesanales/" class="navbar-item"> Artesanales</router-link>
             <router-link to="/tradicionales/" class="navbar-item"> Tradicionales</router-link>

             <div class="navbar-item">
               <div class="buttons">
                 <router-link to="/log-in" class="button is-warning">Login</router-link>
                 
                 <router-link to="/cart" class="button is-warning">
                    <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                    <span>Cart ({{cartTotalLength}})</span>
                 </router-link>
               </div>
             </div>
           </div>
         </div>
     </nav>
</template>

<script>
import axios from 'axios'
export default {

 name: 'NavBar',
  data() {
    return{
      showMobilMenu: false,
      cart:{
        items:[]
      }
    }
  },
  
  mounted(){
    this.cart= this.$store.state.cart
  },

  computed:{
    cartTotalLength(){
      let totalLength = 0

      for(let i=0;i<this.cart.items.length;i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength
    }
  }
 
}
</script>
