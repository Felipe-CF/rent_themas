
from .models import Client, Rent, Theme

class CalcularDesconto:

    def desconto(dia, cliente_id, tema_id):
        cliente = Cliente.objects.get(id=id_cliente)

        historico = Rent.objects.filter(client=cliente).count()

        tema = Theme.objects.get(pk=tema_id)

        if historico > 0:           
            desconto = 0.9

        if dia_semana < 4:
            desconto = 0.5
        
        return tema.valor * desconto
