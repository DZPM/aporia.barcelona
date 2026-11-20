// The header follows the reader and folds once the page has scrolled past the sentinel: fixed at the top, the logo and
// the name smaller, the tagline hidden. CSS does the folding (html.is-scrolled). The script measures the header once,
// so the spacer keeps its place while it is fixed. Without this script, or without IntersectionObserver, the header
// stays in the flow as it is.
(function () {
  var root = document.documentElement;
  document.addEventListener("DOMContentLoaded", function () {
    var header = document.querySelector(".site-header"), sentinel = document.querySelector(".scroll-sentinel");
    if (!header || !sentinel || !("IntersectionObserver" in window)) return;
    function measure() {
      var folded = root.classList.contains("is-scrolled");
      root.classList.remove("is-scrolled");
      root.style.setProperty("--header-h", header.offsetHeight + "px");
      if (folded) root.classList.add("is-scrolled");
    }
    // measure when everything has loaded (the stylesheet and the logo), again when the fonts are in, and on every resize
    addEventListener("load", function () { measure(); root.classList.add("js-header"); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { if (root.classList.contains("js-header")) measure(); });
    addEventListener("resize", measure);
    new IntersectionObserver(function (entries) {
      root.classList.toggle("is-scrolled", !entries[0].isIntersecting);
    }).observe(sentinel);
  });
})();
