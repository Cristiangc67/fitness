let messageStyle = "";
let side = "";
const messagesContainer = document.getElementById("messages");
scrollToBottom();
let url = `ws://${window.location.host}/ws/chat/${roomName}/`;
const chatSocket = new WebSocket(url);

function scrollToBottom() {
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

chatSocket.onopen = function () {
  console.log("WebSocket connection opened");
};

chatSocket.onclose = function () {
  console.log("WebSocket connection closed");
};

chatSocket.onmessage = function (e) {
  let data = JSON.parse(e.data);
  let userId = parseInt(user_id);

  if (data.type === "chat") {
    if (data.deleted_at) {
      console.log("Mensaje eliminado, no mostrarlo.");
      return; // No mostrar el mensaje
    }
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
    console.log(data.id);

    messages.insertAdjacentHTML(
      "beforeend",
      `<div class="message-container ${side}" data-message-id="${
        data.message_id
      }">
        <div class="message ${messageStyle}">
          <strong>${data.sender}</strong>
          <p>${data.message}</p>
          (${formattedDate})
          ${
            data.sender_id === userId
              ? `<button class="delete-message btn btn-danger" data-message-id="${data.message_id}">Eliminar</button>`
              : ""
          }
        </div>
      </div>`
    );
    scrollToBottom();
  } else if (data.type === "delete_message") {
    console.log(`Message ID to delete: ${data.message_id}`);
    const messageElement = document.querySelector(
      `.message-container[data-message-id="${data.message_id}"]`
    );
    console.log(messageElement);
    if (messageElement) {
      messageElement.remove();
    }
  }
};

// Manejar la eliminación de mensajes
document.addEventListener("click", function (event) {
  if (event.target && event.target.classList.contains("delete-message")) {
    const messageId = event.target.getAttribute("data-message-id");
    console.log(`Message ID to delete: ${messageId}`);

    chatSocket.send(
      JSON.stringify({
        action: "delete_message",
        message_id: messageId,
      })
    );
  }
});

// Enviar mensaje cuando se envía el formulario
let form = document.getElementById("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let message = e.target.message.value;

  chatSocket.send(
    JSON.stringify({
      action: "send_message", // Añade explícitamente el campo 'action'
      message: message,
    })
  );
  form.reset();
});
