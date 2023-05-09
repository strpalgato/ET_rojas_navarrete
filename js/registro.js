
const formulario = document.forms["formulario"];
formulario.addEventListener("submit", validarRegistro);
function validarRegistro(event) {

    event.preventDefault();

    const nombre = formulario["nombre"].value;
    const apellidoPaterno = formulario["apellidoPaterno"].value;
    const apellidoMaterno = formulario["apellidoMaterno"].value;
    const genero = formulario["genero"].value;
    const rut = formulario["rut"].value;
    const direccion = formulario["direccion"].value;
    const correo = formulario["correo"].value;
    const telefono = formulario["telefono"].value;

  if (nombre.length < 3 || nombre.length > 20) {
    alert("El nombre debe tener entre 3 y 20 caracteres.");
    return false;
  }
  if (apellidoPaterno.length < 3 || apellidoPaterno.length > 20) {
    alert("El apellido paterno debe tener entre 3 y 20 caracteres.");
    return false;
  }
  if (apellidoMaterno.length < 3 || apellidoMaterno.length > 20) {
    alert("El apellido materno debe tener entre 3 y 20 caracteres.");
    return false;
  }
  if (genero === "") {
    alert("Debe seleccionar un género.");
    return false;
  }
  if (rut === "") {
    alert("Debe ingresar su rut.");
    return false;
  }

  if (rut.length != 10) {
    alert("El rut debe tener 10 caracteres.");
    return false;
  }

  if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) {
    alert("El rut ingresado no es válido.");
    return false;
  }

    if (direccion === "") {
    alert("Debe ingresar su dirección.");
    return false;
  }
  if (telefono.length < 9 || telefono.length > 12) {
    alert("El celular debe tener entre 9 y 12 caracteres.");
    return false;
  }
  if (correo === "") {
    alert("Debe ingresar su correo electrónico.");
    return false;
  }
  alert("El formulario ha sido enviado correctamente."); 
  return true;
}