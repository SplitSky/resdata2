<script>
    export let keys;
  </script>
  
  <div>
    <h2 class="text-2xl font-bold">API Keys</h2>
    <ul>
      {#each keys as key}
        <li>{key}</li>
      {/each}
    </ul>
    <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md">Generate New Key</button>
  </div>  