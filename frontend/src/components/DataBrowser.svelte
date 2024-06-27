<script>
    export let data;
  </script>
  
  <div>
    <h2 class="text-2xl font-bold">Data Browser</h2>
    <ul>
      {#each data as item}
        <li>{item.name}</li>
      {/each}
    </ul>
  </div>