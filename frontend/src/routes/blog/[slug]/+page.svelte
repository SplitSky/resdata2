<script context="module">
export async function load({ params }) {
    // Load the blog post data based on the slug
    const post = await fetchPost(params.slug);
    return { props: { post } };
}
</script>

<script>
export let post;
</script>

<h1>{post.title}</h1>
<p>{post.content}</p>
