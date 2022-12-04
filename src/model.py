class Model():
    def __init__(self,model_path=''):
        self.model_path=model_path
    def getMock(self):
        return [
            {'text' : 'בראשית ברא אלוהים את ','predictions':None},
            {'text':'?','predictions':[{'value':'השמיים','p':0.8},{'value':'הידיים','p':0.1}]},
            {'text': ' ואת הא', 'predictions': None},
            {'text': '?', 'predictions': [{'value': 'ר', 'p': 0.86}, {'value': 'מ', 'p': 0.69}]},
            {'text': 'ץ', 'predictions': None},
        ]