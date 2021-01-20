# copy_and_hash
Script python + shell para comparar copia e hash simultâneo no python vs dcfldd

O dcfldd é uma versão modificado do dd que consegue executar o processo de cópia
e hash em paralelo, inclusive ele realizar o cálculo simultâneo de mais de um 
tipo de hash ao mesmo tempo. 

O copy_and_hash.py é o script que simula o mesmo comportamento do dcfldd, mas utilizando
as bibliotecas do python para cópia de arquivos e cálculo de hash. 

Para baixar e instalar o dcfldd no Ubuntu:
sudo apt-get update -y
sudo apt-get install -y dcfldd

Eu prefiro instalar o pacote todo do *forensics-all*, mas fica a seu critério. 

Para comparar basta executar o "compara.sh"

Os scripts dd_ibs_test.sh e dd_obs_test.sh, que não foram feitos por mim, servem para 
determinar qual o melhor tamanho de bloco.

O exec.py é quem chama o script de cópia, recebendo o arquivo de entrada, o tamanho do bloco
e o arquivo de saída. 

Uma desvatagem em relação ao dd é que o script python não está pronto para receber dados 
da stdin. Se você quiser acrescentar isso, eu agradeço. :D
