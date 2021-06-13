import Vuex from 'vuex'
import Vue from 'vue'
import userModule from './user'
import productModule from './product'
import cartModule from './cart'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user: userModule,
    product: productModule,
    cart: cartModule
  }
})
