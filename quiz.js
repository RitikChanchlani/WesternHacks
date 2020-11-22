const quizContainer = document.getElementById('quiz');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');

function build_quiz()

function show_results()

build_quiz();

submitButton.addEventListener('click', showResults);

const myQuestions = [
    {
      question: "What percent of Canadian parents say their chid has been cyberbullied before?",
      answers: {
        a: "10%",
        b: "15%",
        c: "18%"
      },
      correctAnswer: "c"
    },
    {
      question: "What percent of of Canadian teens with a profile on a social networking site"+ 
      "have seen mean or inappropriate comments about someone they know?",

      answers: {
        a: "10%",
        b: "20%",
        c: "35%"
      },
      correctAnswer: "c"
    },
    {
      question: "What percent of students say teachers intervene?",
      answers: {
        a: "75%",
        b: "50%",
        c: "25%",
      },
      correctAnswer: "c"
    }
  ];

function buildQuiz(){
    const output = [];
  
    myQuestions.forEach(
      (currentQuestion, questionNumber) => {
  
        const answers = [];
  
        for(letter in currentQuestion.answers){
  
          answers.push(
            `<label>
              <input type="radio" name="question${questionNumber}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
          );
                                            }
  
        output.push(
          `<div class="question"> ${currentQuestion.question} </div>
          <div class="answers"> ${answers.join('')} </div>`
        );
      }
    );
    
    myQuestions.forEach( (currentQuestion, questionNumber) => {
      })
      quizContainer.innerHTML = output.join('');

      function showResults(){

        const answerContainers = quizContainer.querySelectorAll('.answers');
      
        let numCorrect = 0;
      
        myQuestions.forEach( (currentQuestion, questionNumber) => {
      
          const answerContainer = answerContainers[questionNumber];
          const selector = `input[name=question${questionNumber}]:checked`;
          const userAnswer = (answerContainer.querySelector(selector) || {}).value;
      
          if(userAnswer === currentQuestion.correctAnswer){
            numCorrect++;
      
            answerContainers[questionNumber].style.color = 'lightgreen';
          }
          else{
            answerContainers[questionNumber].style.color = 'red';
          }
        });
      
        resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
        const answerContainers = quizContainer.querySelectorAll('.answers');

        let numCorrect = 0;

        myQuestions.forEach( (currentQuestion, questionNumber) => {

            const answerContainer = answerContainers[questionNumber];
            const selector = `input[name=question${questionNumber}]:checked`;
            const userAnswer = (answerContainer.querySelector(selector) || {}).value;
          
            if(userAnswer === currentQuestion.correctAnswer){
              numCorrect++;
          
              answerContainers[questionNumber].style.color = 'lightgreen';
            }
            else{
              answerContainers[questionNumber].style.color = 'red';
            }
                                                                  });