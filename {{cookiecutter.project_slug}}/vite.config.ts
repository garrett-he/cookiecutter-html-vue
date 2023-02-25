import path from "path";
{% if cookiecutter.vue_version == '2' %}
import vue from "@vitejs/plugin-vue2";
{% else %}
import vue from "@vitejs/plugin-vue";
{% endif %}

export default {
    plugins: [
        vue()
    ],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "src")
        }
    }
};
