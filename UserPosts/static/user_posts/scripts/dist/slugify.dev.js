"use strict";

/*const titleInput = documents.querySelector('input[name=title]');
const SlugInput = documents.querySelector('input[name=slug]');

const slugify = (val) => {
    return val .toString().toLowerCase().trim()
        .replace(/&/g,'-and-') // replace & with -a-
        .replace(/[\s\W-]+/g , '-') // replace space, non word chars and dashes me 1 dash
    };

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value',slugify(titleInput.value));
});*/
var titleInput = document.querySelector('input[name=title]');
var slugInput = document.querySelector('input[name=slug]');

var slugify = function slugify(val) {
  return val.toString().toLowerCase().trim().replace(/&/g, '-and-') // Replace & with 'and'
  .replace(/[\s\W-]+/g, '-'); // Replace spaces, non-word characters and dashes with a single dash (-)
};

titleInput.addEventListener('keyup', function (e) {
  slugInput.setAttribute('value', slugify(titleInput.value));
});