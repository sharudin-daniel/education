console.log("hui")

const url = window.location.href

const quizBox = document.getElementById('quiz-box')
console.log(quizBox)

let data

$.ajax( {
    type: 'GET',
    url: `${url}data`,
    success: function(response){
    data = response.data
    data.forEach(el => {
        for(const [question, answers] of Object.entries(el)) {
        quizBox.innerHTML += `
            <hr>
            <div class="mb-2">
                <b>${question}</b>
            </div>
        `
            answers.forEach(answer =>{
                quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>
                `
            })
        }
    });
    },
    error: function (error){
        console.log(error)
    }
})

const  quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if(!data[el.name]) {
                data[el.name] = null
            }
        }
    })

$.ajax( {
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function(response){
        const results = response.results
        quizForm.classList.add('not-visible')

        results.forEach(res => {
            const resDiv = document.createElement("div")
            for (const [question, resp] of Object.entries(res)) {
                resDiv.innerHTML += question
                const cls = ['container-question', 'p-3', 'text-light', 'h6']
                resDiv.classList.add(...cls)

                if (resp == 'not answered') {
                    resDiv.innerHTML += '<br> not answered'
                    resDiv.classList.add('bg-danger')
                } else {
                    const answer = resp['answered']
                    const correct = resp['correct_answer']

                    if (answer == correct) {
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML += `<br> answered: ${answer}`
                    } else {
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML += ` <br> correct answered: ${correct}`
                        resDiv.innerHTML += ` <br> answered: ${answer}`

                    }
                }
            }
            const content_container = document.getElementsByClassName('content-container')[0]
            content_container.append(resDiv)
        })
    },
    error: function(error) {
        console.log(error)
    }
})
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
})