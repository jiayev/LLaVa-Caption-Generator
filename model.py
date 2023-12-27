from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
import torch

model, tokenizer, image_processor, context_len = None, None, None, None

def get_device():
    if torch.cuda.is_available():
        return "cuda"
    else:
        return "cpu"
    
def load_model(model_path):
    global model, tokenizer, image_processor, context_len
    print(f"Loading LLaVa model...It takes time.")
    tokenizer, model, image_processor, context_len = load_pretrained_model(
        model_path=model_path,
        model_base=None,
        model_name=get_model_name_from_path(model_path)
    )
    model.to(get_device())  # Move the model to the appropriate device
    print("Finish loading LLaVa model!")
    if model is not None:
        print("Model loaded successfully")
        print(f'Model loaded at id: {id(model)}')
    else:
        print("Failed to load the model")

def unload_model():
    global model, tokenizer, image_processor, context_len
    print("Unloading model")
    del model
    del tokenizer
    del image_processor
    del context_len
    torch.cuda.empty_cache()
    model, tokenizer, image_processor, context_len = None, None, None, None
    print("Finish!")