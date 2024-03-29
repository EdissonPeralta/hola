#include <iostream>
#include <cstdlib>

int main (int argc, char **argv)
{
  std::cout.precision(16); std::cout.setf(std::ios::scientific);
  float under =1.0, over=1.0;
  const int N=std::atoi(argv[1]);
  for (int ii = 0; ii<N; ++ii)
    {
      under /=2;
      over *=2;
      std::cout<<ii<<"\t"<<under<<"\t"<<over<<std::endl;
    }
  return 0;
}
