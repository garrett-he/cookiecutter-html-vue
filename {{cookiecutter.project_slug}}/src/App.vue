{% if cookiecutter.vue_version == '3' %}
<script lang="ts" setup>
import MainView from "./views/MainView.vue";
</script>
{% endif %}
<template>
    <main-view/>
</template>

{% if cookiecutter.vue_version == '2' %}
<script lang="ts">
import MainView from "./views/MainView.vue";

export default {
    name: "App",
    components: {
        MainView
    }
};
</script>
{% endif %}
