import itertools

def truth_table(expression):
    
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([0, 1], repeat=3))
    
    
    print(f"{'A':<4}{'B':<4}{'C':<4}{'Result':<8}")
    print("-" * 20)
    
    pcnf_terms = []
    pdnf_terms = []

    for combination in combinations:
        A, B, C = combination
     
        result = eval(expression)
        
     
        print(f"{A:<4}{B:<4}{C:<4}{result:<8}")
        
     
        if result == 0:
            pcnf_term = f"({'A' if A == 0 else '~A'}) AND ({'B' if B == 0 else '~B'}) AND ({'C' if C == 0 else '~C'})"
            pcnf_terms.append(f"({pcnf_term})")
        else:
            pdnf_term = f"({'A' if A == 1 else '~A'}) AND ({'B' if B == 1 else '~B'}) AND ({'C' if C == 1 else '~C'})"
            pdnf_terms.append(f"({pdnf_term})")
    
    
    pcnf = " OR ".join(pcnf_terms)
    pdnf = " OR ".join(pdnf_terms)
    
    print("\nPDNF:")
    print(pdnf if pdnf else "None")
    print("\nPCNF:")
    print(pcnf if pcnf else "None")


expression = input("Enter a boolean expression using variables A, B, and C (e.g., A and B or C): ")
truth_table(expression)
