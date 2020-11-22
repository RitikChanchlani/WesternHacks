function generateQuiz(questions, quizContainer, resultsContainer, submitButton){

  var myQuestions = [
    {
      question: "What percent of Canadian parents say their chid has been cyberbullied before?",
  
      answers: {
        a: '10',
        b: '18',
        c: '15'
      },
      correctAnswer: 'b'
    },
    {
      question: "What percent of of Canadian teens with a profile on a social networking site"+ 
      "have seen mean or inappropriate comments about someone they know??",
      answers: {
        a: '10',
        b: '20',
        c: '35'
      },
      correctAnswer: 'c'
    }
  ];


	function showQuestions(questions, quizContainer){
	    var output = [];
	    var answers;
	    for(var i=0; i<questions.length; i++){
			    answers = [];
		      for(letter in questions[i].answers){
			        answers.push(
				     '<label>'
					   + '<input type="radio" name="question'+i+'" value="'+letter+'">'
					   + letter + ': '
					   + questions[i].answers[letter]
				     + '</label>'
			);
		}
		    output.push(
			 '<div class="question">' + questions[i].question + '</div>'
			 + '<div class="answers">' + answers.join('') + '</div>'
		);
	}
	quizContainer.innerHTML = output.join('');
}
	showQuestions(questions, quizContainer);

	function showResults(questions, quizContainer, resultsContainer){
    var output = [];
    var answers;
  
    for(var i=0; i<questions.length; i++){
      
      answers = [];
  
      for(letter in questions[i].answers){
  
        answers.push(
          '<label>'
            + '<input type="radio" name="question'+i+'" value="'+letter+'">'
            + letter + ': '
            + questions[i].answers[letter]
          + '</label>'
        );
      }
  
      output.push(
        '<div class="question">' + questions[i].question + '</div>'
        + '<div class="answers">' + answers.join('') + '</div>'
      );
    }
  
    quizContainer.innerHTML = output.join('');
  }

	showQuestions(questions, quizContainer);
  
	function showResults(questions, quizContainer, resultsContainer){
	
    var answerContainers = quizContainer.querySelectorAll('.answers');
    
    var userAnswer = '';
    var numCorrect = 0;
    
    for(var i=0; i<questions.length; i++){
  
      userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;
      
      if(userAnswer===questions[i].correctAnswer){
        numCorrect++;
        
        answerContainers[i].style.color = 'lightgreen';
      }
      else{
        answerContainers[i].style.color = 'red';
      }
    }
  
    resultsContainer.innerHTML = numCorrect + ' out of ' + questions.length;
  }
  submitButton.onclick = function(){
    showResults(questions, quizContainer, resultsContainer);
  }
  var quizContainer = document.getElementById('quiz');
  var resultsContainer = document.getElementById('results');
  var submitButton = document.getElementById('submit');
generateQuiz(myQuestions, quizContainer, resultsContainer, submitButton);
}
