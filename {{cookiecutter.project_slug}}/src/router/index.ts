{% if cookiecutter.vue_version == '2' %}
import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import IndexPage from "@/views/pages/IndexPage.vue";

Vue.use(VueRouter);

const routes: RouteConfig[] = [
    {
        path: "/",
        name: "IndexPage",
        component: IndexPage
    }
];

export default new VueRouter({
    routes
});
{% else %}
import {RouteRecordRaw, createRouter, createWebHashHistory} from "vue-router";
import IndexPage from "@/views/pages/IndexPage.vue";

const routes: RouteRecordRaw[] = [
    {
        path: "/",
        name: "IndexPage",
        component: IndexPage
    }
];

export default createRouter({
    history: createWebHashHistory(),
    routes
});
{% endif %}
