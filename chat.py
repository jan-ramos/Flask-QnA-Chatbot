from flask import current_app,request, jsonify, render_template,Blueprint, render_template, request,session
import openai

chat = Blueprint('chat', __name__)

@chat.route('/chat')
def chatbot():
    return render_template('index.html')

@chat.route('/chat', methods=['POST'])
def chatconv():
    user_typed_message = request.json.get('message')
    
    openai.api_key = session.get('api_key')

    conversation = current_app.my_global_variable
    response = conversation({"question": user_typed_message})


    chatbot_response = response['answer']
    return jsonify({'response': chatbot_response})

