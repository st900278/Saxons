var words = [
  'apple', 'bad', 'cancel', 'delight',
  'entry', 'fault', 'good', 'hunt', 'ignore',
  'jinx', 'know', 'life', 'mortal', 'node',
  'octupus', 'prospect', 'queue', 'relation',
  'section', 'turquoise', 'union', 'value',
  'wander', 'xeon', 'yield', 'zip'
];

var Quiz = function () {
  var INSTANCE = this;
  this.problem = 0;
  this.correct = 0;
  this.correctAnswer = 0
  this.response = {};

  this.swipe = function () {
    var quiz = document.querySelector('#quiz-container-1');
    //$(quiz).removeClass("fadeInRightBig");
    $(quiz).addClass("fadeOutLeftBig").addClass("delay-animate-2s");
  }

  this.nextQuestion = function () {
    INSTANCE.swipe();
    //$('#quiz-container-1').remove();
    return function () {
      INSTANCE.create();
    }();
  };

  this.endQuiz = function () {
    //TODO
  }

  //  this.preload = function () {
  //    var quiz = $("<div class='triple-padded animated blue box' id='quiz-container-2'></div>")
  //    quiz.append($(INSTANCE.showQuestion()));
  //    quiz.append($(INSTANCE.showOption()));
  //    quiz.addClass("fadInRightBig");
  //    return quiz;
  //  }

  this.create = function () {
    this.correctAnswer = words[parseInt((Math.random() * 100), 10) % words.length + 1]
    this.response = {
      def: 'Definition',
      ans: INSTANCE.correctAnswer,
      words: ['fake', this.correctAnswer, 'unreal']
    };
    var quiz = $("<div class='triple-padded animated blue box' id='quiz-container-1'></div>");
    quiz.append($(INSTANCE.showQuestion()));
    quiz.append($(INSTANCE.showOption()));
    quiz.addClass("fadInRightBig");
    $("#container").append(quiz);
    //    $("#container").append(INSTANCE.preload());
  }

  this.showQuestion = function () {
    var question = document.createElement('div');
    var paragraph = document.createElement('p');
    paragraph.innerHTML = INSTANCE.response['def'];
    paragraph.className = "large align-center";
    question.className = "orange box prob";
    question.appendChild(paragraph);
    return question;
  };

  this.showOption = function () {
    var correct;
    var option;
    var paragraph;
    var options = [];
    var i = 0;
    var key;
    for (key in INSTANCE.response["words"]) {
      option = document.createElement('div');
      paragraph = document.createElement('p');
      paragraph.innerHTML = INSTANCE.response['words'][key];
      paragraph.className = "large align-center";
      option.className = "gapped green box opt";
      if (INSTANCE.response['words'][key] === INSTANCE.correctAnswer) {
        option.className += " animated";
        correct = option;
      }
      option.appendChild(paragraph);

      paragraph.addEventListener('click', function (e) {
        var btn = e.target;
        if (btn.innerHTML === INSTANCE.correctAnswer) {
          correct.className += " wobble";
          if (INSTANCE.problem < 5) {
            INSTANCE.problem += 1;
            INSTANCE.nextQuestion();
          } else {
            INSTANCE.endQuiz();
          }
        } else {
          var parent = btn.parentNode;
          parent.className += " red"
          correct.className += " wobble";
          if (INSTANCE.problem < 5) {
            INSTANCE.problem += 1;
            INSTANCE.nextQuestion();
          } else {
            INSTANCE.endQuiz();
          }
        }
      }, false);
      options[i] = option;
      i += 1;
    }
    return options;
  };
}

new Quiz().create();
