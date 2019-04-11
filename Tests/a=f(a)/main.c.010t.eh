
;; Function f (f, funcdef_no=0, decl_uid=2248, cgraph_uid=0, symbol_order=0)

f (int a)
{
  int D.2254;

  D.2254 = a;
  goto <D.2255>;
  <D.2255>:
  return D.2254;
}



;; Function main (main, funcdef_no=1, decl_uid=2250, cgraph_uid=1, symbol_order=1)

main ()
{
  int a;
  int D.2268;

  a = 0;
  if (a == 0) goto <D.2256>; else goto <D.2257>;
  <D.2256>:
  if (a == 1) goto <D.2258>; else goto <D.2259>;
  <D.2258>:
  if (a == 2) goto <D.2260>; else goto <D.2261>;
  <D.2260>:
  a = 3;
  <D.2261>:
  <D.2259>:
  a = 4;
  <D.2257>:
  if (a == 0) goto <D.2262>; else goto <D.2263>;
  <D.2262>:
  _1 = a == 1;
  _2 = a == 2;
  _3 = _1 & _2;
  if (_3 != 0) goto <D.2264>; else goto <D.2265>;
  <D.2264>:
  a = 3;
  <D.2265>:
  a = 4;
  <D.2263>:
  if (1 != 0) goto <D.2266>; else goto <D.2267>;
  <D.2266>:
  a = 3;
  <D.2267>:
  D.2268 = 1;
  goto <D.2269>;
  a = a + 1;
  D.2268 = 0;
  goto <D.2269>;
  D.2268 = 0;
  goto <D.2269>;
  <D.2269>:
  return D.2268;
}


