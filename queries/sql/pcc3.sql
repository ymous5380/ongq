create or replace recursive view tc1(src, trg) as (
    select subject, object
    from serial_triples
    where predicate = '&0'
    union
    select tc1.src, s.object
    from tc1, serial_triples as s
    where tc1.trg = s.subject and
           s.predicate = '&0'
);

create or replace recursive view tc2(src, trg) as (
    select subject, object
    from serial_triples
    where predicate = '&1'
    union
    select tc1.src, s.object
    from tc1, serial_triples as s
    where tc1.trg = s.subject and
       s.predicate = '&1'
);

create or replace recursive view tc3(src, trg) as (
   select subject, object
   from serial_triples
   where predicate = '&2'
   union
   select tc1.src, s.object
   from tc1, serial_triples as s
   where tc1.trg = s.subject and
           s.predicate = '&2'
);

select count(*)
from tc1, tc2, tc3
where tc1.src = tc2.src and
      tc1.src = tc3.src and
      tc1.trg = tc2.trg and
      tc1.trg = tc3.trg;
