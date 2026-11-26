class NoCacheMiddleware:
    """
    Middleware que previene que las páginas protegidas
    sean almacenadas en caché por el navegador.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Agregar headers de no-cache a TODAS las respuestas
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        response['Vary'] = 'Cookie'
        
        return response