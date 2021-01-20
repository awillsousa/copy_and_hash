#!/usr/bin/python

import sys
import os
import hashlib
import argparse

HASHES_SUPPORT = hashlib.algorithms_guaranteed

def copia_hasheando(arquivo_in, arquivo_out, hashes_req, block_size):
    # Verifica se os algoritmos de hashes passados são suportados
    hashes_calc = []
    for hash_alg in hashes_req:
        if hash_alg not in HASHES_SUPPORT:
            print("Algoritmo {} não suportado.".format(hash_alg))
        else:
            hashes_calc.append(hashlib.new(hash_alg))

    # Executa a copia e calculo dos hashes
    try:
        with open(arquivo_in, 'rb') as arq_in_fp:
            with open(arquivo_out, 'wb') as arq_out_fp:
                bloco = arq_in_fp.read(block_size)
                while bloco:
                    for hash_obj in hashes_calc:
                        hash_obj.update(bloco)

                    arq_out_fp.write(bloco)
                    bloco = arq_in_fp.read(block_size)

        # Exibe os hashes calculados
        for hash_obj in hashes_calc:
            print("{0}: {1}".format(hash_obj.name, hash_obj.hexdigest()))

    except OSError as erro:
        print(erro)    
        arq_in_fp.close()
        arq_out_fp.close()
        sys.exit(1)



def main():
    print("Iniciando processo de cópia.")
    print("Argumentos passados: {}".format(args))
    
    # Verifica o arquivo de entrada
    if args.input == args.output:
        print("Arquivo de entrada e de saída devem ser diferentes.")
        sys.exit(1)

    # Verifica o arquivo de entrada
    if not os.path.isfile(args.input):
        print("Arquivo de entrada não localizado.")
        sys.exit(1)
    
    # Verifica o caminho do arquivo de saída
    dir_out = os.path.dirname(args.output)
    if dir_out and not os.path.isdir(dir_out):
        print("Caminho do arquivo de saída inválido.")
        sys.exit(1)

    copia_hasheando(arquivo_in=args.input, arquivo_out=args.output,
                    hashes_req=args.hashes, block_size=args.block_size*1024)

    print("Processo de cópia encerrado.")



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Programa para copiar um arquivo e calcular o seu hash ao mesmo tempo.')
    parser.add_argument('--hashes', metavar='N', type=str, nargs='+', 
            help='Lista dos hashes a serem calculados.'+' Valores possíveis: '+str(HASHES_SUPPORT),
                        default=["md5", "sha256"])
    parser.add_argument('--input', type=str, help='Caminho completo do arquivo de entrada.')
    parser.add_argument('--output', type=str, help='Caminho completo do arquivo de saida.')
    parser.add_argument('--block_size', type=int, default=64, help='Tamanho do bloco em KB.')
    args = parser.parse_args()

    FLAGS, unparsed = parser.parse_known_args()
    main()



