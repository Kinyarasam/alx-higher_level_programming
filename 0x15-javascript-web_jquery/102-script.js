$('document').ready(function () {
    const API_URL = 'https://www.fourtonfish.com/hellosalut/hello/';
    $('INPUT#btn_translate').click(function () {
        $.get(API_URL + $.param({
            lang: $('INPUT#language_code').val()
        }), function (data) {
            $('DIV#hello').html(data.hello);
        });
    });
});