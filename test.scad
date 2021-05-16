module a()
  cube([10, 10, 10]);

module bla (  first    ,second, third,fourth) {

    local = if(first) second[0] else third;
}

module blub(first) bla(blub);
module blub2(first) bla(0, [0, 0], 0, 0);

function aaa(a) = a * 2;
function bbb(c) = let(a=1) if(a==1) b(a,c) else 2;

