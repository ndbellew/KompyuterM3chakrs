#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  int a, b, c, i;
  cin >> a >> b >> c;
  double size = sqrt(b*b+c*c);
  int num;
  string ans[1000] = {};
  for(i=0; i<a; i++)
  {
    cin >> num;
    if(num <= size) ans[i] = "DA";
    else ans[i] = "NE";
  }
  for(i=0; i<a; i++) cout << ans[i] << endl;

  return 0;
}
