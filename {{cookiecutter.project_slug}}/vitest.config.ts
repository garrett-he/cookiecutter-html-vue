import path from "path";
import {defineConfig} from "vitest/config";
{% if cookiecutter.vue_version == '2' %}
import vue from "@vitejs/plugin-vue2";
{% else %}
import vue from "@vitejs/plugin-vue";
{% endif %}

export default defineConfig({
    test: {
        environment: "jsdom"
    },
    plugins: [
        vue()
    ],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "src")
        }
    }
});
