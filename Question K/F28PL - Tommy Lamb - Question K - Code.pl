person(jake).
person(jill).
person(john).
person(joan).
likes(jake, tomato).
likes(jill, cheese).
likes(jill, tomato).
likes(john, cheese).
likes(joan, tomato).
likes(joan, cheese).
likes(X, pizza) :- likes(X,tomato), likes(X, cheese).
knows(jake, jill).
knows(jill, john).
knows(john, joan).
knows(joan, jake).
knows(X,X) :- person(X).

place(aberdeen).
place(dundee).
place(edinburgh).
place(glasgow).
place(kirkcaldy).
place(standrews).
distance(aberdeen, dundee, 60).
distance(dundee, edinburgh, 60).
distance(standrews, edinburgh, 60).
distance(dundee, standrews, 10).
% distance(dundee, aberdeen,60). %Superfluous, serves only to give duplicates
distance(standrews, kirkcaldy, 30).
distance(kirkcaldy, edinburgh, 35).
distance(glasgow, edinburgh, 45).
distance(X,X,0).
finddistance(X,Y,Z) :- distance(X,Y,Z), place(X),place(Y) ; distance(Y,X,Z), place(X), place(Y).
indirectdistance(X,Y,A,Z) :- finddistance(X,Y,Z) ; finddistance(X,A,B), finddistance(A,Y,C), Z is C+B.
recursivedistance(From, To, Distance) :- finddistance(From, To, Distance),! ; recursivedistance(From, X, D1) , recursivedistance(To, Y, D2), recursivedistance(X, Y, D3), Distance is D1+D2+D3,!.
