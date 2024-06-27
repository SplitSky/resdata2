<script>
    export let user = { isAdmin: false };
  </script>
  
  <nav class="bg-gray-800 p-4">
    <div class="container mx-auto flex justify-between items-center">
      <a href="/" class="text-white font-bold">Resdata2</a>
      <div class="flex space-x-4">
        <a href="/" class="text-gray-300 hover:text-white">Home</a>
        <a href="/about" class="text-gray-300 hover:text-white">About Us</a>
        <a href="/documentation" class="text-gray-300 hover:text-white">Documentation</a>
        <a href="/login" class="text-gray-300 hover:text-white">Login</a>
        {#if user.isAdmin}
          <a href="/profile" class="text-gray-300 hover:text-white">Profile</a>
        {/if}
      </div>
    </div>
  </nav>
  