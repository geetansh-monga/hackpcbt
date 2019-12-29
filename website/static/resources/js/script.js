// Carousal for the our team section
$(".owl-carousel").owlCarousel({
  loop: true,
  margin: 30,
  nav: false,
  stagePadding: 20,
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 2
    },
    1000: {
      items: 3
    }
  }
});

// section-about-animations
var tl = new TimelineMax({ onUpdate: updatePercentage });
const controller = new ScrollMagic.Controller();

tl.from(".page-heading", 1.5, { y: 200, opacity: 0 });
tl.from(".page-content", 1, { x: 400, opacity: 0 });

const scene = new ScrollMagic.Scene({
  triggerElement: ".section-about",
  triggerHook: "onLeave",
  duration: "100%"
})

  .setPin(".section-about")
  .setTween(tl)
  .addTo(controller);

function updatePercentage() {
  tl.progress();
  console.log(tl.progress());
}

// animation-section-schedule

var tl2 = new TimelineMax({ onUpdate: updatePercentage });
const controller2 = new ScrollMagic.Controller();

tl2.from(".head-one", 1.5, { y: 200, opacity: 0 });
tl2.from(".timeline-block-right", 6, { y: -400, opacity: 0 });

const scene2 = new ScrollMagic.Scene({
  triggerElement: ".sticky",
  triggerHook: "onLeave",
  duration: "100%"
})

  .setPin(".sticky")
  .setTween(tl2)
  .addTo(controller2);

function updatePercentage() {
  tl2.progress();
  console.log(tl2.progress());
}

// animation-section-sponsors

var tl3 = new TimelineMax({ onUpdate: updatePercentage });
const controller3 = new ScrollMagic.Controller();

tl3.from(".sponsor-head", 3, { x: 400, opacity: 0 });
tl3.from(".gallery", 3, { y: 400, opacity: 0 });

const scene3 = new ScrollMagic.Scene({
  triggerElement: ".section-sponsors",
  triggerHook: "onLeave",
  duration: "100%"
})

  .setPin(".section-sponsors")
  .setTween(tl3)
  .addTo(controller3);

function updatePercentage() {
  tl3.progress();
  console.log(tl3.progress());
}

//section-ourteam

var tl4 = new TimelineMax({ onUpdate: updatePercentage });
const controller4 = new ScrollMagic.Controller();

// tl4.from(".owl-wrapper", 1.5, { y: 200, opacity: 0 });
tl4.from(".section-ourteam", 3, { y: 400, opacity: 0 });
// tl4.from(".owl-wrapper", 3, { y: 400, opacity: 0 });
tl4.from(".owl-wrapper", 6, { opacity: 0, scale: 0 });

const scene4 = new ScrollMagic.Scene({
  triggerElement: ".section-ourteam",
  triggerHook: "onLeave",
  duration: "100%"
})

  .setPin(".section-ourteam")
  .setTween(tl4)
  .addTo(controller4);

function updatePercentage() {
  tl4.progress();
  console.log(tl4.progress());
}

var tl5 = new TimelineMax({ onUpdate: updatePercentage });
const controller5 = new ScrollMagic.Controller();

// tl4.from(".owl-wrapper", 1.5, { y: 200, opacity: 0 });
tl5.from(".anime-faq", 3, { x: 400, opacity: 0 });
tl5.from(".col-anime", 3, { x: -400, opacity: 0 });

const scene5 = new ScrollMagic.Scene({
  triggerElement: ".section-faq",
  triggerHook: "onLeave",
  duration: "100%"
})

  .setPin(".section-faq")
  .setTween(tl5)
  .addTo(controller5);

function updatePercentage() {
  tl5.progress();
  console.log(tl5.progress());
}
