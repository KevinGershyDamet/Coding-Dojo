
class lista:

    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = nodo(val)
        new_node.next = self.head
        self.head = new_node
        return self
    
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = nodo(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        if self.head == None:
            return None

        current_head = self.head
        self.head = self.head.next
        return current_head

    def remove_from_back(self):
        if self.head == None:
            return None
        
        if self.head.next == None:
            resultado = self.head
            self.head = None
            return resultado

        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        resultado = runner.next
        runner.next = None
        return resultado
    
    def remove_val(self, val):
        if self.head.valor == val:
            self.head = self.head.next
            return self

        runner = self.head
        while runner.next.valor != val:
            runner = runner.next
        runner.next = runner.next.next
        return self
    
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        
        runner = self.head
        for x in range(0,n):
            if runner.next == None:
                runner.next = nodo(val)
                return self
            else:
                current = runner
                runner = runner.next
        current.next = nodo(val)
        current.next.next = runner
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.valor)
            runner = runner.next
        return self


class nodo:

    def __init__(self, val):
        self.valor = val
        self.next = None


listota = lista()
listota.add_to_front('son').add_to_front('Las listas enlazadas').add_to_back('geniales').remove_val('Las listas enlazadas')
listota.print_values()


listita = lista()
listita.add_to_back('Las').add_to_back('listas').add_to_back('enlazadas').add_to_back('son').add_to_back('geniales').print_values()
listita.insert_at('super', 2).print_values()