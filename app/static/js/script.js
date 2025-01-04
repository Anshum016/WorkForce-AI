document.querySelector(".tour-button").addEventListener("click", function (e) {
    e.preventDefault(); // Prevent the default jump to the element
    document.getElementById("timeline-background").scrollIntoView({
      behavior: "smooth", // Smooth scrolling effect
      block: "start",     // Scroll to the top of the element
    });
  });
  