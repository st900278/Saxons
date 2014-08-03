var packs = $("#lang-packs-container");
var data;

$.ajax({
  url: "static/data/packs.json",
  beforeSend: function (xhr) {
    xhr.overrideMimeType("text/plain; charset=x-user-defined");
  }
}).done(function (response) {
  console.log(response);
  obj = JSON.parse(response);
  data = response;
});

