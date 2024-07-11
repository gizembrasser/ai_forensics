# Get the models from the textfiles
def load_models(models_file):
    with open(models_file, 'r') as file:
        models = file.read().strip().split(',')
    return [model.strip() for model in models]
