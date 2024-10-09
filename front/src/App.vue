<!-- frontend/src/App.vue -->

<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: 'Loading...'
    };
  },
  mounted() {
    axios.get('/api/')
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.log(error);
        this.message = 'Error fetching data';
      });
  }
};
</script>
