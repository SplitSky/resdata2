<script>
    let posts = [
      { title: "My First Post", slug: "my-first-post" },
      { title: "Another Post", slug: "another-post" }
    ];
</script>
  
<h1>Blog</h1>
<ul>
{#each posts as post}
    <li><a href={`/blog/${post.slug}`}>{post.title}</a></li>
{/each}
</ul>
