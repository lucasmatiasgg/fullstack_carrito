
const routes = [
  {
    path: '/',
    component: () => import('layouts/LoginLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') },
      { path: '/register', component: () => import('pages/Register.vue') }
    ]
  },
  {
    path: '/desktop',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Desktop.vue') },
      { path: '/cart', component: () => import('pages/Cart.vue') },
      { path: '/changeName', component: () => import('pages/Preferences') },
      { path: '/changePassword', component: () => import('pages/ChangePassword') },
      { path: '/buyOrder', component: () => import('pages/BuyOrder') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
