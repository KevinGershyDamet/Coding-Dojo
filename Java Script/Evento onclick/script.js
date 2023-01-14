function login_out (accion) {
    if (accion.innerText == "Login") {
        accion.innerText = "Logout"
    } else {
        accion.innerText = "Login"
    }
}

function desaparece (accion) {
    accion.remove()
}

