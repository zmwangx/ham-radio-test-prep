/* global $ */

$(function () {
  var $document = $(document)
  var $body = $('body')

  var cycleDoneDisplayModes = function () {
    if ($body.hasClass('done-show-titles')) {
      $body.addClass('done-hide').removeClass('done-show-titles')
    } else if ($body.hasClass('done-hide')) {
      $body.addClass('done-show').removeClass('done-hide')
    } else if ($body.hasClass('done-show')) {
      $body.addClass('done-show-titles').removeClass('done-show')
    } else {
      console.warn('body has none of the done-show-titles, done-hide, and done-show classes.')
    }
  }

  $document.on('keypress', function (event) {
    var key = String.fromCharCode(event.which)
    switch (key) {
      case 'a':
        $body.toggleClass('show-answers')
        break
      case 's':
        cycleDoneDisplayModes()
        break
      default:
        break
    }
    return false
  })

  $('.question .title').click(function () {
    $(this).parent().toggleClass('done')
  })
})
