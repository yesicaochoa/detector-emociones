document.getElementById('emocion-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const frase = document.getElementById('frase').value;

  const formData = new FormData();
  formData.append('frase', frase);

  const response = await fetch('https://detector-emociones-production.up.railway.app/', {
    method: 'POST',
    body: formData,
  });

  const html = await response.text();
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');

  const emocion = doc.querySelector('h2').innerText;
  document.getElementById('resultado').innerText = emocion;
});
