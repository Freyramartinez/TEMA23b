# Escribe debajo el codigo de la clase LinkedList y sus respectivos metodos     
# Recuerda importar la clase Node en este script
# LinkedList_sandbox.py
# LinkedList_sandbox.py

from Node import Node

class LinkedList:
    def __init__(self, value=None):
        # Establecer el nodo cabeza
        self.head_node = Node(value)

    def get_head_node(self):
        # Devolver el nodo cabeza
        return self.head_node

    def insert_beginning(self, new_value):
        # Crear un nuevo nodo con el nuevo valor
        new_node = Node(new_value)
        # Hacer que el next_node del nuevo nodo apunte al nodo cabeza actual
        new_node.next_node = self.head_node
        # Actualizar el nodo cabeza para que sea el nuevo nodo
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""  # Inicializar cadena vacía para almacenar los valores
        current_node = self.head_node  # Comenzar desde el nodo cabeza
        
        while current_node is not None:  # Recorrer hasta que current_node sea None
            if current_node.value is not None:  # Verificar que el valor no sea None
                string_list += str(current_node.value) + "\n"  # Concatenar el valor
            current_node = current_node.next_node  # Avanzar al siguiente nodo
        
        return string_list  # Devolver la cadena construida

    def remove_node(self, value_to_remove):
        current_node = self.head_node  # Iniciar desde el nodo cabeza
        # Verificar si el nodo cabeza tiene el valor a eliminar
        if current_node is not None and current_node.value == value_to_remove:
            # Ajustar el nodo cabeza al siguiente nodo
            self.head_node = current_node.next_node
            return

        # Recorrer la lista buscando el valor a eliminar
        while current_node is not None:
            next_node = current_node.next_node
            if next_node is not None and next_node.value == value_to_remove:
                # Ajustar enlaces para eliminar el nodo
                current_node.next_node = next_node.next_node
                return
            current_node = next_node  # Avanzar al siguiente nodo