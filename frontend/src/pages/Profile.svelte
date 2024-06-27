<script>
    import UserDetails from '../components/UserDetails.svelte';
    import LicenseManagement from '../components/LicenseManagement.svelte';
    import DataSummary from '../components/DataSummary.svelte';
    import DataBrowser from '../components/DataBrowser.svelte';
    import ApiKeys from '../components/ApiKeys.svelte';
  
    let user = {
      username: 'johndoe',
      email: 'john.doe@example.com',
      isAdmin: true,
      license: { capacity: '50GB', used: '20GB', users: 10, userLimit: 20 },
      summary: { projects: 5, experiments: 10, datasets: 25 },
      data: [{ name: 'Dataset 1' }, { name: 'Dataset 2' }],
      keys: ['key1', 'key2']
    };
  </script>
  
  <section class="container mx-auto p-4">
    <UserDetails {user} />
    <LicenseManagement license={user.license} />
    <DataSummary summary={user.summary} />
    <DataBrowser data={user.data} />
    {#if user.isAdmin}
      <ApiKeys keys={user.keys} />
    {/if}
  </section>  