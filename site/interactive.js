/* global $, localStorage */

$(function () {
  var $window = $(window)
  var $document = $(document)
  var $body = $('body')
  var $status = $('#status')

  var cycleDoneDisplayModes = function () {
    var status
    if ($body.hasClass('done-show-titles')) {
      $body.addClass('done-hide').removeClass('done-show-titles')
      status = 'Hidden'
    } else if ($body.hasClass('done-hide')) {
      $body.addClass('done-show').removeClass('done-hide')
      status = 'Shown'
    } else if ($body.hasClass('done-show')) {
      $body.addClass('done-show-titles').removeClass('done-show')
      status = 'Question bodies hidden'
    } else {
      console.warn('body has none of the done-show-titles, done-hide, and done-show classes.')
      return
    }
    $status.clearQueue()
    $status.text(status).fadeIn(200).delay(500).fadeOut(200)
  }

  var saveState = function () {
    localStorage.setItem('showAnswers', $body.hasClass('show-answers'))
    var doneIDs = $.map($('.question.done'), function (elem) { return $(elem).attr('id') })
    localStorage.setItem('doneIDs', JSON.stringify(doneIDs))
    ;['done-show-titles', 'done-hide', 'done-show'].forEach(function (mode) {
      if ($body.hasClass(mode)) {
        localStorage.setItem('doneDisplayMode', mode)
      }
    })
    localStorage.setItem('scroll', $window.scrollTop())
    localStorage.setItem('stateSaved', 'true')
  }

  var restoreState = function () {
    if (localStorage.getItem('stateSaved') !== 'true') {
      return
    }
    $body.toggleClass('show-answers', localStorage.getItem('showAnswers') === 'true')
    var mode = localStorage.getItem('doneDisplayMode')
    $body.removeClass('done-show-titles').removeClass('done-hide').removeClass('done-show')
      .addClass(mode)
    JSON.parse(localStorage.getItem('doneIDs')).forEach(function (id) {
      $('#' + id).addClass('done')
    })
    $window.scrollTop(parseInt(localStorage.getItem('scroll')))
  }

  restoreState()
  ;['pagehide', 'beforeunload', 'unload'].forEach(function (eventname) {
    $window.on(eventname, saveState)
  })
  $window.on('pageshow', restoreState)

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
    saveState()
    return false
  })

  $('.question .title').click(function () {
    $(this).parent().toggleClass('done')
    saveState()
  })
})
