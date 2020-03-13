#include "two_sum.hpp"
#include <iostream>
#include <array>
#include <vector>

using namespace std;


int main()
{
  vector <int> inputvec = {1, 3, 5, 7, 9, 12, 15};
  int target = 14;
  vector <int> a = twoSum(inputvec,target);

  cout << a[0] << '\n';
  cout << a[1] << '\n';

  return 0;
}