{% if cookiecutter.vue_version == '2' %}
declare module "*.vue"
{
    import Vue from "vue";
    export default Vue;
}
{% else %}
declare module "*.vue"
{
    import {defineComponent} from "vue";
    const Component: ReturnType<typeof defineComponent>;
    export default Component;
}
{% endif %}
