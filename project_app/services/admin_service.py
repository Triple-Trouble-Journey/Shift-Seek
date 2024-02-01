from base_models.admin_model import Admin
from config.db_engine import insert_query, read_query


def get_admin(username) -> None | Admin:
    admin_data = read_query('''
    SELECT a.id, a.username, a.first_name, a.last_name, a.picture, c.email, c.address, c.telephone, c.post_code, l.city, l.country
    FROM admin_list as a, employee_contacts as c, locations as l 
    WHERE a.employee_contacts_id = c.id AND c.locations_id = l.id
    AND a.username = ?
    ''', (username,))

    return next((Admin.from_query_results(*row) for row in admin_data), None)