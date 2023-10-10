import path from "path";
import {defineConfig} from "vitest/config";
import vue from "@vitejs/plugin-vue";

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
