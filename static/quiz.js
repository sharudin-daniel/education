console.log("hui")

const url = window.location.href

const taskBox = document.getElementById('task-box')
console.log(taskBox)

let data

$.ajax( {
    type: 'GET',
    url: `${url}data`,
    success: function(response){
    data = response.data
    data.forEach(el => {
        for(const [question, answers] of Object.entries(el)) {
        taskBox.innerHTML += `
            <hr>
            <div class="mb-2">
                <b>${question}</b>
            </div>
        `
            answers.forEach(answer =>{
                taskBox.innerHTML += `
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

const  taskForm = document.getElementById('task-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

// const sendData = () => {
//     const elements = [...document.getElementsByClassName('ans')]
//     const data = {}
//     data['csrfmiddlewaretoken'] = csrf[0].value
//     elements.forEach(el => {
//         if (el.checked) {
//             data[el.name] = el.value
//         } else {
//             if (!data[el.name]) {
//                 data[el.name] = null
//             }
//         }
//     })
// }
// $.ajax( {
//     type: 'POST',
//     url: `${url}results/`,
//     data: data,
//     success: function(response){
//               alert('Оно наконец заработало!')
//         // const results = response.results
//         // taskForm.classList.add('not-visible')
//         //
//         // results.forEach(res => {
//         //     const resDiv = document.createElement("div")
//         //     for (const [question, resp] of Object.entries(res)) {
//         //         resDiv.innerHTML += question
//         //         const cls = ['container-question', 'p-3', 'text-light', 'h6']
//         //         resDiv.classList.add(...cls)
//         //
//         //         if (resp == 'not answered') {
//         //             resDiv.innerHTML += '<ul> <li>Not answered</li></ul>'
//         //             resDiv.classList.add('bg-danger')
//         //         } else {
//         //             const answer = resp['answered']
//         //             const correct = resp['correct_answer']
//         //
//         //             if (answer == correct) {
//         //                 resDiv.classList.add('bg-success')
//         //                 resDiv.innerHTML += `<ul> <li>Answered: ${answer}</li></ul>`
//         //             } else {
//         //                 resDiv.classList.add('bg-danger')
//         //                 resDiv.innerHTML += `<ul> <li>Answered: ${answer}</li></ul>`
//         //                 resDiv.innerHTML += `<ul> <li>Correct answered: ${correct}</li></ul>`
//         //             }
//         //         }
//         //     }
//         //     const content_container = document.getElementsByClassName('content-container')[0]
//         //     content_container.append(resDiv)
//         // })
//     },
//     error: function(error) {
//         console.log(error)
//     }
// })
// }
//
// taskForm.addEventListener('submit', e => {
//     e.preventDefault()
//
//     sendData()
// })