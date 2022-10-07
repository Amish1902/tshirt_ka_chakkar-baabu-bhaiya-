#include <bits/stdc++.h>
using namespace std;
int findDuplicate(vector<int> &A)
{
  int n = A.size();
  for (int i = 0; i < n; i++)
  {
    A[A[i] % n] = A[A[i] % n] + n;
  }
  for (int i = 0; i < n; i++)
  {
    if ((A[i] / n) > 1)
    {
      return i;
    }
  }
  return 0;
}
int main()
{
  int n;
  cout << "Enter size of the array : ";
  cin >> n;
  vector<int> v;
  cout << "Enter elements of the array :" << endl;
  for (int i = 0; i < n; i++)
  {
    int x;
    cin >> x;
    v.push_back(x);
  }
  cout << "Duplicate number in the array is: ";
  cout << findDuplicate(v);
}
