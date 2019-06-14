import re

URL = 'http://compras.dados.gov.br/materiais/v1/materiais.html'

DATABASE_CONN = 'mongodb+srv://{user}:{password}@cluster0-1gfrp.gcp.mongodb.net/test?retryWrites=true&w=majority'
DATABASE = 'inventory'
COLLECTION = 'materials'

attributes_properties = {
    'Código do Item': {
        'field': 'item_id',
        'parser': lambda x: int(x)
    },
    'Descrição do Item': {
        'field': 'item_description',
        'parser': lambda x: re.sub(r'\s{2,}', '', x)
    },
    'Grupo': {
        'field': 'item_group',
        'parser': lambda x: x.contents[0].strip()
    },
    'Classe': {
        'field': 'item_class',
        'parser': lambda x: x.contents[0].strip()
    },
    'PDM': {
        'field': 'pdm',
        'parser': lambda x: x.contents[0].strip()
    },
    'Status': {
        'field': 'status',
        'parser': lambda x: x
    },
    'Sustentável': {
        'field': 'is_sustainable',
        'parser': lambda x: {'Não': False, 'Sim': True}.get(x)
    }
}
