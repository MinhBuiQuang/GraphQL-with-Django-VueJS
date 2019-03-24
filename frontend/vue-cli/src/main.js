import Vue from 'vue'
import VueApollo from 'vue-apollo'
import App from './App.vue'
import Create from './Create.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import ApolloClient from 'apollo-boost'

const apolloClient = new ApolloClient({
  // You should use an absolute URL here
  uri: 'http://localhost:8000/graphql'
})

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

Vue.use(VueApollo)
Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  apolloProvider,
  render: h => h(App)
})

new Vue({
  el: '#create',
  apolloProvider,
  render: h => h(Create)
})
