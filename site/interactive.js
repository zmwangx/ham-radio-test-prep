/* global $ */

$(function () {
  var $document = $(document)
  var $body = $('body')

  $document.on('keypress', function (event) {
    var key = String.fromCharCode(event.which)
    switch (key) {
      case 'a':
        $body.toggleClass('show-answers')
        break
      default:
        break
    }
  })
})
