<script>
    import FullWidthImage from './FullWidthImage.svelte';
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
      <a href="/documentation">Documentation</a>
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
        <FullWidthImage src='backdrop.png' alt="full width front page" />
    </div>

</section>
<section class="overview">
    <h2> What is ResData? </h2>
    <p> Resdata2 is a comprehensive full-stack implementation of a data pipeline API. It is designed to allow for a quick and simple deployment of a data architecture and integration of it with lab equipment to allow a continuous dashboard/analysis as data comes in. This project started as a way of using the technology that's openly available and putting together a simple system that stops you from having to carry a USB stick from a lab to your office. It's simple, free (for small teams) and most importantly it allows for easy programmatic integration with existing code. It's quite literally just an API wrapped with a nice web UI.</p>
</section>

<section class="features">
  <h2>Features</h2>
  <div class="features-list">
    <div class="feature-item">
      <strong>Data Ingestion:</strong>
      <span>Easily upload and organize data from various sources.</span>
    </div>
    <div class="feature-item">
      <strong>Real-Time Analysis:</strong>
      <span>Analyze data on-the-fly with integrated Jupyter Notebook support.</span>
    </div>
    <div class="feature-item">
      <strong>Scalable Storage:</strong>
      <span>Efficient data storage with MongoDB and flat file support.</span>
    </div>
    <div class="feature-item">
      <strong>User Management:</strong>
      <span>Manage team access and permissions with role-based controls.</span>
    </div>
    <div class="feature-item">
      <strong>API Integration:</strong>
      <span>Seamlessly integrate with lab equipment and other tools.</span>
    </div>
    <div class="feature-item">
      <strong>Secure Data:</strong>
      <span>Ensure data security with advanced encryption and authentication mechanisms.</span>
    </div>
     <div class="feature-item">
      <strong>Use Local Storage:</strong>
      <span>Allows for integration of your local server if you want to keep data on premises</span>
    </div>   
  </div>
</section>
<section>
  <h2> Let's get started! </h2>
  <button>Get Started</button>
</section>
</main>

<footer>
  <div class="footer-social-media">
    Resdata2 2024 - Contact us:  
    <a href="https://x.com/TomekNeska"><img class="tiny-icons" src="twitter_icon.png" alt="Twitter"></a>
    <a href="https://www.linkedin.com/in/tomasz-neska-444476187/"><img class="tiny-icons" src="linkedIn.png" alt="LinkedIn"></a>
    <a href="https://github.com/SplitSky"><img class="tiny-icons" src="github.png" alt="GitHub"></a>
  </div>
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

  .features {
    text-align: center;
  }
  
  .features-list {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .feature-item {
    display: flex;
    justify-content: flex-start;
    width: 100%;
    padding: 10px 0;
    border-bottom: 1px solid #333;
  }
  
  .feature-item strong {
    flex-basis: 200px;
    text-align: left;
  }
  
  .feature-item span {
    flex-grow: 1;
    text-align: left;
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
    margin: 0.5rem 0;
    padding: 0.5rem;
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
    padding: 0.9rem 0;
    text-align: center;
    border-top: 2px solid #333;
    position: fixed;
    width: 100%;
    bottom: 0;
  }

  footer p {
    margin: 0;
    font-size: 0.8rem;
  }

  img.tiny-icons {
    height: 20px;
  }
</style>
