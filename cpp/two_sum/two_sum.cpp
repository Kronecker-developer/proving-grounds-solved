#include <iostream>
#include <array>
#include <vector>

using namespace std;

vector <int> twoSum(vector <int> inputvec, int target)
{
  vector <int> answer(2);
  int n = inputvec.size();

  for (int i=0; i<n-1; i++)
  {
    for (int j=i+1; j<n; j++)
    {
      if (inputvec[i]+inputvec[j]==target)
      {
        answer[0]=i;
        answer[1]=j;
      }
    }
  }
  return answer;
}
