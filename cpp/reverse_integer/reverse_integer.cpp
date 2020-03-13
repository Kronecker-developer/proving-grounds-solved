#include "reverse_integer.hpp"
#include <iostream>

signed int reverse(signed int y)
{
  std::string out="";
  if (y==0)
  {
    return 0;
  }
  while (y % 10 == 0)
  {
    y = y / 10;
  }

  if (y < 0)
  {
    y = y*(-1);
    while (y>0)
    {
      out = out+std::to_string(y%10);
      y = y / 10;
    }
    return (-1)*std::stoi(out);
  }

  while (y>0)
  {
    out = out+std::to_string(y%10);
    y = y / 10;
  }
  return std::stoi(out);
}
