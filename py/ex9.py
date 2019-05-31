#!/bin/python

## Lista Duplamente Ligada
class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None


class Lista:
  def __init__(self):
    self.first_node = None

  def __str__(self):
    node = self.first_node
    string = ""
    while node is not None:
      string += f"{node.value} "
      node = node.next
    return string

  def add_end(self, value):
    new_node = Node(value)
    #
    if self.first_node is None:
      self.first_node = new_node
    else:
      node = self.first_node
    #
      while node.next is not None:
        node = node.next
    #
      node.next = new_node
      new_node.prev = node

  def add_start(self, value):
    new_node = Node(value)
    if self.first_node is None:
      self.first_node = new_node
      return
    #
    new_node.next = self.first_node
    self.first_node.prev = new_node
    self.first_node = new_node


  def find(self, value):
    node = self.first_node
    i = 0
    #
    while node.next is not None:
      if node.value == value:
        print(i)
        return
      node = node.next
      i += 1
    #
    return False
  

  def find_all(self, value):
    node = self.first_node
    index = Lista()
    i = 0
    #
    while node.next is not None:
      if node.value == value:
        index.add_end(i)
      node = node.next
      i += 1
    #
    if index.first_node is None:
      return False
    else:
      print(index)


  def sub(self, value, new_value):
    node = self.first_node
    nova_lista = Lista()
    #
    while node is not None:
      if node.value == value:
        node.value = new_value
        return True
      node = node.next
    return False


  def sub_all(self, value, new_value):
    node = self.first_node
    nova_lista = Lista()
    i = 0
    #
    while node is not None:
      if node.value == value:
        node.value = new_value
        i += 1
      node = node.next
    if i >= 1:
      return True
    else:
      return False


    #
    self = nova_lista

  def del_val(self, value):
    i = 0
    if self.first_node.value == value:
      self.first_node = self.first_node.next
      self.first_node.prev = None
      return True
    #
    node = self.first_node
    while node.next is not None:
      if node.value == value:
        i += 1
        break;
      node = node.next
    if node.next is not None:
      node.prev.next = node.next
      node.next.prev = node.prev
    else:
      if node.value == value:
        node.prev.next = None

    if i >= 1:
      return True
    else:
      return False


  def del_all(self, value):
    i = 0
    if self.first_node.value == value:
      self.first_node = self.first_node.next
      self.first_node.prev = None
    #
    node = self.first_node
    while node is not None:
      if node.value == value:
        if node.next is not None:
          node.prev.next = node.next
          node.next.prev = node.prev
        else:
          if node.value == value:
            node.prev.next = None
        i += 1
      node = node.next
    if i >= 1:
      return True
    else:
      return False

def main():
  print("Criando a lista e adicionando valores no final")
  a = Lista()
  a.add_end(1)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(2)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(2)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(1)
  print(a)
  a.add_end(5)
  print(a)
  print("Adicionando valores no inicio")
  a.add_start(5)
  print(a)
  print("Buscando primeira ocorrencia do valor 2")
  a.find(2)
  print("Buscando todas as ocorrencias do valor2")
  a.find_all(2)
  print("Alterando o primeiro 5")
  print(a.sub(5, 4))
  print(a)
  print("Alterando todos os 2")
  print(a.sub_all(2, 3))
  print(a)
  print("Removendo o valor 5")
  print(a.del_val(5))
  print(a)
  print("Removendo todos os 3")
  print(a.del_all(3))
  print(a)
  print("Falhando ao buscar o valor 2")
  print(a.find(2))
  print(a.find_all(2))
  print("Falhando ao alterar o valor 2")
  print(a.sub(2, 3))
  print(a.sub_all(2, 3))
  print("Falhando remover o valor 2")
  print(a.del_val(2))
  print(a.del_all(2))

if __name__ == "__main__":
  main()
