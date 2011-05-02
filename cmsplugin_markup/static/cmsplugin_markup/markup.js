// Automatic preview through XHR
// Based on Trac version, http://trac.edgewall.org/

(function($) {
  // Enable automatic previewing to <textarea> elements.
  //
  // Arguments:
  //  - `href`: URL to be called for fetching the preview data.
  //  - `args`: arguments to be passed with the XHR.
  //  - `update`: the function that is called with the preview results. It
  //              is called with the textarea, the text that was rendered and
  //              the rendered text.
  $.fn.autoPreview = function(href, args, update) {
    if (auto_preview_timeout <= 0)
      return this;
    var timeout = auto_preview_timeout * 1000;
    return this.each(function() {
      var timer = null;
      var updating = false;
      var textarea = this;
      var data = {};
      for (var key in args)
        data[key] = args[key];
      data["text"] = textarea.value;
      
      // Request a preview through XHR
      function request() {
        var text = textarea.value;
        if (!updating && (text != data["text"])) {
          updating = true;
          data["text"] = text;
          $.ajax({
            type: "POST", url: href, data: data, dataType: "html",
            success: function(data) {
              updating = false;
              update(textarea, text, data);
              if (textarea.value != text)
                timer = setTimeout(request, timeout);
            },
            error: function(req, err, exc) {
              updating = false;
            }
          });
        }
      }
      
      // Trigger a request after the given timeout
      function trigger() {
        if (!updating) {
          if (timer)
            clearTimeout(timer);
          timer = setTimeout(request, timeout);
        }
        return true;
      }
      
      $(this).keydown(trigger).keypress(trigger).blur(request);
    });
  }
})(jQuery);

(function ($){
  $(document).ready(function(){
      $.fn.cmsPatchCSRF();
  });
})(jQuery);

jQuery(document).ready(function($) {
  // Only if preview exists
  $('#plugin-preview').each(function() {
    var preview = $(this);
    $('#id_body').autoPreview(auto_preview_url, {
        'markup': $('#id_markup').val(),
        'plugin_id': plugin_id,
        'page_id': page_id
      },
      function (textarea, text, data) {
        preview.html(data);
        parent.setiframeheight($('body').height() + 20, 11);
      });
  });
});

// Allow resizing <textarea> elements through a drag bar
// Copied from Trac, http://trac.edgewall.org/

jQuery(document).ready(function($) {
  $('textarea.django-resizable').each(function() {
    var textarea = $(this);
    var offset = null;
    
    function beginDrag(e) {
      offset = textarea.height() - e.pageY;
      textarea.blur();
      $(document).mousemove(dragging).mouseup(endDrag);
      return false;
    }
    
    function dragging(e) {
      textarea.height(Math.max(32, offset + e.pageY) + 'px');
      parent.setiframeheight($('body').height() + 20, 11);
      return false;
    }
    
    function endDrag(e) {
      textarea.focus();
      $(document).unbind('mousemove', dragging).unbind('mouseup', endDrag);
    }
    
    var grip = $('<div class="django-grip"/>').mousedown(beginDrag)[0];
    textarea.wrap('<div class="django-resizable"><div></div></div>')
            .parent().append(grip);
    grip.style.marginLeft = (this.offsetLeft - grip.offsetLeft) + 'px';
    grip.style.marginRight = (grip.offsetWidth - this.offsetWidth) +'px';
  });
});
