string your_input = "ABCDEFG";
char[] array = your_input.ToCharArray();
string[] array2 = new string[array.Length];
string enc = "";
string correct = "144260662546426066";
string dec = "";
string temp = "";

for (int i = 0; i < your_input.Length; i++)
{
    array2[i] = Convert.ToString((int)array[i] - 55);
    enc += array2[i];
}

for (int i = 0; i < correct.Length / 2; i++)
{
    Console.WriteLine(Convert.ToString((int)correct[i]));
    temp = "";
    test = 0;
}

Console.WriteLine(enc);
Console.WriteLine(correct);
Console.WriteLine(correct.Length);

if (enc == correct){
    Console.WriteLine("Good job!");}
else{
    Console.WriteLine("Wrong Answer!");}
                            