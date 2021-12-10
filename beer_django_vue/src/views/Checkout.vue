<template>
  <div class="page-checkout">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Checkout</h1>
          </div>
      </div>

      <div class="column is-12 box">
              <table class="table is-fullwidth" v-if="cartTotalLength">
                  <thead>
                      <tr>
                          <th>Producto</th>
                          <th>Precio</th>
                          <th>Cantidad</th>
                          <th>Total</th>
                          <th></th>
                      </tr>
                  </thead>

                  <tbody>
                      <CartItem
                      v-for="item in cart.items"
                      v-bind:key="item.product.id"
                      v-bind:initialItem="item"
                      v-on:removeFromCart="removeFromCart"
                      />
                  </tbody>

                  <tfoot>

                      <tr>
                          <td colspan="2">Total</td>
                          <td>{{ cartTotalLength }}</td>
                          <td>${{ cartTotalPrice.toFixed(2) }}</td>
                      </tr>

                  </tfoot>
              </table>
              <p v-else> El carrito está vácio...</p>

              <div class="column is-12 box">
                  <h2 class="subtitle">Detalles de envío</h2>
                  <p class="has-text-grey mb-4">* Todos los campos son requeridos</p>

                <div class="columns is-multiline">
                
                    <div class="column is-6">
                        <div class="field">
                            <label>Primer Nombre*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Segundo Nombre*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Teléfono*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Dirección*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Código postal*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>

                    <div class="notification is-danger mt-4" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error" >{{error}}</p>
                    </div>

                    <hr>

                </div>
                    <div id="card-element" class="mb-5">
                        <template v-if="cartTotalLength">
                            <hr>
                            <button class="button is-dark" @click="submitForm">Pagar con Payu</button>
                        </template>
                    </div>
              </div>
        </div>
  </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
export default {

    name:'Checkout',
    components:{
        CartItem
    },
    data(){
        return{
            cart:{
                items: [],
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted(){
        document.title = 'Checkout | Beerup'
        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm(){
            this.errors= []

            if(this.first_name === ''){
                this.errors.push('No hay información en el primer nombre')
            }
            else if(this.last_name === ''){
                this.errors.push('No hay información en el segundo nombre')
            }
            else if(this.email === ''){
                this.errors.push('No escribió el correo electrónico')
            }
            else if(this.phone === ''){
                this.errors.push('No escribió el número de teléfono')
            }
            else if(this.address === ''){
                this.errors.push('No escribió la dirección')
            }
            else if(this.zipcode === ''){
                this.errors.push('No escribió el código postal')
            }
            else if(this.address === ''){
                this.errors.push('No escribió el método de pago')
            }
            
        }
    },
    computed:{
        cartTotalPrice(){
            return this.cart.items.reduce((acc, curVal)=> {
                return acc += curVal.product.price * curVal.quantity
            },0)
        },

        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=> {
                return acc += curVal.quantity
            }, 0)
        }
    }

}
</script>

<style>

</style>