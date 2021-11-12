<template>
  <div id="wrapper">
    <NavBar/>

    <section class="section">
      <router-view/>
    </section>

   <Footer/>     
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components:{
    NavBar,
    Footer,
  },
  data() {

  },


   
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
