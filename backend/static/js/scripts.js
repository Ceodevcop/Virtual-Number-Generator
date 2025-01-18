document.addEventListener("DOMContentLoaded", () => {
  fetch("/get-number")
    .then(response => response.json())
    .then(data => {
      document.getElementById("virtualNumber").innerText = data.virtual_number;
    });

  setInterval(() => {
    fetch("/receive-sms")
      .then(response => response.json())
      .then(data => {
        const messagesList = document.getElementById("messages");
        messagesList.innerHTML = `<li>From: ${data.from}, Message: ${data.message}</li>`;
      });
  }, 5000);
});
