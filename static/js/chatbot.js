var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chatbot/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data['message'];
    const chat_log =  document.querySelector('#chat-log')
    chat_log.value += ('Bot : ' + message + '\n');
    chat_log.scrollTop = chat_log.scrollHeight;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    document.querySelector('#chat-log').value += ('나 : ' + message + '\n');

    messageInputDom.value = ' ';
};

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
$('.carousel').carousel()