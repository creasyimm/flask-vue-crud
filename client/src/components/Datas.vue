<template>

  <div class="container">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <!--
        success, info, warning, danger, dark, light
      -->
      <b-navbar-brand href="#">EEureka</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">CN</b-dropdown-item>
          </b-nav-item-dropdown>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br><br>

    <b-table small bordered :fields="my_tbl_fields" :items="my_items"
     head-variant="light" responsive="sm">

      <template v-slot:cell(type)="data">
        <span v-html="data.value"></span>
      </template>

      <template v-slot:cell(service)="data">
        <div class="col-sm-13 pt-1">
          <b-progress :value="data.value.value" :variant="data.value.variant"
            :key="data.index"></b-progress>
        </div>

      </template>

    </b-table>

  </div>
</template>

<script>
import axios from 'axios';
// import Alert from './Alert.vue';

export default {

  data() {
    return {

      //---------------------
      bars: [
        { variant: 'success', value: 10 },
        { variant: 'info', value: 20 },
        { variant: 'warning', value: 30 },
        { variant: 'danger', value: 40 },
        { variant: 'primary', value: 50 },
        { variant: 'secondary', value: 60 },
        { variant: 'dark', value: 75 },
      ],

      tbl_fields: [
        // A virtual column that doesn't exist in items
        'index',
        // A column that needs custom formatting
        { key: 'name', label: 'Full Name' },
        // A regular column
        'age',
        // A regular column
        'sex',
        // A virtual column made up from two fields
        { key: 'nameage', label: 'First name and age' },
      ],
      items: [
        { name: { first: 'John', last: 'Doe' }, sex: 'Male', age: 42 },
        { name: { first: 'Jane', last: 'Doe' }, sex: 'Female', age: 36 },
        { name: { first: 'Rubin', last: 'Kincade' }, sex: 'Male', age: 73 },
        { name: { first: 'Shirley', last: 'Partridge' }, sex: 'Female', age: 62 },
      ],

      my_tbl_fields: [
        { key: 'type', label: 'Type' },
        { key: 'name', lable: 'Name' },
        { key: 'host', lable: 'Host' },
        { key: 'os', lable: 'Os' },
        { key: 'latency', lable: 'Latency' },
        { key: 'service', lable: 'Service' },
        { key: 'offline', lable: 'Offline' },
        { key: 'ts', lable: 'LastUpdate' },
      ],
      my_items: [],
    };
  },
  components: {
    // alert: Alert,
  },
  methods: {
    getData() {
      // console.log('huihui');
      const path = 'http://192.168.1.137:5000/datas';
      axios.get(path)
        .then((res) => {
          this.my_items = res.data.datas;
          // console.log(res.data.datas);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

  },
  mounted() {
    setInterval(() => {
      this.getData();
    }, 1000);
  },


};
</script>
