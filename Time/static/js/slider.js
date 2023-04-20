$(document).ready(function() {
    const slides = $('.slides');
    const slide = $('.slide');
    const prevBtn = $('.prev');
    const nextBtn = $('.next');
    let counter = 1;
    const size = slide.outerWidth();
  
    slides.css('transform', 'translateX(' + (-size * counter) + 'px)');
  
    nextBtn.click(function() {
      if (counter >= slide.length - 1) return;
      slides.css('transition', 'transform 0.5s ease-in-out');
      counter++;
      slides.css('transform', 'translateX(' + (-size * counter) + 'px)');
    });
  
    prevBtn.click(function() {
      if (counter <= 0) return;
      slides.css('transition', 'transform 0.5s ease-in-out');
      counter--;
      slides.css('transform', 'translateX(' + (-size * counter) + 'px)');
    });
  
    slides.on('transitionend', function() {
      if (slide[counter].id === 'lastClone') {
        slides.css('transition', 'none');
        counter = slide.length - 2;
        slides.css('transform', 'translateX(' + (-size * counter) + 'px)');
      }
      if (slide[counter].id === 'firstClone') {
        slides.css('transition', 'none');
        counter = slide.length - counter;
        slides.css('transform', 'translateX(' + (-size * counter) + 'px)');
      }
    });
  });