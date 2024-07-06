<script>
    let user = null; // Replace with actual user data in a real application
  
    function login() {
      // Implement login functionality here
      user = { name: 'John Doe', profileImage: 'https://via.placeholder.com/40' };
    }
    
    function logout() {
      // Implement logout functionality here
      user = null;
    }
</script>

<header>
    <div class="logo">
      <img src="logo_bg.png" alt="Project Icon" />
    </div>
    
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
      <a href="/blog">Blog</a>
    </nav>
    
    <div class="user-section">
      {#if user}
        <div class="user-info">
          <img src={user.profileImage} alt="User Profile" />
          <span>{user.name}</span>
          <button on:click={logout}>Logout</button>
        </div>
      {:else}
        <button on:click={login}>Login</button>
      {/if}
    </div>
  </header>

<main>
<section>
    <div class="section">
        <h2 class="title-lean" >Start your journey with data here!</h2>
    </div>
    <picture class="full-page-picture">
      <source srcset="backdrop.png" type="image/png">
    </picture>
    <button>Get Started</button>
</section>
</main>

<footer>
<p>&copy; 2024 ResData2. This project is open source!</p>
</footer>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

  :global(body) {
    margin: 0;
    font-family: 'Roboto', sans-serif;
    background-color: #121212;
    color: #ffffff;
  }

  h2.title-lean {
    font-family: 'Arial', sans-serif;
    font-weight: 300; /* Lean weight */ 
    font-size: 2em;
    color: #ffffff;
    margin: 0.5em 0;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border-bottom: 2px solid #ccc;
    padding-bottom: 0.2em;
  }


  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #1f1f1f;
    padding: 1rem 2rem;
    border-bottom: 2px solid #333;
  }

  .logo {
    display: flex;
    align-items: center;
  }

  .logo img {
    height: 90px;
    margin-right: 1rem;
  }

  .logo span {
    font-size: 1.5rem;
    font-weight: bold;
    color: #ffffff;
  }

  nav {
    display: flex;
    gap: 1rem;
    text-align: center;
    margin: 2rem 0;
  }

  nav a {
    color: #b3b3b3;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
  }

  nav a:hover {
    color: #bb86fc;
  }

  main {
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }

  section {
    margin-bottom: 2rem;
  }

  h2 {
    color: #bb86fc;
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }

  p, ul {
    font-size: 1.1rem;
    margin-bottom: 1rem;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    background: #1f1f1f;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border-radius: 5px;
    border: 1px solid #333;
  }

  .user-section {
    display: flex;
    align-items: center;
  }

  .user-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .user-info img {
    height: 40px;
    border-radius: 50%;
  }

  .user-info span {
    font-size: 1rem;
    color: #ffffff;
  }

  button {
    background: #bb86fc;
    color: #ffffff;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 5px;
    transition: background 0.3s ease;
  }

  button:hover {
    background: #9f68e0;
  }

  footer {
    background: #1f1f1f;
    padding: 1rem 0;
    text-align: center;
    border-top: 2px solid #333;
    position: fixed;
    width: 100%;
    bottom: 0;
  }

  footer p {
    margin: 0;
    font-size: 0.9rem;
  }
</style>
