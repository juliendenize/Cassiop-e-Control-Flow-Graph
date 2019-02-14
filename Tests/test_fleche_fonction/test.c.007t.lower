
;; Function foo (foo, funcdef_no=0, decl_uid=2248, cgraph_uid=0, symbol_order=0)

foo (int a)
{
  int D.2258;

  if (a > 0) goto <D.2256>; else goto <D.2257>;
  <D.2256>:
  D.2258 = -a;
  goto <D.2259>;
  <D.2257>:
  D.2258 = a;
  goto <D.2259>;
  <D.2259>:
  return D.2258;
}



;; Function main (main, funcdef_no=1, decl_uid=2252, cgraph_uid=1, symbol_order=1)

main (int argc, char * * argv)
{
  int b;
  int D.2263;

  b = 3;
  _1 = foo (b);
  if (_1 > 3) goto <D.2260>; else goto <D.2261>;
  <D.2260>:
  __builtin_puts (&"Large"[0]);
  goto <D.2262>;
  <D.2261>:
  __builtin_puts (&"Small"[0]);
  <D.2262>:
  D.2263 = 0;
  goto <D.2264>;
  D.2263 = 0;
  goto <D.2264>;
  <D.2264>:
  return D.2263;
}


