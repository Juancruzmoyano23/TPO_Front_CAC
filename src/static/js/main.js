const form_recetas = document.querySelector("form")

form_recetas.addEventListener('submit', (event) => {
    event.preventDefault()

    const firstname = form_recetas["firstname"].value
    const lastname = form_recetas["lastname"].value
    
    //console.log(form_recetas)
    //const formData = new FormData(form_recetas)
   // const data = Object.fromEntries(formData)
    //console.log(data)

})

/*
const firstname = form_recetas["firstname"].value
const lastname = form_recetas["lastname"].value
const dire = form_recetas["dire"].value
const email = form_recetas["email"].value
const ubi = form_recetas["ubi"].value
const code = form_recetas["code"].value
const nacimiento = form_recetas["nacimiento"].value



const response = await fetch('/api/recetas', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        firstname: firstname,
        lastname: lastname,
        dire: dire,
        email: email,
        ubi: ubi,
        code: code,
        nacimiento: nacimiento
    })
})

const data = await response.json()
console.log(data)
*/