<script>
    let username = '';
    let password = '';
  
    function login() {
      // Handle login logic
      console.log(`Logging in as ${username}`);
      // Redirect to profile page
      window.location.href = '/profile';
    }
  </script>
  
  <section class="container mx-auto p-4">
    <h1 class="text-2xl font-bold">Login</h1>
    <form on:submit|preventDefault={login} class="mt-4">
      <label class="block">
        <span class="text-gray-700">Username</span>
        <input type="text" bind:value={username} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" />
      </label>
      <label class="block mt-4">
        <span class="text-gray-700">Password</span>
        <input type="password" bind:value={password} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm" />
      </label>
      <button type="submit" class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md">Login</button>
    </form>
  </section>  