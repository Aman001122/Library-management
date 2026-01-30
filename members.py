members = []

def add_member(member_id, name):
    members.append({
        "id": member_id,
        "name": name,
        "issued_books": [],
        "fine": 0
    })

def get_all_members():
    return members
