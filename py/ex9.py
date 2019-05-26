#!/bin/python

## Lista Duplamente Ligada
class List:
    def __init__(self):
        self.first_node = None

    def __str__(self):
        """Metodo especial que eh chamado quando o print() eh usado no objeto."""
        node = self.first_node
        string = ''
        while node is not None:
            string += f'{node.value} '  # string = string + f'{node.value} '
            node = node.next
        return string

    def __len__(self):
        """Implementar o tamanho a lista."""
        node = self.first_node
        size = 0
        while node is not None:
            node = node.next
            size += 1
        return size

    def add_sorted(self, value):
        """Usar essa adicao desde o inicio para manter lista ligada."""
        pass

    def addat_end(self, value):
        """Adiciona ao final da lista ligada."""
        # TODO Exercicio: Adicionar apenas elementos nao repetidos

        # Cria-se novo node.
        new_node = Node(value)

        if not self.empty():  # Se a lista nao eh vazia.
            # Var auxiliar para nao perder referencia do primeiro node.
            node = self.first_node
            # Se o "campo next" nao eh None continuamos andando na lista para
            # chegar ao ultimo node.
            while node.next is not None:
                node = node.next
            # Quando o "node" auxiliar esta com "node.next == None"
            # atribuimos a "node.next" o novo node.
            node.next = new_node
        else:  # Se a lista esta vazia, o novo node eh o primeiro node.
            self.first_node = new_node

    def addat_start(self, value):
        """Adiciona ao comeco da lista ligada."""
        new_node = Node(value)
        new_node.next = self.first_node  # Novo node ja aponta para o primeiro.
        self.first_node = new_node  # Primeiro node se torna o novo node.

    def search(self, value):
        """Retorna posicao de value na lista caso encontre; caso contrario
        retorna False
        """
        node = self.first_node
        i = 0
        while node is not None:
            if node.value == value:
                return i
            node = node.next
            i += 1
        return False

    def update(self, value, new_value):
        """Retorna True se o node da lista foi atualizado; caso contrario
        retorna False.
        """
        node = self.first_node
        while node is not None:
            if node.value == value:
                node.value = new_value
                return True
            node = node.next
        return False

    def remove(self, value):
        """Return true if the value was found and removed; otherwise False."""
        # Se a lista nao estiver vazia, procura-se value para remover.
        if not self.empty():
            # Unico caso em que temos que atualizar o primeiro node, eh quando
            # o primeiro node precisa ser removido.
            if self.first_node.value == value:
                node = self.first_node  # Primeiro node de remocao eh armazenado.
                # Atualiza-se o primeiro node para o proximo.
                self.first_node = self.first_node.next
                del node  # Remove-se o node em questao.
                return True
            else:
                prev_node = self.first_node  # Node anterior precisa ser salvo.
                node = prev_node.next  # Node auxiliar para checagem.
                while node is not None:  # Enquanto nao chegar ao fim da lista.
                    if node.value == value:  # Se encontrar o valor.
                        # Node anterior aponta para o proximo do node a ser removido.
                        prev_node.next = node.next
                        del node  # Exclui-se o node auxiliar.
                        return True  # Retorna para parar de andar na lista
                    # Percorre-se a lista atualizado os dois nodes.
                    prev_node = node
                    # prevo_node = prev_node.next
                    node = node.next
        return False

    def remove_first(self, value):
        if self.first_node.value == value:
            node = self.first_node
            self.first_node = self.first_node.next
            del node
            return True
        else:
            return False

    def remove_refactored(self, value):
        # Se a lista nao estiver vazia, procura-se value para remover.
        if not self.empty():
            # Se nao encontrou no primeiro node, procura-se nos proximos
            # para remover.
            if not self.remove_first(value):
                prev_node = self.first_node
                node = prev_node.next
                while node is not None:
                    if node.value == value:
                        prev_node.next = node.next
                        del node
                        return True
                    prev_node = node
                    node = node.next
            else:  # Encontrou no primeiro node.
                return True
        return False

    def remove_tail(self, value):
        """Remove apenas do segundo node pra frente (se econtrar)"""
        prev_node = self.first_node
        node = prev_node.next
        while node is not None:
            if node.value == value:
                prev_node.next = node.next
                del node
                return True
            prev_node = node
            node = node.next
        return False

    def remove_refactored2(self, value):
        if not self.empty():
            if not self.remove_first(value):
                return self.remove_tail(value)
            else:
                return True
        return False

    def improved_remove(self, value):
        if not self.empty():
            return self.remove_first(value) or self.remove_tail(value)
        else:
            return False

    def reset(self):
        """Reset the list to size 0"""
        node = self.first_node
        while node.next is not None:
            node_to_del = node
            node = node.next
            del node_to_del
        self.first_node = None

    def empty(self):
        return self.first_node is None  # self.first_node == None

    def print_(self):
        aux_node = self.first_node
        # while aux_node != None:
        while aux_node is not None:
            print(aux_node.value, end=' ')
            aux_node = aux_node.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def main():
    # reset_tests()
    removing_tests()
    # addat_end_tests()
    # search_tests()
    # update_tests()


