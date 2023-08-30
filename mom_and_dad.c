#include <stdio.h>

int main(){
    char your_input[9] = "Snowballs";
    // char flag[9];

    int j, i = 0;
    char Baby[9], DAD[] = "zlBnSaoO24GeliI", MOM[] = "dYbWqlL8wsSk5jfduU8";
    printf("%d\n", strlen(your_input));
    if (strlen(your_input) != 9 || your_input[0] != DAD[4])
    {
        printf("Wrong Input");
        exit(0);
    }

    for (j = 8; j >= 0; j--)
    {
        Baby[i] = your_input[j];
        i++;
    }
    printf("%s\n", Baby);
    Baby[j] = '\0';
    if ((Baby[0] == MOM[9]) && (Baby[7] == DAD[3]) && (Baby[1] == MOM[5]) && (Baby[6] == DAD[6]) && (Baby[2] == DAD[1]) && (Baby[5] == MOM[8]) && (Baby[3] == DAD[5]) && (Baby[4] == MOM[2]))
    {
            printf("Good Job!");
    }
    else
    {
        printf("Wrong Answer");
    }
    // flag[0] = MOM[9]; 
    // flag[1] = MOM[5]; 
    // flag[2] = DAD[1]; 
    // flag[3] = DAD[5]; 
    // flag[4] = MOM[2]; 
    // flag[5] = MOM[8]; 
    // flag[6] = DAD[6]; 
    // flag[7] = DAD[3];

    // printf("\n%s\n", flag);
    // Results - sllabwon (reverse in python [::-1] give nowballs)
    // First letter should be - S
    // 
}