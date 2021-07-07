var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chatbot/')

// 메세지 전송 함수
// String message
// 채팅에 띄울 메세지 내용
// Bool isBot
// isBot이 Truely한 값인 경우에는 상대방으로 판단하고 메세지 추가
function createChatMessage (message, isBot) {
    if (!message) {
        throw new Error('No message defined!')
    }

    var className = 'chat_log '

    if (isBot) {
        className += 'them'
    } else {
        className += 'me'
    }

    $("#chat_root").append(
      $("<p/>", {
        text: message,
        class: className,
      })
    );

    var root = document.querySelector('#chat_root')

    root.scrollTop = root.scrollHeight
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)
    const message = data.message

    createChatMessage(message, true)
}

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly')
}

document.querySelector('#chat-message-input').focus()
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click()
    }
}

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input')
    var message = messageInputDom.value

    chatSocket.send(JSON.stringify({
        'message': message
    }))

    createChatMessage(message, false)

    messageInputDom.value = ' '
}

function openForm() {
    document.getElementById("myForm").style.display = "block"
}

function closeForm() {
    document.getElementById("myForm").style.display = "none"
}

// DOM이 로드된 이후에 jQuery init
window.addEventListener('DOMContentLoaded', function () { 
    $('.carousel').carousel()
})