import {createApp} from "vue";
import App from "./App.vue";

import router from "./router";
{% if cookiecutter.with_vuex == 'yes' %}
import store from "./store";
{% endif %}

createApp(App)
    .use(router)
    {% if cookiecutter.with_vuex == 'yes' %}
    .use(store)
    {% endif %}
    .mount("#app");
