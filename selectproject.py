
"""
	Given a list of relations r
        r =  [{"A" : 1, "B" : 4, "C" : 3},
             {"A" : 2, "B" : 5, "C" : 2},
             {"A" : 3, "B" : 6, "C" : 1}]

Implement select
		select(r, unary predicate)

	Ex: select(r, lambda d : d["A"] > 0)

		returns the whole list

"""



""" Given a list of relations r
              r =  [{"A" : 1, "B" : 4, "C" : 3},
             		{"A" : 2, "B" : 5, "C" : 2},
             		{"A" : 3, "B" : 6, "C" : 1}]

Implement project
		select(r, list of attributes)
		EX: select(r, "A", "B", "C")

		returns the whole list