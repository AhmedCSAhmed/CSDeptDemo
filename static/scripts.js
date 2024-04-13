document.addEventListener("DOMContentLoaded", function () {
  // Your code here...
  const chatroom = document.getElementById("chatroom");
  var socket = io();
  socket.on("chatroom", function (msg) {
    chatroom.innerHTML += `<div class="row mx-0 mx-5-md"><div class="alert alert-warning" role="alert"><b>${msg['email']}</b><hr /><p>${msg['data']}</p></div></div>`;
    chatroom.scrollTop = chatroom.scrollHeight;
  });
});
