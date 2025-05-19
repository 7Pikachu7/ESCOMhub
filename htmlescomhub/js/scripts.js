// Mostrar la fecha actual
document.addEventListener('DOMContentLoaded', function() {
  const fecha = new Date();
  const opciones = { year: 'numeric', month: 'long', day: 'numeric' };
  const elementosFecha = document.querySelectorAll('#fecha-actual');
  
  elementosFecha.forEach(elemento => {
    elemento.textContent = fecha.toLocaleDateString('es-ES', opciones);
  });
});