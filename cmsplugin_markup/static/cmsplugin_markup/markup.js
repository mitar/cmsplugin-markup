// Based on Trac version, http://trac.edgewall.org/

(function($) {
  $.loadStyleSheet = function(href, type) {
    type = type || "text/css";
    $(document).ready(function() {
      if ($('head link[href="' + href + '"]').length == 0) {
        if (document.createStyleSheet) { // MSIE
          document.createStyleSheet(href);
        } else {
          $("<link rel='stylesheet' type='" + type + "' href='" + href + "' />")
            .appendTo("head");
        }
      }
    });
  }
})(jQuery);
