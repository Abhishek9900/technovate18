#include <iostream>
#include <fstream>
using namespace std;
int main()
{
   fstream o("materialize.min.css",ios::in);
   fstream f("temp.css",ios::out);
  while(o)
  {  char ch= o.get();
     f.put(ch);
     if(ch=='}')
      f.put('\n');
   }
   o.close();
   f.close();
return 0; 
}
