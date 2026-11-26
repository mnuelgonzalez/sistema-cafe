class NoCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Agregar headers de no-cache a TODAS las respuestas
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0, post-check=0, pre-check=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        response['Vary'] = 'Cookie, Authorization'
        
        # Línea de verificación (puedes verla en la consola)
        if not request.user.is_authenticated:
            print(f"Middleware: Usuario NO autenticado - Headers no-cache aplicados")
        
        return response