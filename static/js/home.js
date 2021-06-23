new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        news: []
    },
    mounted: function () {
        this.getNews();
    },
    methods: {
      getNews: function () {
        fetch('/api/v1/news/')
            .then(function(response) {
              return response.json();
            })
            .then((json) => {
                this.news = json;
            });
      }
    }
})