export default {
  loadUserInfo: function (state, data) {
    console.log('loadUserInfo-mutation')
    console.log(data)
    state.firstName = data.firstName
    state.lastName = data.lastName
  }
}
