document.getElementById('emocion-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const frase = document.getElementById('frase').value;

  const formData = new FormData();
  formData.append('frase', frase);

  const response = await fetch('https://detector-emociones-production.up.railway.app/api/detectar', {
    method: 'POST',
    body: formData,
  });

  const data = await response.json();
  document.getElementById('resultado').innerText = 'Emoción detectada: ' + data.emocion;
});
