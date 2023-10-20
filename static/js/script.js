const messageBar = document.querySelector(".bar-wrapper input");
const sendBtn = document.querySelector(".bar-wrapper button");
const messageBox = document.querySelector(".message-box");

const API_URL = '/chat';  // Update this URL to match your Flask route


var input = document.querySelector(".bar-wrapper input");

// Execute a function when the user presses a key on the keyboard
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendBtn.click();
  }
});

sendBtn.onclick = function () {
  if (messageBar.value.length > 0) {
    const UserTypedMessage = messageBar.value;
    messageBar.value = "";

    const message =
      `<div class="chat message">
      <img src="static/img/user.jpg">
      <span>
        ${UserTypedMessage}
      </span>
    </div>`;

    const response =
      `<div class="chat response">
      <img src="static/img/chatbot.jpg">
      <span class="new">...
      </span>
    </div>`

    messageBox.insertAdjacentHTML("beforeend", message);

    setTimeout(() => {
      messageBox.insertAdjacentHTML("beforeend", response);

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ "message": UserTypedMessage })
      }

      fetch(API_URL, requestOptions)
        .then(res => res.json())
        .then(data => {
          const ChatBotResponse = document.querySelector(".response .new");
          ChatBotResponse.innerHTML = data.response;
          ChatBotResponse.classList.remove("new");
        })
        .catch((error) => {
          const ChatBotResponse = document.querySelector(".response .new");
          ChatBotResponse.innerHTML = "Oops! An error occurred. Please try again.";
          ChatBotResponse.classList.remove("new");
        });
    }, 100);
  }
}
