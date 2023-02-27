<template>
    <div class="index-page">
        <h1>Hello, world!</h1>
    </div>
</template>

{% if cookiecutter.vue_version == '2' %}
<script lang="ts">
export default {
    name: "IndexPage"
};
</script>
{% endif %}

<style lang="stylus" scoped>
h1
    color #900
</style>
