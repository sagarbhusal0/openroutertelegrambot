from models import models

def get_model_info(user_message):
    """
    Parses the user message and returns the model object if a valid model ID is found.
    """
    for model in models:
        model_id_command = f"/{model.model_id.split('/')[1].split(':')[0].replace('-', '')}"
        if user_message.lower() == model_id_command:
            return model
    return None

def list_available_models():
    """
    Returns a list of tuples containing the modified model ID and the model name.
    """
    return [(model.model_id.split('/')[1].split(':')[0].replace('-', ''), f"{model.name.split(':')[0]}: {model.name.split(':')[1]}") for model in models]