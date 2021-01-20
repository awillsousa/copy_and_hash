from copy_and_hash import copia_hasheando


arquivo_in = '/home/willian/desenv/sandbox/forensics/arquivao.txt'
arquivo_out = '/home/willian/desenv/sandbox/forensics/copia_arquivo.txt'
hashes_req = ["md5", "sha256"]

copia_hasheando(arquivo_in, arquivo_out, hashes_req)
