#include <stdio.h>

int main() {
    char your_input[7];

    scanf("%s", your_input);

    char* correct = "cr4ckme";

    for (int i = 0; i < strlen(correct); i++) {
        printf("%c", correct[i] - 1);
    }

    for (int i = 0 ; i < strlen(correct) ; i++)
    {
        if (correct[i] - 1 != your_input[i]) {
            printf("Wrong Answer");
            return 1;
        }
    }
    printf("Good Job!");
}                        