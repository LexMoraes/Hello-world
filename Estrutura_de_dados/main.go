package main

import "fmt"

type Node struct {
	value int
	next  *Node
	prev  *Node
	size  int
}

type DoublyLinkedList struct {
	head *Node
	tail *Node
}

func (list *DoublyLinkedList) Append(value int) {
	newNode := &Node{value: value}
	if list.head == nil { // Se a cabeça da lista for nula:
		list.head = newNode // Cabeça da lista recebe o novo nó
		list.tail = newNode // Cauda da lista recebe o novo nó
	} else { // Caso a cabeça da lista não seja nulo:
		list.tail.next = newNode //  O próximo da cauda recebe o novo nó
		newNode.prev = list.tail // O anterior do nó recebe a cauda
		list.tail = newNode      // A cauda recebe o novo nó
	}
}

func (list *DoublyLinkedList) Remove(value int) {
	current := list.head
	for current != nil && current.value != value { // Enquanto o atual for != de nulo
		current = current.next // E o valor do atual for != do valor a ser removido
	} // O valor atual recebe o próximo do valor atual

	if current != nil { // Se o atual é != de nulo
		// Entra nas demais validações:
		// Primeira validação: verificação do elemento anterior;
		if current.prev != nil { // Se o anterior ao atual for != de nulo:
			current.prev.next = current.next // O próximo do anterior recebe o próximo do atual
		} else { // Se o anterior do atual for nulo:
			list.head = current.next // A cabeça da lista recebe o próximo do atual
		}
		// Segunda validação: verificação do elemento posterior;
		if current.next != nil { // Se o próximo do atual for != de nulo:
			current.next.prev = current.prev // O anterior do próximo recebe o anterior do atual
		} else { // Se o próximo do atual for = a nulo;
			list.tail = current.prev // A cauda da lista recebe o anterior do atual.
		}
	}
}

func (list *DoublyLinkedList) Print() {
	current := list.head
	for current != nil {
		fmt.Print(current.value, " <-> ")
		current = current.next
	}
}

func (list *DoublyLinkedList) PrintReverse() {
	current := list.tail
	for current != nil {
		fmt.Print(current.value, " <-> ")
		current = current.prev
	}
}

func main() {
	dlist := DoublyLinkedList{}
	dlist.Append(1)
	dlist.Append(2)
	dlist.Append(3)
	dlist.Append(4)
	dlist.Append(5)
	dlist.Append(6)
	dlist.Print()
	fmt.Println("\n_______________________________________\n")
	dlist.Remove(6)
	dlist.PrintReverse()
	fmt.Println("\n_______________________________________\n")

}
