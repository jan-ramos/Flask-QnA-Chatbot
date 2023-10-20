from flask import Blueprint,current_app, render_template, redirect, url_for, request, flash,session
from .utils.chatflow import document_loader,split_text,vector_storage,get_conversation_chain

upl = Blueprint('upl', __name__)
 
@upl.route('/upl')
def uplbot():
    return render_template('upload.html')
    
@upl.route('/upl', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files.getlist('file')

    if file is None:
        return 'No selected file'

    raw_text = document_loader(file)
    
    if session.get('validation-file') == True:
        text_chunks = split_text(raw_text)
                            
        # Create Vector Store
        vector_store = vector_storage(text_chunks,session.get('api_key') )
        conversation =  get_conversation_chain(vector_store,session.get('api_key'))
        current_app.my_global_variable  = conversation
        
        return redirect(url_for('chat.chatbot'))
    else:
        flash('Invalid File')
        
        return redirect(url_for('upl.uplbot'))