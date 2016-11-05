%The Great Big Recursion experiment
place(aberdeen).
place(dundee).
place(edinburgh).
place(glasgow).
place(kirkcaldy).
place(standrews).
place(berlin).
place(hamburg).
place(biedefeld).
distance(aberdeen, dundee, 60).
distance(dundee, edinburgh, 60).
distance(standrews, edinburgh, 60).
distance(dundee, standrews, 10).
distance(standrews, kirkcaldy, 30).
distance(kirkcaldy, edinburgh, 35).
distance(glasgow, edinburgh, 45).
distance(edinburgh, berlin, 200).
distance(berlin, hamburg, 10).
distance(hamburg, biedefeld, 2).
distance(berlin, biedefeld, 3).
distance(X,X,0).
finddistance(X,Y,Z) :- distance(X,Y,Z), place(X),place(Y) ; distance(Y,X,Z), place(X), place(Y).
recursivedistance(From, To, Distance) :- finddistance(From, To, Distance),! ; recursivedistance(From, X, D1) , recursivedistance(To, Y, D2), recursivedistance(X, Y, D3), Distance is D1+D2+D3,!.