def addat_start_tests():
    print('Addat start tests')
    list_ = List()  # Nova lista.
    list_.addat_start(1)
    list_.addat_start(2)
    list_.addat_start(3)
    list_.addat_start(4)
    list_.addat_start(5)
    list_.addat_start(6)
    list_.addat_start(7)
    list_.addat_start(8)
    print(list_)


def addat_end_tests():
    print('Addat end tests')
    list_ = List()  # Nova lista.
    list_.addat_end(1)
    list_.addat_end(2)
    list_.addat_end(3)
    list_.addat_end(4)
    list_.addat_end(5)
    print(list_)


def removing_tests():
    print('Removing tests')
    list_ = List()  # Nova lista.
    list_.addat_start(1)
    list_.addat_start(2)
    list_.addat_start(3)
    list_.addat_start(4)
    list_.addat_start(5)
    list_.addat_start(6)
    list_.addat_start(7)
    list_.addat_start(8)
    print(list_)
    # list_.print_()

    value = 8
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 1
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 7
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 4
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 10
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 6
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 5
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 3
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 2
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)

    value = 0
    print(f'Revoving {value}:', list_.remove(value))
    print(list_)


def reset_tests():
    print('Reset tests')
    list_ = List()  # Nova lista.
    list_.addat_start(1)
    list_.addat_start(2)
    list_.addat_start(3)
    list_.addat_start(4)
    list_.addat_start(5)
    list_.addat_start(6)
    list_.addat_start(7)
    list_.addat_start(8)
    print(list_)
    list_.reset()
    print('Reseted list')
    print(list_)


def search_tests():
    print('Search tests')
    list_ = List()  # Nova lista.
    for value in range(10):
        list_.addat_end(value)
    print(list_)
    value = 5
    print(f'Searching {value}:', list_.search(value))
    value = 10
    print(f'Searching {value}:', list_.search(value))
    value = 11
    print(f'Searching {value}:', list_.search(value))
    value = 2
    print(f'Searching {value}:', list_.search(value))
    value = 6
    print(f'Searching {value}:', list_.search(value))


def update_tests():
    print('Update tests')
    list_ = List()  # Nova lista.
    for value in range(10):
        list_.addat_end(value)
    print(list_)
    value, new_value = 5, 50
    print(f'Updating {value} -> {new_value}:', list_.update(value, new_value))
    print(list_)
    value, new_value = 6, 60
    print(f'Updating {value} -> {new_value}:', list_.update(value, new_value))
    print(list_)
    value, new_value = 9, 90
    print(f'Updating {value} -> {new_value}:', list_.update(value, new_value))
    print(list_)
    value, new_value = 10, 10
    print(f'Updating {value} -> {new_value}:', list_.update(value, new_value))
    print(list_)


if __name__ == '__main__':
  main()
