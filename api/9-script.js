/*
It is observed that the url given does not allow cross origin.
However this can be bypassed by using a proxy server specified below.
*/

const url = 'https://localhost:8001/api/accounts/1';
$.get(url, function (response) {
  const hello = response.address;
  $('DIV#hello').text(hello);
});
