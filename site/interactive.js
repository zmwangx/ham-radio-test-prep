/* global $ */

$(function () {
  var $document = $(document)
  var $body = $('body')

  $document.on('keypress', function (event) {
    var key = String.fromCharCode(event.which)
    switch (key) {
      case 'a':
        if ($body.hasClass('show-answers')) {
          $body.removeClass('show-answers')
        } else {
          $body.addClass('show-answers')
        }
        break
      default:
        break
    }
  })
})
