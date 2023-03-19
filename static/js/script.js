const form = document.querySelector('form');
const themeInput = document.querySelector('#theme');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const response = await fetch('/generate-story', {
    method: 'POST',
    body: formData
  });
  const story = await response.text();
  document.querySelector('#story').innerHTML = story;
  themeInput.value = '';
});
