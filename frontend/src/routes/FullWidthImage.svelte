<script>
  export let src = "backdrop.png";
  export let alt = "Full Width Image";
</script>

<style>
  .full-width-image {
    width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
    padding: 15px;
  }
</style>

<img class="full-width-image" src={src} alt={alt}>
