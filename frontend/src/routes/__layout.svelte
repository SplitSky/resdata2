<script>
    // You can add layout-specific script here
  </script>
  
  <header>
    <nav>
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
      <a href="/blog">Blog</a>
    </nav>
  </header>
  
  <main>
    <slot></slot>
  </main>
  
  <footer>
    <!-- Footer content -->
  </footer>
  
  <style>
    :global(body) {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      color: #333;
      line-height: 1.6;
    }
  
    header {
      background: #333;
      color: #fff;
      padding: 1rem 0;
      text-align: center;
    }
  
    nav a {
      color: #fff;
      text-decoration: none;
      margin: 0 1rem;
      font-weight: bold;
    }
  
    nav a:hover {
      text-decoration: underline;
    }
  
    main {
      padding: 2rem;
      max-width: 800px;
      margin: 0 auto;
    }
  
    footer {
      background: #333;
      color: #fff;
      text-align: center;
      padding: 1rem 0;
      position: absolute;
      bottom: 0;
      width: 100%;
    }
  </style>