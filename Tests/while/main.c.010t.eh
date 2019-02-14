
;; Function main (main, funcdef_no=0, decl_uid=2247, cgraph_uid=0, symbol_order=0)

main ()
{
  int a;
  int D.2254;

  a = 0;
  goto <D.2251>;
  <D.2250>:
  a = a + 1;
  <D.2251>:
  if (a <= 999) goto <D.2250>; else goto <D.2252>;
  <D.2252>:
  D.2254 = 0;
  goto <D.2255>;
  D.2254 = 0;
  goto <D.2255>;
  <D.2255>:
  return D.2254;
}


