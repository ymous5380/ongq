with recursive tc1(src, trg) as (
    select subject, object
    from serial_triples
    where predicate = '&2'
    union
    select tc1.src, s.object
    from tc1, serial_triples as s
    where tc1.trg = s.subject and
            s.predicate = '&2'
),
inn(src, trg) as (
    select s1.subject, s1.object
    from serial_triples as s1, tc1
    where s1.predicate = '&1' and
        tc1.trg = '&3' and
        s1.subject = tc1.src
),
aux2(src, trg) as (
    with recursive tc2(src, trg) as (
        select src, trg
        from inn
        union
        select tc2.src, i.trg
        from tc2, inn as i
        where tc2.trg = i.src
    )
    select * from tc2
)
select count(*)
from serial_triples as r, aux2 as t
where r.predicate = '&0' and
      r.object = t.src;
