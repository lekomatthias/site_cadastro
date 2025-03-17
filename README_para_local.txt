PARA COLOCAR O SEVIÇO DISPONÍVEL COM CLOUDFLARE BASATA ABRIR DOIS TERMINAIS (a porta 8080 é arbitrária):

 - python manage.py runserver 0.0.0.0:8080 (PARA DISPONIBILIZAR O SERVIÇO)
 - cloudflared tunnel --url http://localhost:8080 (PARA O TUNNELAMENTO CLOUDFLARE)

com isso devo colocar o link no arquivo em cadastro_app/settings.py:
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    # posso colocar qlqr outro endereço aqui para permitir o acesso externo
]
