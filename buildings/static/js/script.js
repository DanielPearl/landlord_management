/**
 * Created by DanielPearl on 11/8/15.
 */

//Show pencil edit
$("li a").hover(function() {
    $(function() {
    $('li a').hover(function() {
        $('span').show();
    }, function() {
        $('span').hide();
    });
});
});

//Show tooltip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
    })