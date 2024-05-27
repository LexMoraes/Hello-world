package main

import (
	"errors"
	"fmt"
)

type Impressora struct {
	proximo   *Impressora
	documento string
}

type filaImpressao struct {
	frente  *Impressora
	final   *Impressora
	tamanho int
}

func (fila *filaImpressao) Enfileirar(doc string) {

	novoDoc := &Impressora{documento: doc}
	if fila.frente == nil {
		fila.frente = novoDoc
		fila.final = novoDoc
		fmt.Println(novoDoc, "adicionado à fila de impressão.")
	} else {
		fila.final.proximo = novoDoc
		fila.final = novoDoc
		fmt.Println(novoDoc, "adicionado à fila de impressão.")
	}
	fila.tamanho++
}

func (fila *filaImpressao) Remover() (string, error) {
	if fila.frente == nil {
		return "", errors.New("Fila de impressão vazia")
	}
	doc := fila.frente.documento
	fila.frente = fila.frente.proximo
	if fila.frente == nil {
		fila.final = nil
	}
	fila.tamanho--
	return doc, nil
}

func (lista *filaImpressao) Imprimir(f func(string)) {
	atual := lista.frente
	for atual != nil {
		fmt.Println(*atual)
		f(atual.documento)
		atual = atual.proximo
	}
}

func main() {
	var doc Impressora

	for {

		fmt.Print("Digite o nome do documento a ser impresso: ")
		fmt.Scan(&doc.documento)

		filaImpressao.Enfileirar(doc.documento)

		if doc.documento == "0" {
			break
		}
	}
}