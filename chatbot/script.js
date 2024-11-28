document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');
  
    function addMessage(message, type) {
      const messageElement = document.createElement('div');
      messageElement.classList.add('message', type);
      messageElement.textContent = message;
      chatWindow.appendChild(messageElement);
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }
  
    function sendMessage() {
      const message = messageInput.value.trim();
      if (message) {
        addMessage(message, 'outgoing');
        messageInput.value = '';
  
        // Simulate incoming response (replace with actual bot logic)
        setTimeout(() => {
          const responses = [
            'Hello!', 
            'How are you?', 
            'That sounds interesting.', 
            'Tell me more.', 
            'Great!'
          ];
          const response = responses[Math.floor(Math.random() * responses.length)];
          addMessage(response, 'incoming');
        }, 1000);
      }
    }
  
    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        sendMessage();
      }
    });
  });