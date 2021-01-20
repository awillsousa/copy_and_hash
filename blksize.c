#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>

// Codigo para imprimir o tamanho do bloco
int main()
{
  struct stat fi;
  stat("/", &fi);
  printf("%d\n", fi.st_blksize);
  return 0;
}
