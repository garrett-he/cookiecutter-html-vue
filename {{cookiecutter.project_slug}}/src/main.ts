{% if cookiecutter.vue_version == '2' %}
import Vue from "vue";
import App from "./App.vue";

import router from "./router";
{%- if cookiecutter.with_vuex == 'yes' %}
import store from "./store";
{%- endif %}

new Vue({
    router,
    {%- if cookiecutter.with_vuex == 'yes' %}store,{%- endif %}
    render: h => h(App)
}).$mount("#app");
{% else %}
import {createApp} from "vue";
import App from "./App.vue";

import router from "./router";
{%- if cookiecutter.with_vuex == 'yes' %}
import store from "./store";
{%- endif %}

createApp(App)
    .use(router)
    {%- if cookiecutter.with_vuex == 'yes' %}.use(store){%- endif %}
    .mount("#app");
{% endif %}
