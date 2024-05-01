#include "iostream"
#include "string"
using namespace std;

string ReverseFunction(int array[][4], string InputStr, int index) {
   int number = array[index][0];
   int len = array[index][1];

   cout << "number의값:" << number << " len의값:" << len << endl;
   for (int j = array[index][0]; j <= array[index][1]; j++) {
      if (InputStr[len] == ' ') {
         len--;
         continue;
      }
      char temp = InputStr[number];
      InputStr[number] = InputStr[len];
      InputStr[len] = temp;
      number++;
      len--;

      if (j == (array[index][0] + array[index][1]) / 2) {
         break;
      }
   }
   cout << InputStr << endl;
   return InputStr;
}

int main() {
   string str;

   int reverseNum[][4] = { {0,7},{4,6},{5,14},{2,7} };
   getline(cin, str);
   for (int index = 0; index < 4; index++) {
      str = ReverseFunction(reverseNum, str, index);
   }
   cout << str;
   return 0;
}

