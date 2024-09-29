class ResponseMessage:
    def __init__(self, icon, title, message) -> None:
        self.icon = icon
        self.title = title
        self.message = message
        
    def makeSuccessInstanceResponseMessage(message=""):
        return ResponseMessage(icon="success", title="Succèss", message=message)
    
    def makeInfoInstanceResponseMessage(message=""):
        return ResponseMessage(icon="info", title="Info", message=message)
    
    def makeErrorInstanceResponseMessage(message=""):
        return ResponseMessage(icon="error", title="Erreur", message=message)
    
    def tojson(self) -> dict:
        return {
            "icon" : self.icon,
            "title": self.title,
            "message": self.message
        }