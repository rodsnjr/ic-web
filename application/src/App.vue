<template>
  <div id="app" class="page-container">
    <md-app md-mode="reveal">
      <md-app-toolbar class="md-primary">
        <!-- Menu Open Button -->
        <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
          <md-icon>menu</md-icon>
        </md-button>
        <span class="md-title">Hello {{user}}</span>
      </md-app-toolbar>

      <div class="md-toolbar-section-end">
        Test
      </div>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>
        <Menu></Menu>
      </md-app-drawer>

      <md-button class="md-icon-button">
        <md-icon>menu</md-icon>
      </md-button>

      <md-app-content>
        <Activity></Activity>
      </md-app-content>
    </md-app>
  </div>
</template>

<style lang="scss" scoped>
  .md-app {
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
</style>

<script>
import Menu from './components/Menu.vue';
import Activity from './components/Activity.vue';

export default {
  name: 'App',
  components: {
    Menu,
    Activity,
  },
  data: () => ({
    menuVisible: false,
    user: 'Rodney',
  }),
};
</script>
