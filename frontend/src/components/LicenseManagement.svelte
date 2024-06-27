<script>
    export let license;
  </script>
  
  <div>
    <h2 class="text-2xl font-bold">License</h2>
    <p><strong>Database Capacity:</strong> {license.capacity}</p>
    <p><strong>Space Used:</strong> {license.used}</p>
    <p><strong>Users:</strong> {license.users}/{license.userLimit}</p>
  </div>  