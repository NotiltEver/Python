document.getElementById('generate-btn').addEventListener('click', function() {
  const length = parseInt(document.getElementById('length').value);
  const includeLowercase = document.getElementById('lowercase').checked;
  const includeUppercase = document.getElementById('uppercase').checked;
  const includeDigits = document.getElementById('digits').checked;
  const includeSpecial = document.getElementById('special').checked;

  let characters = '';
  if (includeLowercase) {
    characters += 'abcdefghijklmnopqrstuvwxyz';
  }
  if (includeUppercase) {
    characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  }
  if (includeDigits) {
    characters += '0123456789';
  }
  if (includeSpecial) {
    characters += '!@#$%^&*()_+[]{}|;:,.<>?';
  }

  if (characters === '') {
    document.getElementById('password').value = 'Välj minst en teckentyp!';
    return;
  }

  let password = '';
  for (let i = 0; i < length; i++) {
    password += characters.charAt(Math.floor(Math.random() * characters.length));
  }

  document.getElementById('password').value = password;
});
