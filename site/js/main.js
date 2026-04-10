$(function(){
  // Header fixed on scroll + logo swap
  var $header = $('header');
  var $logo = $('#js-header-main-logo');
  var logoDefault = $logo.attr('src');
  var logoFixed = (function(){
    var scripts = document.getElementsByTagName('script');
    for(var i = 0; i < scripts.length; i++){
      var src = scripts[i].src;
      if(src.indexOf('main.js') !== -1){
        return src.replace('js/main.js', 'css/header-logo002.svg');
      }
    }
    return '/css/header-logo002.svg';
  })();

  $(window).on('scroll', function(){
    if($(this).scrollTop() > 100){
      if(!$header.hasClass('header-fixed')){
        $header.addClass('header-fixed');
        $logo.attr('src', logoFixed);
      }
    } else {
      if($header.hasClass('header-fixed')){
        $header.removeClass('header-fixed');
        $logo.attr('src', logoDefault);
      }
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
