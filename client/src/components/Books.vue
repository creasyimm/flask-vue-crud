<template>

  <div class="container">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <!--
        success, info, warning, danger, dark, light
      -->
      <b-navbar-brand href="#">NavBar</b-navbar-brand>

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

            <!-- Using 'button-content' slot
          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
            -->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br><br>
      <div v-for="bar in bars" class="row mb-1">
          <div class="col-sm-2">{{ bar.variant }}:</div>
          <div class="col-sm-10 pt-1">
            <b-progress :value="bar.value" :variant="bar.variant" :key="bar.variant"></b-progress>
        </div>
      </div>
    <br><br>

    <b-table small bordered :fields="my_tbl_fields" :items="my_items" responsive="sm">
      <template v-slot:cell(service)="data">
        <div class="col-sm-13 pt-1">
          <b-progress :value="data.value.value" :variant="data.value.variant" :key="data.index"></b-progress>
        </div>

      </template>
    </b-table>

    <b-table small :fields="tbl_fields" :items="items" responsive="sm">
      <!-- A virtual column -->
      <template v-slot:cell(index)="data">
        {{ data.index + 1 }}
      </template>

      <!-- A custom formatted column -->
      <template v-slot:cell(name)="data">
        <b class="text-info">{{ data.value.last.toUpperCase() }}</b>, <b>{{ data.value.first }}</b>
      </template>

      <!-- A virtual composite column -->
      <template v-slot:cell(nameage)="data">
        {{ data.item.name.first }} is {{ data.item.age }} years old
      </template>

      <!-- Optional default data cell scoped slot -->
      <template v-slot:cell()="data">
        <i>{{ data.value }}</i>
      </template>
    </b-table>

    <div class="row">
      <div class="col-sm-10">
        <!--
        <h1>Books</h1>
        <hr><br><br>
      -->
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Type</th>
              <th scope="col">Name</th>
              <th scope="col">Host</th>
              <th scope="col">OS</th>
              <th scope="col">CPU</th>
              <th scope="col">Memory</th>
              <th scope="col">Disk</th>
              <th scope="col">Service</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.price }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.book-update-modal
                          @click="editBook(book)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteBook(book)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
            id="book-modal"
            title="Add a new book"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
            id="book-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
// import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';

export default {
  // components: {
  //   BIcon,
  //   BIconArrowUp,
  //   BIconArrowDown
  // },
  // mounted() {
  //   this.timer = setInterval(() => {
  //     this.bars.forEach(bar => (bar.value = 25 + Math.random() * 75))
  //   }, 2000)
  // },
  // beforeDestroy() {
  //   clearInterval(this.timer)
  //   this.timer = null
  // },
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
          { variant: 'dark', value: 75 }
        ],
        // timer: null,

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
        { key: 'nameage', label: 'First name and age' }
      ],
      items: [
        { name: { first: 'John', last: 'Doe' }, sex: 'Male', age: 42 },
        { name: { first: 'Jane', last: 'Doe' }, sex: 'Female', age: 36 },
        { name: { first: 'Rubin', last: 'Kincade' }, sex: 'Male', age: 73 },
        { name: { first: 'Shirley', last: 'Partridge' }, sex: 'Female', age: 62 }
      ],

      my_tbl_fields: [
        { key: 'type', label: 'Type' },
        { key: 'name', lable: 'Name'},
        { key: 'host', lable: 'Host'},
        { key: 'os', lable: 'Os'},
        { key: 'cpu', lable: 'CPU'},
        { key: 'memory', lable: 'Memory'},
        { key: 'disk', lable: 'Disk'},
        { key: 'service', lable: 'Service'}
      ],
      my_items: [
        {type: 'BareMetal', name: 'TestEnv', host: '172.16.75.249', os: 'Esxi 6.7', cpu: 0.6, 
          memory: 0.3, disk: 0.5, service: { variant: 'success', value: 10 }},
        {type: 'BareMetal', name: 'DevEnv', host: '172.16.75.223', os: 'Esxi 6.7', cpu: 0.6, 
          memory: 0.3, disk: 0.5, service: { variant: 'warning', value: 30 }},
      ],

      //---------------------
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
    editBook(book) {
      this.editForm = book;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.id);
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks(); // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.id);
    },

    getData() {
      console.log('huihui')
      const path = 'http://localhost:5000/datas';
      axios.get(path)
        .then((res) => {
          this.my_items = res.data.datas;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    // this.getBooks();
    let timer = setInterval(() => {
      this.getData();
    }, 1000);
  },
};
</script>
