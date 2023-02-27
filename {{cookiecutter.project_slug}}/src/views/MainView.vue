<template>
    <div class="main-view">
        <router-view/>
    </div>
</template>

{% if cookiecutter.vue_version == '2' %}
<script lang="ts">
export default {
    name: "MainView"
};
</script>
{% endif %}
