let messageStyle = "";
let side = "";
const messagesContainer = document.getElementById("messages");
scrollToBottom();
let url = `ws://${window.location.host}/ws/chat/${roomName}/`;
const chatSocket = new WebSocket(url);
function scrollToBottom() {
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

chatSocket.onmessage = function (e) {
  let data = JSON.parse(e.data);

  let userId = parseInt(user_id);

  if (data.type === "chat") {
    let messages = document.getElementById("messages");

    if (data.sender_id === userId) {
      messageStyle = "message-sender";
      side = "sender";
    } else {
      messageStyle = "message-receiver";
      side = "receiver";
    }
    const date = new Date(data.timestamp);
    const options = {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      hour12: true,
    };
    const formattedDate = new Intl.DateTimeFormat("en-US", options).format(
      date
    );

    messages.insertAdjacentHTML(
      "beforeend",
      `<div class="message-container ${side}">
        <div class="message ${messageStyle}">
          <strong>${data.sender}</strong>
          <p>${data.message}</p>
          (${formattedDate})
        </div>
      </div>`
    );
    scrollToBottom();
  }
};

let form = document.getElementById("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let message = e.target.message.value;
  chatSocket.send(
    JSON.stringify({
      message: message,
    })
  );
  form.reset();
});
