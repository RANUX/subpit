const URL = 'http://localhost:8000';
const btnSend = document.querySelector('.btn-send');
const response = document.querySelector('.response');
const emailInput = document.querySelector('.email');
const error = document.querySelector('.error')

btnSend.addEventListener('click', async () => {
  let userData = {
    email: emailInput.value,
    host: window.location.host
  }
  try {
    const resp = await fetch(`${URL}/subs/create/`, {
      method: 'POST',
      body: JSON.stringify(userData),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await resp.json();
    displayData(data);
  } catch (err) {
    displayError(err);
  }
});

function displayData(data) {
  response.textContent = JSON.stringify(data);
}

function displayError(err) {
  error.textContent = err;
}