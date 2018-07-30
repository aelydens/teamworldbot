var game = {
  init: function() {
    game.setUp();
  },

  setUp: function() {
    $('#guess').on('input', game.checkGuess);
    $('#guess').on('input', game.updateProgress);
  },

  checkGuess: function() {
    const answer = $('#puzzle').data('value');

    if ($('#guess').val().toLowerCase() == answer.toLowerCase()) {
      $('#guess').val(answer);
      $('#guess').addClass('winner');
      $('#guess').prop('disabled', true);
      $('.game.alert-success').show();
    }
  },

  updateProgress: function() {
    const answer = $('#puzzle').data('value');
    const guess = $('#guess').val()

    var numCorrect = 0;
    for (var i = 0; i < answer.length; i++) {
      if (guess[i] === answer[i]) {
        numCorrect++;
      }
    }

    var percentCorrect = Math.floor((numCorrect / answer.length) * 100);
    var percentIncorrect = 100 - percentCorrect;
    $('.guess-progress').text(game.toPercent(percentCorrect));
    $('.progress-bar.bg-success').css("width", game.toPercent(percentCorrect));
    $('.progress-bar.bg-danger').css("width", game.toPercent(percentIncorrect));
  },

  toPercent: function(num) {
    return num + "%";
  }
}

$(document).ready(function() {
  game.init();
})
