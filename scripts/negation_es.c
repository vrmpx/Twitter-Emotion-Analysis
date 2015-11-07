#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
	size_t n = 1024;
	char *buffer = malloc(n);
	char *pch;
	int NEG;

	while(getline(&buffer, &n, stdin) != -1){
		
		pch = strtok(buffer, " ");
		NEG = 0;

		while (pch != NULL){

			//Check if token starts w/ punctuation
			if (NEG == 1 && (strcmp(pch, "?") == 0 || 
							 strcmp(pch, ",") == 0 || 
							 strcmp(pch, ";") == 0 || 
							 strcmp(pch, "!") == 0 ||
							 strcmp(pch, ".") == 0 || 
							 strcmp(pch, ":") == 0 )){
				NEG = 0;
			}

			if (NEG == 1){
				printf("NEG_%s", pch);
			} else {
				printf("%s", pch);
			}
			if (strcmp("\n", pch + strlen(pch) - 1) != 0){
					printf(" ");
			}

			//Check for negation
			if (NEG == 0) {
				if (strcmp(pch, "nunca") == 0 || strcmp(pch, "no") == 0 || strcmp(pch, "nada") == 0 || 
					strcmp(pch, "ningun") == 0 || strcmp(pch, "ni") == 0 || strcmp(pch, "ninguno") == 0 ||
					strcmp(pch, "ninguna") == 0 || strcmp(pch, "jamás") == 0 || strcmp(pch, "jamas") == 0 ||
					strcmp(pch, "tampoco") == 0 || strcmp(pch, "sin") == 0){

						NEG = 1;
	
				}
			}else {
				//Check if token ends in punct before next token
				if (strcmp("?", pch + strlen(pch) - 1) == 0 || 
					strcmp(",", pch + strlen(pch) - 1) == 0 || 
					strcmp(".", pch + strlen(pch) - 1) == 0 || 
					strcmp(";", pch + strlen(pch) - 1) == 0 || 
					strcmp(":", pch + strlen(pch) - 1) == 0 || 
					strcmp("!", pch + strlen(pch) - 1) == 0){
					NEG = 0;
				}
			}


			pch = strtok (NULL, " ");
		}
		// printf("\n");
	}
	return 0;
}