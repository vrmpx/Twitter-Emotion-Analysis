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
				if (strcmp(pch + strlen(pch) - 3, "n't") == 0 || 
					strcmp(pch, "never") == 0 || strcmp(pch, "no") == 0 || strcmp(pch, "nothing") == 0 || 
					strcmp(pch, "nowhere") == 0 || strcmp(pch, "noone") == 0 || strcmp(pch, "none") == 0 || 
					strcmp(pch, "not") == 0 || strcmp(pch, "havent") == 0 || strcmp(pch, "hasnt") == 0 || 
					strcmp(pch, "hadnt") == 0 || strcmp(pch, "cant") == 0 || strcmp(pch, "couldnt") == 0 || 
					strcmp(pch, "shouldnt") == 0 || strcmp(pch, "wont") == 0 || strcmp(pch, "wouldnt") == 0 || 
					strcmp(pch, "dont") == 0 || strcmp(pch, "doesnt") == 0 || strcmp(pch, "didnt") == 0 || 
					strcmp(pch, "isnt") == 0 || strcmp(pch, "arent") == 0 || strcmp(pch, "aint") == 0){

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