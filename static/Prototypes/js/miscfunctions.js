$(function showOrHideClock() {
    $('.showButton').click(function () {
        $('.hiddenn').show();
        $('.showclock').hide();
    });
    $('.hideButton').click(function () {
        $('.hiddenn').hide();
        $('.showclock').show();
    });
});