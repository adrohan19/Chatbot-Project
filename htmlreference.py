css = '''
<style>
  .chat-container {
    display: flex;
    flex-direction: column;
    max-width: 600px; 
    margin: auto;
  }

  .chat-message {
    display: flex;
    align-items: center;
    padding: 0.75rem;
    border-radius: 20px;
    margin-bottom: 1rem;
    font-size: 16px; 
    color: #fff;
  }

  .chat-message .avatar img {
    width: 50px; 
    height: 50px; 
    border-radius: 50%;
    object-fit: cover;
    margin-right: 1rem;
  }

  .chat-message .avatar {
  width: 60px; 
  height: 60px; 
  border-radius: 50%;
  background-color: #333; /* Or any color that fits your design */
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  color: white; /* Choose a text color that stands out against the avatar background */
}

  .chat-message.user {
    background-color: #2b313e;
    justify-content: flex-end;
    text-align: right;
  }

  .chat-message.user .message {
    order: -1;
    margin-right: 1rem;
  }

  .chat-message.bot {
    background-color: #475063;
    justify-content: flex-start;
    text-align: left;
  }

  .chat-message .message {
    padding: 0.5rem 1rem;
    border-radius: 15px;
    max-width: 80%; /* Ensures text doesn't span the entire width */
  }
</style>
'''
chatbot ='''
  <!-- Bot Message -->
  <div class="chat-message bot">
      <div class="avatar">
          ChatBot
      </div>
      <div class="message">{{MSG}}</div>
'''

user = '''
  <!-- User Message -->
  <div class="chat-message user">
    <div class="avatar">
        User
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''