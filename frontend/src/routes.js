import Home from './pages/Home.svelte';
import About from './pages/About.svelte';
import Documentation from './pages/Documentation.svelte';
import Login from './pages/Login.svelte';
import Profile from './pages/Profile.svelte';

export default {
  '/': Home,
  '/about': About,
  '/documentation': Documentation,
  '/login': Login,
  '/profile': Profile
};