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
           <div class="navbar-end">
             <router-link to="/artesanales" class="navbar-item"> Artesanales</router-link>
             <router-link to="/tradicionales" class="navbar-item"> Tradicionales</router-link>

             <div class="navbar-item">
               <div class="buttons">
                 <router-link to="/login" class="button is-warning">Login</router-link>
                 
                 <router-link to="/cart" class="button is-warning">
                    <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                    <span>Cart</span>
                 </router-link>
               </div>
             </div>
           </div>
         </div>
     </nav>
</template>

<script>
export default {
 name: 'NavBar',
data(){
    return {
     showMobileMenu: false, 
    }
}
 
}
</script>
