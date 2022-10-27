$('document').ready(function () {
    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').focus(function () {
        $(this).keydown(function (e) {
            if (e.keyCode === 13) {
                translate();
            }
        });
    });
  });
  
function translate () {
    const API_URL = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(API_URL + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
    });
}