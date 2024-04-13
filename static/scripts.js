document.addEventListener("DOMContentLoaded", function () {
  // Your code here...
  var socket = io();
  socket.on('connect', function() {
      console.log('Connected!');
      socket.emit('chatroom', {data: 'I\'m connected!'});
  });
});
