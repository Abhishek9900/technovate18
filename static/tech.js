
$(document).ready(function(){
  $(".button-collapse").sideNav();
});
$(document).ready(function(){
      $('#joinID').click(function(){
        $('.button-collapse').sideNav('hide');
      });
   });
$(document).ready(function () {
$('#sponsors').hide("fast");
$('#aboutus').hide("fast");
$('#tech-team').hide("fast");
$('#title').hide("fast");

$('#tevents').show();
$('#workshop').hide();
$('.acc-desc').hide();
$('.homelink').click(function(){
    $('#sponsors').hide("slow");
    $('#aboutus').hide("slow");
    $('#tevents').hide("slow");
    $('#workshop').hide("slow");
    $('.my-reg-button').show("fast");
    $('#tech-team').hide("slow");
    $('#dashboard').hide();
    $('#why').show();
    $('.button-collapse').sideNav('hide');
    $('#title').show("slow");

    $('#tevn1').hide();
    $('#tevn2').hide();
    $('#tevn3').hide();
    $('#tevn4').hide();
    $('#tevn5').hide();
    $('#tevn7').hide();
    $('#tevn8').hide();
    $('#tevn6').hide();
    $('#ntevn1').hide();
    $('#ntevn2').hide();
    $('#ntevn3').hide();
    $('#ntevn4').hide("slow");

});

$('.indexlink').click(function () {
    $('#tevents').hide("slow");
    $('#sponsors').hide("slow");
    $('#aboutus').hide("slow");
    $('#workshop').hide("slow");
    $('#tech-team').hide();
    $('.button-collapse').sideNav('hide');
    $('.my-reg-button').show("fast");
    $('#title').show("slow");
    $('#why').show();

    $('#tevn1').hide();
    $('#tevn2').hide();
    $('#tevn3').hide();
    $('#tevn4').hide();
    $('#tevn5').hide();
    $('#tevn6').hide();
    $('#tevn7').hide();
    $('#tevn8').hide();
    
    $('#ntevn1').hide();
    $('#ntevn2').hide();
    $('#ntevn3').hide();
    $('#ntevn4').hide("slow");
});
$('.sponsorslink').click(function () {
    $('#tevents').hide("slow");
    $('#title').hide("slow");
    $('#aboutus').hide("slow");
    $('.my-reg-button').hide("fast");
    $('#tech-team').hide();
    $('#workshop').hide("slow");
    $('.button-collapse').sideNav('hide');
    $('#sponsors').slideToggle("slow");
    $('#why').show();


    $('#tevn1').hide();
    $('#tevn2').hide();
    $('#tevn3').hide();
    $('#tevn4').hide();
    $('#tevn5').hide();
    $('#tevn6').hide();
    $('#tevn7').hide();
    $('#tevn8').hide();

    $('#ntevn1').hide();
    $('#ntevn2').hide();
    $('#ntevn3').hide();
    $('#ntevn4').hide("slow");
});
$('.aboutlink').click(function () {
    $('#tevents').hide("slow");
    $('#sponsors').hide("slow");
    $('#title').hide("slow");
    $('#tech-team').hide();
    $('.my-reg-button').hide("fast");
    $('.button-collapse').sideNav('hide');
    $('#workshop').hide("slow");
    $('#aboutus').show("slow");
    $('#why').show();


    $('#tevn1').hide();
    $('#tevn2').hide();
    $('#tevn3').hide();
    $('#tevn4').hide();
    $('#tevn5').hide();
    $('#tevn6').hide();
    $('#tevn7').hide();
    $('#tevn8').hide();

    $('#ntevn1').hide();
    $('#ntevn2').hide();
    $('#ntevn3').hide();
    $('#ntevn4').hide("slow");
});
$('.teamlink').click(function() {
    $('#tevents').hide("slow");
    $('#sponsors').hide("slow");
    $('#title').hide("slow");
    $('#workshop').hide("slow");
    $('#aboutus').hide("slow");
    $('.my-reg-button').hide("fast");
    $('.button-collapse').sideNav('hide');
    $('#tech-team').slideDown("slow");
    $('#why').show();


    $('#tevn1').hide();
    $('#tevn2').hide();
    $('#tevn3').hide();
    $('#tevn4').hide();
    $('#tevn5').hide();
    $('#tevn6').hide();
    $('#tevn7').hide();
    $('#tevn8').hide();

    $('#ntevn1').hide();
    $('#ntevn2').hide();
    $('#ntevn3').hide();
    $('#ntevn4').hide("slow");
});
$('.techeventslink').click(function(){
  $('#dashboard').hide("fast");
  $('#sponsors').hide("fast");
  $('.my-reg-button').hide("fast");
  $('#workshop').hide("slow");
  $('#title').hide("fast");
  $('#aboutus').hide("fast");
  $('.button-collapse').sideNav('hide');
  $('#tech-team').hide("slow");
  $('#why').show();
  $('#tevents').show("fast");

  $('#tevn1').hide();
  $('#tevn2').hide();
  $('#tevn3').hide();
  $('#tevn4').hide();
  $('#tevn5').hide();
  $('#tevn6').hide();
  $('#tevn7').hide();
  $('#tevn8').hide();

  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide();
  $('#ntevn4').hide("slow");
});
$('.workshoplink').click(function(){
  $('#title').hide("slow");
  $('#sponsors').hide("slow");
  $('.my-reg-button').hide("fast");
  $('#aboutus').hide("slow");
  $('#tech-team').hide("slow");
  $('#why').show();
  $('#dashboard').hide();
  $('.button-collapse').sideNav('hide');
  $('#tevents').hide("slow");
  $('#workshop').show("slow");

  $('#tevn1').hide();
  $('#tevn2').hide();
  $('#tevn3').hide();
  $('#tevn4').hide();
  $('#tevn5').hide();
  $('#tevn6').hide();
  $('#tevn7').hide();
  $('#tevn8').hide();

  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide();
  $('#ntevn4').hide("slow");
});
$('#tevn1').show();
$('#tevn2').hide();
$('#tevn3').hide();
$('#tevn4').hide();
$('#tevn5').hide();
$('#tevn6').hide();
$('#tevn7').hide();
$('#tevn8').hide();
$('#ntevn1').hide();
$('#ntevn2').hide();
$('#ntevn3').hide();
$('#ntevn4').hide("slow");

$('#tevnl1').click(function() {
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn6').hide("slow");
  $('#tevn8').hide();
  $('#tevn5').hide("slow");
  $('#tevn7').hide();

  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");

  $('#tevn1').show("slow");
});
$('#tevnl2').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn8').hide();
  $('#tevn5').hide("slow");
  $('#tevn6').hide("slow");
  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");
  $('#tevn7').hide();

  $('#tevn2').show("slow");

});
$('#tevnl3').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn6').hide("slow");
  $('#tevn8').hide();
  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#tevn7').hide();
  $('#ntevn4').hide("slow");

  $('#tevn3').show("slow");
});
$('#tevnl4').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn6').hide("slow");
  $('#ntevn1').hide();
  $('#tevn8').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");
  $('#tevn7').hide();

  $('#tevn4').show("slow");
});
$('#tevnl5').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn6').hide("slow");
  $('#tevn8').hide();
  $('#ntevn1').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#tevn7').hide();
  $('#ntevn4').hide("slow");

  $('#tevn5').show("slow");
});
$('#tevnl6').click(function () {
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn8').hide();
  $('#tevn5').hide("slow");
  $('#ntevn1').hide();
  $('#tevn7').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");

  $('#tevn6').show("slow");
});
$('#tevnl7').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn8').hide();
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#ntevn1').hide();
  $('#tevn6').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");

  $('#tevn7').show("slow");
});
$('#tevnl8').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn7').hide();
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#ntevn1').hide();
  $('#tevn6').hide();
  $('#ntevn2').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");

  $('#tevn8').show("slow");
});
$('#ntevnl1').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn8').hide();
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn6').hide("slow");
  $('#tevn7').hide();
  $('#ntevn3').hide("slow");
  $('#ntevn2').hide("slow");
  $('#ntevn4').hide("slow");

  $('#ntevn1').show("slow");
});
$('#ntevnl2').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn7').hide();
  $('#tevn8').hide();
  $('#tevn6').hide("slow");
  $('#ntevn1').hide("slow");
  $('#ntevn3').hide("slow");
  $('#ntevn4').hide("slow");

  $('#ntevn2').show("slow");
});
$('#ntevnl3').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn8').hide();
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn6').hide("slow");
  $('#tevn7').hide();
  $('#ntevn1').hide("slow");
  $('#ntevn2').hide("slow");
  $('#ntevn4').hide("slow");

  $('#ntevn3').show("slow");
});
$('#ntevnl4').click(function(){
  $('#tevn1').hide("slow");
  $('#tevn2').hide("slow");
  $('#tevn3').hide("slow");
  $('#tevn4').hide("slow");
  $('#tevn5').hide("slow");
  $('#tevn8').hide();
  $('#tevn6').hide("slow");
  $('#ntevn1').hide("slow");
  $('#tevn7').hide();
  $('#ntevn2').hide("slow");
  $('#ntevn3').hide("slow");

  $('#ntevn4').show("slow");
});


});
$(document).ready(function(){
$('.tooltipped').tooltip({delay: 50});
});
$(document).ready(function(){
// the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
$('.modal-trigger').leanModal();
});

$(document).ready(function(){
$('.carousel.carousel-slider').carousel({full_width: true});
});
$(document).ready(function(){
$('.carousel').carousel();
});
$(document).ready(function(){
$('fixed-action-btn').openFAB();
});