let messageStyle = "";
let side = "";
let url = `ws://${window.location.host}/ws/chat/${roomName}/`;
const chatSocket = new WebSocket(url);
chatSocket.onmessage = function (e) {
  let data = JSON.parse(e.data);
  console.log("Data:", data);

  if (data.type === "chat") {
    let messages = document.getElementById("messages");
    console.log("sender:", sender);
    console.log("user_id:", user_id);
    if (sender == user_id) {
      messageStyle = "message-sender";
      side = "sender";
    } else if (sender != user_id) {
      messageStyle = "message-receiver";
      side = "receiver";
    }
    messages.insertAdjacentHTML(
      "beforeend",
      `<div
      class="message-container ${side}">
      <div
        class="message ${messageStyle}">
        <strong>${data.sender}</strong>
        <p>${data.message}</p>
        (${data.timestamp})
      </div>
    </div>`
    );
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
