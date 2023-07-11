const form = document.querySelector('form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const subjectInput = document.getElementById('subject');
const messageInput = document.getElementById('message');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  // Validar nombre
  if (nameInput.value.trim() === '') {
    setErrorFor(nameInput, 'El nombre no puede estar vacío');
  } else {
    setSuccessFor(nameInput);
  }
  
  // Validar correo electrónico
  if (emailInput.value.trim() === '') {
    setErrorFor(emailInput, 'El correo electrónico no puede estar vacío');
  } else if (!isValidEmail(emailInput.value.trim())) {
    setErrorFor(emailInput, 'El correo electrónico no es válido');
    } else {
    setSuccessFor(emailInput);
    }
    
    // Validar teléfono
    if (phoneInput.value.trim() === '') {
    setErrorFor(phoneInput, 'El teléfono no puede estar vacío');
    } else {
    setSuccessFor(phoneInput);
    }
    
    // Validar asunto
    if (subjectInput.value.trim() === '') {
    setErrorFor(subjectInput, 'El asunto no puede estar vacío');
    } else {
    setSuccessFor(subjectInput);
    }
    
    // Validar mensaje
    if (messageInput.value.trim() === '') {
    setErrorFor(messageInput, 'El mensaje no puede estar vacío');
    } else {
    setSuccessFor(messageInput);
    }
    
    // Si no hay errores, enviar formulario
    if (isFormValid()) {
    form.submit();
    }
    });
    
    function setErrorFor(input, errorMessage) {
    const formControl = input.parentElement;
    const errorElement = formControl.querySelector('.error');
    
    errorElement.innerText = errorMessage;
    formControl.classList.add('error');
    formControl.classList.remove('success');
    }
    
    function setSuccessFor(input) {
    const formControl = input.parentElement;
    
    formControl.classList.add('success');
    formControl.classList.remove('error');
    }
    
    function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
    return emailRegex.test(email);
    }
    
    function isFormValid() {
    return document.querySelectorAll('.error').length === 0;
    }
