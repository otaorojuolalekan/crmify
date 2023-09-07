const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (response) {
  const listMovies = $('#list_movies');
  const films = response.results;
  films.forEach(film => {
    const title = film.title;
    // const description = film.opening_crawl;
    // can be used to append the opening crwal as a paragragh
    // by adding ".append($('<p>').text(description))"
    const liTitle = $('<li>').text(title);
    listMovies.append(liTitle);
  });
});

// const url = "https://swapi-api.alx-tools.com/api/films/?format=json";

// $.get(url, function (data) {
//   const films = data.results;
//   const listMovies = $("#list_movies");

//   films.forEach(function (film) {
//     const li = $("<li>");
//     li.text(film.title);
//     listMovies.append(li);
//   });
// });
