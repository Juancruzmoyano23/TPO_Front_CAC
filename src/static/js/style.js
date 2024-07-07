document.getElementById('form').addEventListener('submit', function(event) {
    let valid = true;

    // Validación de nombre, apellido y ciudad
    const fieldsToValidate = ['firstname', 'lastname', 'ubi'];
    fieldsToValidate.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        const errorField = document.getElementById(fieldId + 'Error');
        const fieldValue = field.value.trim();
        if (fieldValue === '' || /\d/.test(fieldValue)) {
            errorField.textContent = 'Este campo no puede estar vacío ni contener números.';
            valid = false;
        } else {
            errorField.textContent = '';
        }
    });

    // Dirección (solo verificar que no esté vacía)
    const direccion = document.getElementById('dire').value;
    const direccionError = document.getElementById('direError');
    if (direccion.trim() === '') {
        direccionError.textContent = 'La dirección es obligatoria.';
        valid = false;
    } else {
        direccionError.textContent = '';
    }

    // Email (validación de formato)
    const email = document.getElementById('email').value;
    const emailError = document.getElementById('emailError');
    const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = 'Por favor, introduce un email válido.';
        valid = false;
    } else {
        emailError.textContent = '';
    }

    // Código Postal (validación de rango)
    const codigoPostal = document.getElementById('code').value;
    const codigoPostalError = document.getElementById('codeError');
    if (codigoPostal.trim() === '' || isNaN(codigoPostal) || codigoPostal < 1 || codigoPostal > 9999) {
        codigoPostalError.textContent = 'Por favor, introduce un código postal válido.';
        valid = false;
    } else {
        codigoPostalError.textContent = '';
    }

    // Fecha de Nacimiento (solo verificar que no esté vacía)
    const fechaNacimiento = document.getElementById('nacimiento').value;
    const fechaNacimientoError = document.getElementById('nacimientoError');
    if (fechaNacimiento.trim() === '') {
        fechaNacimientoError.textContent = 'La fecha de nacimiento es obligatoria.';
        valid = false;
    } else {
        fechaNacimientoError.textContent = '';
    }

    if (!valid) {
        event.preventDefault();
    }
});

