$(function(){
  // Header fixed on scroll
  var $header = $('header');
  $(window).on('scroll', function(){
    if($(this).scrollTop() > 100){
      $header.addClass('header-fixed');
    } else {
      $header.removeClass('header-fixed');
    }
  });

  // bxSlider init (top page)
  if($('#mainvisual').length){
    $('#mainvisual').bxSlider({
      auto: true,
      pause: 5000,
      speed: 800,
      mode: 'fade',
      pagerCustom: null,
      controls: false,
      touchEnabled: true,
      adaptiveHeight: true
    });
  }
  if($('#mainvisual-sp').length){
    $('#mainvisual-sp').bxSlider({
      auto: true,
      pause: 5000,
      speed: 800,
      mode: 'fade',
      controls: false,
      touchEnabled: true,
      adaptiveHeight: true
    });
  }

  // News tab switching
  var $tabs = $('.news-tab-list h3');
  var $contents = $('#tab-area > div');
  if($tabs.length){
    $tabs.first().addClass('active');
    $contents.hide().first().show();
    $tabs.on('click', function(e){
      e.preventDefault();
      var idx = $tabs.index(this);
      $tabs.removeClass('active');
      $(this).addClass('active');
      $contents.hide().eq(idx).fadeIn(300);
    });
  }

  // Scroll to top
  $('.footer-floating-btn').on('click', function(e){
    e.preventDefault();
    $('html, body').animate({scrollTop: 0}, 600);
  });

  // SP footer menu toggle
  $('.js-footer-button').on('click', function(){
    var target = '#' + $(this).data('target');
    $(target).toggleClass('open');
  });

  // Footer bg click to close
  $('#js-footer-bg').on('click', function(){
    $('.footer__sp-nav-wrapper').removeClass('open');
  });
});
