
function validarRegistro() {
    var nombre = document.getElementById("nombre").value;
    var apellidoPaterno = document.getElementById("apellidoPaterno").value;
    var apellidoMaterno = document.getElementById("apellidoMaterno").value;
    var genero = document.getElementById("genero").value;
    var rut = document.getElementById("rut").value;
    var direccion = document.getElementById("direccion").value;
    var correo = document.getElementById("correo").value;
    var telefono = document.getElementById("telefono").value;

    if (nombre == "") {
        alert("El campo nombre es obligatorio");
        return false;
    }
    if (apellidoPaterno == "") {
        alert("El campo apellido paterno es obligatorio");
        return false;
    }
    if (apellidoMaterno == "") {
        alert("El campo apellido materno es obligatorio");
        return false;
    }
    if (genero == "") {
        alert("El campo genero es obligatorio");
        return false;
    }
    if (rut == "") {
        alert("El campo rut es obligatorio");
        return false;
    }
    if (direccion == "") {
        alert("El campo direccion es obligatorio");
        return false;
    }
    if (correo == "") {
        alert("El campo correo es obligatorio");
        return false;
    }
    if (telefono == "") {
        alert("El campo telefono es obligatorio");
        return false;
    }
    return true;
}