{% if cookiecutter.vue_version == '2' %}
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: () => ({})
});
{% else %}
import {createStore} from "vuex";

export default createStore({
    state: () => ({})
});
{% endif %}
