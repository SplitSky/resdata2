import adapter from '@sveltejs/adapter-auto';

export default {
  kit: {
    target: '#svelte',
    adapter: adapter(),
  },
};