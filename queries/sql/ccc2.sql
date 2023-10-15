with recursive tc(src, trg) as (
    select subject, object
    from serial_triples
    where predicate = '&0'
    union
    select tc.src, s.object
    from tc, serial_triples as s
    where predicate = '&0' and
          tc.trg = s.subject
)
select count(*)
from tc, serial_triples as b, serial_triples as c
where b.predicate = '&1' and
      c.predicate = '&2' and
    tc.src = b.subject and
    tc.trg = c.subject and
    b.object = c.object;
