<template>
  <div class="page-sign-up">
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Registrarse</h1>

              <form @submit.prevent="submitForm">
                  <div class="field">
                      <label for="">Usuario</label>
                      <div class="control">
                          <input type="text" name="username" id="username" class="input" v-model="username">
                      </div>
                  </div>
                  <div class="field">
                      <label for="">Password</label>
                      <div class="control">
                          <input type="password" name="pass" id="pass" class="input" v-model="password">
                      </div>
                  </div>
                  <div class="field">
                      <label for="">Confirmar Password</label>
                      <div class="control">
                          <input type="password" name="conf_pass" id="conf_pass" class="input" v-model="conf_password">
                      </div>
                  </div>
                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                  </div>

                  <div class="field">
                      <div class="control">
                          <button class="button is-dark">Registrar</button>
                      </div>
                  </div>

                  <hr>

                  O <router-link to="/log-in">Click aquí </router-link> para ingresar

              </form>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name:'SignUp',
    data(){
        return {
            username:'',
            password:'',
            conf_password:'',
            errors:[],
        }
    },
    methods:{
        submitForm(){
            this.errors = []

            if(this.username==''){
                this.errors.push('Debes escribir un nombre de usuario')
            }
            if(this.password ==''|| this.password.length < 6){
                if (this.password==''){
                    this.errors.push('El password está vácio')
                }
                else{
                this.errors.push('El password es muy corto')
                }
            }
            if(this.password != this.conf_password){
                this.errors.push('El password y la confirmación no coinciden')
            }
            if (!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post("api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message:'Usuario creado exitosamente',
                            type:'is-success',
                            dismissible:true,
                            pauseOnHover:true,
                            duration:2000,
                            position:'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error=> {
                        if (error.response){
                            for(const property in error.respose.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))

                        }else if(error.message){
                            this.errors.push('Algo va mal, intenta nuevamente.')
                            console.log(JSON.stringify(error))
                        }
                    })
                
            }
        }
    }

}
</script>

<style>

</style>