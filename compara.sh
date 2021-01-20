# Cria arquivo de teste
./cria_arquivo_teste.sh

# Usando dcfldd
echo ""
echo "-----------------------------------"
echo "Usando dcfldd com block size de 64M"
echo "-----------------------------------"
time dcfldd if=arquivao.txt bs=64M hash=sha256,md5 of=novo_arquivo.txt

# Usando python
echo ""
echo "-----------------------------------"
echo "Usando python com block size de 64K"
echo "-----------------------------------"
time python copy_and_hash.py --input arquivao.txt --output novo_arquivo.txt --block_size 64

# Limpa arquivos
rm arquivao.txt
rm novo_arquivo.txt
