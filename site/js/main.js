$(function(){
  // Header fixed on scroll + logo swap
  var $header = $('header');
  var $logo = $('#js-header-main-logo');
  var logoDefault = $logo.attr('src');
  var isHome = $('#body-in').hasClass('home');
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

  // Non-home pages: always use logo002 and header-fixed
  if(!isHome){
    $header.addClass('header-fixed');
    $logo.attr('src', logoFixed);
  }

  $(window).on('scroll', function(){
    if(isHome){
      // Home: swap logo on scroll
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

  // Column slider (carousel)
  if($('#column-slider').length){
    var spMode = $(window).width() <= 767;
    $('#column-slider').bxSlider({
      auto: true,
      pause: 4000,
      speed: 600,
      mode: 'horizontal',
      slideWidth: spMode ? 280 : 370,
      minSlides: spMode ? 1 : 3,
      maxSlides: spMode ? 1 : 3,
      moveSlides: 1,
      slideMargin: spMode ? 12 : 24,
      pager: true,
      controls: true,
      nextText: '<span class="column-slider-next">&rsaquo;</span>',
      prevText: '<span class="column-slider-prev">&lsaquo;</span>',
      touchEnabled: true,
      infiniteLoop: true
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
