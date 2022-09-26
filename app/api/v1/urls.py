from app.api.v1 import api as api_v1
from app.api.v1.repositories.ram_calculator import get_list_of_ram

api_v1.add_url_rule('/ram/list/<int:last_n_minutes>', view_func=get_list_of_ram, methods=['GET'])
