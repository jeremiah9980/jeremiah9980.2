/**
 * Google Analytics / Google tag bootstrap for this static GitHub Pages site.
 *
 * Measurement ID: G-0H9QRFPRQF
 *
 * Each HTML page references this file with a relative path. Keeping the
 * measurement ID here avoids duplicating the full gtag snippet across every
 * page and makes future analytics changes a one-file edit.
 */
(function () {
  var measurementId = "G-0H9QRFPRQF";

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };

  window.gtag("js", new Date());
  window.gtag("config", measurementId);

  var tag = document.createElement("script");
  tag.async = true;
  tag.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(measurementId);
  document.head.appendChild(tag);
})();
