"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),  
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),  
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
            "id": self._generate_id(),  
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }    
        ]

    # Este método genera un identificador incremental único.
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método.
        ## Añade el miembro a la lista de miembros
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name

        self._members.append(member)    

    def delete_member(self, id):
        ## Debes implementar este método.
        ## Recorre la lista y elimina el miembro con el ID dado.
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        ### Debes implementar este método.
        ## Recorre todos los miembros y devuelve el que tenga el id dado.
        for member in self._members:
            if member["id"] == id:
                return member
        return None    

    # Este método está terminado, devuelve una lista con todos los miembros de la familia.
    def get_all_members(self):
        return self._members