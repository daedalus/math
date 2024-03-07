leibniz_pi = lambda n: 4*sum(((-1)**(k-1))/(k*2-1) for k in range(1, n+1))
leibniz_pi = lambda n: 4*sum(((-1)*((k-1)&1)+((k-1)&1==0))/((k<<1)-1) for k in range(1, n+1))
